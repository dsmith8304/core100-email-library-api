from flask import Flask, request, jsonify
import json, os
app = Flask(__name__)
try:
    script_dir = os.path.dirname(__file__)
    json_path = os.path.join(script_dir, '..', 'Core100EmailLibrary.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        emails = json.load(f)
except Exception as e:
    emails = []
@app.route('/email', methods=['GET'])
def get_email_by_id():
    email_id = request.args.get('email_id')
    if not email_id: return jsonify({"error": "Please provide an email_id parameter."}), 400
    if not emails: return jsonify({"error": "Email data could not be loaded."}), 500
    match = next((e for e in emails if e.get("email_id") == email_id), None)
    if match: return jsonify(match)
    else: return jsonify({"error": f"No email found with ID {email_id}."}), 404
@app.route('/status', methods=['GET'])
def home():
    if not emails: return "Flask API is running, but FAILED to load email data."
    return f"Flask API is running and email data is loaded with {len(emails)} records."
