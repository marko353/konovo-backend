from flask import Flask
from flask_cors import CORS
from routes.auth import auth_bp
from routes.products import products_bp
import os

app = Flask(__name__)

# ✅ Pravilna CORS konfiguracija — dozvoli samo frontend sa Vercela
CORS(app, origins=["https://konovo-client.vercel.app"], supports_credentials=True)

# ✅ Registruj blueprint-ove
app.register_blueprint(auth_bp)
app.register_blueprint(products_bp)

# ✅ Pokretanje aplikacije
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",                         # Omogućava pristup spolja
        port=int(os.environ.get("PORT", 5000)), # Render automatski dodeljuje PORT
        debug=True
    )
