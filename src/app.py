from flask import Flask
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():

    username = os.getenv('USER')
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')
    print(username, email, password)

    return '<h1>Mi primera aplicación deployeada en render</h1>{}{}{}'.format(username,email,password)

def status_404(error):
    return '<h1>CHAVALES! Página no encontrada</h1>'

if (__name__) == '__main__':
    app.register_error_handler(404, status_404)
    app.run(debug=True)
