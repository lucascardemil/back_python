from flask import Blueprint, jsonify, request
from app.functions.image_processing import process_image

scanner_api_bp = Blueprint('scanner_api', __name__)

@scanner_api_bp.route('/api/scanner', methods=['POST'])
def scanner():
    request_data = request.get_json()
    response_data = process_image(request_data)
    return jsonify(response_data)

