from flask import Flask, render_template, jsonify
from cleaner_pandas import clean_data  
# ✅ Import your cleaning logic

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    try:
        # ✅ Use cleaned version of telemetry_log.jsonl
        cleaned_data = clean_data('telemetry_log.jsonl')
    except FileNotFoundError:
        cleaned_data = []  # File doesn't exist yet
    
    return jsonify(cleaned_data)

if __name__ == '__main__':
    app.run(debug=True)
