from flask import Flask, request, abort
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with a strong and unique secret key
csrf = CSRFProtect(app)
# Exempt the '/webhook' endpoint from CSRF protection

@app.route('/webhook', methods=['POST'])
@csrf.exempt
def webhook():
    if request.headers.get('Content-Type') == 'application/json':
        payload = request.json
        print("Received payload:", payload)  # Print payload for debugging
        process_payload(payload)
        return 'Webhook received successfully!', 200
    else:
        abort(400, 'Invalid content type')


def process_payload(payload):
    # Add your custom logic to process the GitHub webhook payload
    event_type = request.headers.get('X-GitHub-Event')

    if event_type == 'ping':
        print('Ping event received')
    elif event_type == 'push':
        print('Push event received')
        # You can access details like repository, commits, etc. from the payload
        repository_name = payload['repository']['name']
        print(f'Repository Name: {repository_name}')
        # Add more processing logic as needed


if __name__ == '__main__':
    app.run(port=5000)
