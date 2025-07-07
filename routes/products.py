from flask import Blueprint, jsonify, request
from services.external_api import get_jwt_token, get_products_from_api
from utils.helpers import process_products, filter_and_search

products_bp = Blueprint("products", __name__)

@products_bp.route("/products", methods=["GET"])
def get_products():
    token = get_jwt_token()
    if not token:
        return jsonify({"error": "Failed to authenticate with external API"}), 401

    products = get_products_from_api(token)
    processed = process_products(products)

    category = request.args.get("category")
    search = request.args.get("search")

    result = filter_and_search(processed, category, search)
    return jsonify(result)

@products_bp.route("/products/<int:product_id>", methods=["GET"])
def get_single_product(product_id):
    token = get_jwt_token()
    if not token:
        return jsonify({"error": "Failed to authenticate with external API"}), 401

    products = get_products_from_api(token)
    processed = process_products(products)

    product = next((p for p in processed if p["id"] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    return jsonify(product)
