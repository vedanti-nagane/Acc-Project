# cleaner_pandas.py
import pandas as pd
import ipaddress

def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip.strip())
        return True
    except:
        return False

def clean_data(input_path):
    df = pd.read_json(input_path)

    # 1. Invalid Timestamp
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
    df = df.dropna(subset=['Timestamp'])

    # 2. Invalid Username
    df['Username'] = df['Username'].fillna("Unknown_User")
    df['Username'] = df['Username'].replace(r'^\s*$', "Unknown_User", regex=True)

    # 3. Invalid Permission
    validpermission = ["true", "false"]
    df['Permission'] = df['Permission'].apply(lambda x: x if x in validpermission else "Invalid")

    # 4. Invalid Process Name
    if 'Process Name' in df.columns:
        df['Process Name'] = df['Process Name'].fillna("Unnamed_Process")
        df['Process Name'] = df['Process Name'].replace(r'^\s*$', "Unnamed_Process", regex=True)

    # 5. Improper IP Address
    df = df[df['IP Address'].notna() & (df['IP Address'].str.strip() != '')]
    df = df[df['IP Address'].apply(is_valid_ip)]

    # 6. Duplicate entries
    df = df.drop_duplicates()

    # Reset index and return dict
    df = df.reset_index(drop=True)
    return df.to_dict(orient="records")
