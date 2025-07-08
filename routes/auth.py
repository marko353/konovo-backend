from flask import Blueprint, request, jsonify
import requests

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    # Prosledi zahtev eksternom API-ju
    response = requests.post(
        'https://zadatak.konovo.rs/login',
        json={'username': username, 'password': password}
    )

    if response.status_code != 200:
        return jsonify({'error': 'Invalid credentials'}), 401

    token = response.json().get('token')
    if not token:
        return jsonify({'error': 'Token not received'}), 500

    return jsonify({'token': token})
