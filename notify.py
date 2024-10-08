from flask import Flask, request
from email_adapter import EmailAdapter

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Notification API. Use the /send endpoint to send notifications.", 200

@app.route('/send', methods=['POST'])
def send_notification():
    data = request.get_json()
    to_email = data.get('to')
    message = data.get('message')
    subject = data.get('subject')
    adapter = EmailAdapter()
    adapter.send(message=message, to_email=to_email, subject=subject or "Notification")
    return f"Email sent to {to_email} with message: {message}", 200

if __name__ == '__main__':
    # Ensure Flask listens on all available IPs and on port 5000
    app.run(host='0.0.0.0', port=5000)
