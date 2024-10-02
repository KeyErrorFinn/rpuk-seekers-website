from flask import Flask, redirect, render_template, request, url_for, flash, send_file
import os


app = Flask(__name__, template_folder='site/templates', static_folder='site/static')


@app.route('/')
def home():
    filename = "home"
    return render_template(f"{filename}.html", template_name=filename)



if __name__ == '__main__':
    # Check if FLASK_ENV is set, if not, default to development
    if not os.environ.get('FLASK_ENV'):
        os.environ['FLASK_DEBUG'] = 'development'

    # Check if the environment is set to development (local)
    if os.environ.get('FLASK_DEBUG') == 'development':
        app.run(debug=True, host='0.0.0.0', port=5000)
    else:
        pass