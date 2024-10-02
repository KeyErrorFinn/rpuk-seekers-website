from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == '__main__':
    # Check if FLASK_ENV is set, if not, default to development
    if not os.environ.get('FLASK_ENV'):
        os.environ['FLASK_DEBUG'] = 'development'

    # Check if the environment is set to development (local)
    if os.environ.get('FLASK_DEBUG') == 'development':
        # Local development, use Flask's built-in server
        app.run(debug=True, host='0.0.0.0', port=5000)
    else:
        # In production (Docker), Gunicorn will serve the app
        # Nothing to do here because Gunicorn will handle it in Docker
        pass