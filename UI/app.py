from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    data = [
  {
    "Timestamp": "2025-06-17T14:02:15",
    "IP Address": "192.168.1.10",
    "Username": "jdoe",
    "Process Name": "Accessed confidential_report.pdf",
    "Permission": "Allowed"
  },
  {
    "Timestamp": "2025-06-17T14:05:47",
    "IP Address": "192.168.1.23",
    "Username": "asmith",
    "Process Name": "Opened Chrome Browser",
    "Permission": "Allowed"
  },
  {
    "Timestamp": "2025-06-17T14:06:30",
    "IP Address": "10.0.0.56",
    "Username": "bpatel",
    "Process Name": "Accessed URL: http://example.com",
    "Permission": "Allowed"
  },
  {
    "Timestamp": "2025-06-17T14:10:02",
    "IP Address": "192.168.1.15",
    "Username": "mjones",
    "Process Name": "Tried accessing /etc/shadow file",
    "Permission": "Not Allowed"
  },
  {
    "Timestamp": "2025-06-17T14:12:33",
    "IP Address": "10.0.0.19",
    "Username": "rlee",
    "Process Name": "Executed install_script.sh",
    "Permission": "Allowed"
  },
  {
    "Timestamp": "2025-06-17T14:14:18",
    "IP Address": "172.16.5.44",
    "Username": "skhan",
    "Process Name": "Connected USB device",
    "Permission": "Not Allowed"
  },
  {
    "Timestamp": "2025-06-17T14:15:50",
    "IP Address": "192.168.1.48",
    "Username": "dsmith",
    "Process Name": "Logged into email",
    "Permission": "Allowed"
  },
  {
    "Timestamp": "2025-06-17T14:17:21",
    "IP Address": "10.0.0.7",
    "Username": "pgupta",
    "Process Name": "Accessed shared drive: Finance",
    "Permission": "Allowed"
  },
  {
    "Timestamp": "2025-06-17T14:20:39",
    "IP Address": "172.16.10.30",
    "Username": "kumar",
    "Process Name": "Attempted remote desktop connection",
    "Permission": "Not Allowed"
  },
  {
    "Timestamp": "2025-06-17T14:22:10",
    "IP Address": "192.168.0.20",
    "Username": "tnguyen",
    "Process Name": "Opened Task Manager",
    "Permission": "Allowed"
  },
  {
    "Timestamp": "2025-06-17T14:24:12",
    "IP Address": "10.0.1.12",
    "Username": "awilliams",
    "Process Name": "Changed system time settings",
    "Permission": "Not Allowed"
  },
  {
    "Timestamp": "2025-06-17T14:25:40",
    "IP Address": "192.168.2.9",
    "Username": "vsharma",
    "Process Name": "Downloaded file from external site",
    "Permission": "Not Allowed"
  },
  {
    "Timestamp": "2025-06-17T14:27:33",
    "IP Address": "172.16.8.22",
    "Username": "rjohnson",
    "Process Name": "Accessed HR_Policies.docx",
    "Permission": "Allowed"
  },
  {
    "Timestamp": "2025-06-17T14:30:00",
    "IP Address": "10.0.0.88",
    "Username": "npatel",
    "Process Name": "Launched Zoom application",
    "Permission": "Allowed"
  },
  {
    "Timestamp": "2025-06-17T14:31:45",
    "IP Address": "192.168.1.50",
    "Username": "mwang",
    "Process Name": "Attempted to disable antivirus",
    "Permission": "Not Allowed"
  }
]
    # Return the data as JSON
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)



