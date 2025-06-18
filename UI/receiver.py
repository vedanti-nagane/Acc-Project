from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = 'telemetry_log.jsonl'  # Line-delimited JSON format

@app.route('/telemetry', methods=['POST'])
def receive_telemetry():
    try:
        json_data = request.get_json(force=True)

        # Append data to file (each JSON on a new line)
        with open(DATA_FILE, 'a') as f:
            json.dump(json_data, f)
            f.write('\n')  # newline for separation

        print("[+] Received and stored telemetry data.")
        return jsonify({"status": "success"}), 200

    except Exception as e:
        print("[-] Error:", e)
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
