from flask import Flask
from flask_cors import CORS
from routes.auth import auth_bp
from routes.products import products_bp
import os

app = Flask(__name__)

# Pravilna CORS konfiguracija
CORS(app, origins=["https://konovo-client.vercel.app"], supports_credentials=True)

# Registracija ruta
app.register_blueprint(auth_bp)
app.register_blueprint(products_bp)

if __name__ == "__main__":
    app.run(debug=True)


