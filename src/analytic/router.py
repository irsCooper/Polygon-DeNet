from flask import Blueprint, request, jsonify
from src.analytic.service import AnaliticService

app = Blueprint("analytics", __name__)


@app.get("/top")
def get_top():
    offset = int(request.args.get("offset", 10))
    holders = AnaliticService.get_top_holders(offset)
    return jsonify(holders)


@app.get("/top_with_transactions")
def get_top_with_transactions():
    offset = int(request.args.get("offset", 10))
    data = AnaliticService.get_top_with_transactions(offset)
    return jsonify(data)
