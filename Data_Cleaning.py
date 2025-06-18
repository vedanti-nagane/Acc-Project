import pandas as pd
import json

df=pd.read_json("//content//Project//Sample_JSON_data.json")

print(df)
print(df.dtypes)

# 1. Timestamp Invalid
df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
df = df.dropna(subset=['Timestamp'])

# 2. Invalid USername
df['Username'] = df['Username'].fillna("Unknown_User")
df['Username'] = df['Username'].replace(r'^\s*$', "Unknown_User", regex=True) # handles " ", "\t", "\n"

# 3. PermissionWrong Entry
df.reset_index(drop=True, inplace=True)
validpermission=["Allowed", "Not Allowed"]
for i in range(len(df)):
    if df.loc[i, 'Allowed/Not Allowed'] not in validpermission:
        df.loc[i, 'Allowed/Not Allowed'] = "Invalid"

# 4. Invalid ProcessName Entry
df['Process Name'] = df['Process Name'].fillna("Unnamed_Process")
df['Process Name'] = df['Process Name'].replace(r'^\s*$', "Unnamed_Process", regex=True)

# 5. Improper IP Address
df = df[df['IP Address'].notna() & (df['IP Address'].str.strip() != '')]
import ipaddress
def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip.strip())
        return True
    except:
        return False
df = df[df['IP Address'].notna() & df['IP Address'].apply(is_valid_ip)]
df = df.reset_index(drop=True)

# 6. Duplicate Data Entries
df = df.drop_duplicates()
df = df.reset_index(drop=True)
