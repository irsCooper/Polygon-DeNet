from flask import Blueprint, request, jsonify
from blockchain.polygon.erc20_contract import ERC20Contract
from src.core.config import erc20, w3, settings

app = Blueprint("erc20", __name__)


@app.get("/balance")
def get_balance():
    address = request.args.get("address")
    if not address:
        return jsonify({"error": "address required"}), 400

    balance = erc20.get_balance(address)
    return jsonify({"balance": balance})


@app.post("/balance_batch")
def get_balance_batch():
    payload = request.json or {}
    addresses = payload.get("addresses")

    if not addresses:
        return jsonify({"error": "addresses required"}), 400

    balances = erc20.get_balance_batch(addresses)
    return jsonify({"balances": balances})

@app.get("/token_info")
def get_token_info():
    contract_address = request.args.get("address")
    if not contract_address:
        return jsonify({"error": "contract address required"}), 400

    erc20 = ERC20Contract(
        w3_client=w3,
        contract_address=contract_address,
        abi_path=settings.polygon_config.abi_erc20_path,
        default_sender=settings.polygon_config.sender_address
    )
    info = erc20.get_token_info()
    return jsonify(info)


@app.get("/call_contract")
def call_contract():
    """
    Универсальный вызов метода контракта.
    GET body:
    {
        "address": "0xContractAddress",
        "method": "decimals",
        "args": [arg1, arg2, ...]  # опционально
    }
    """
    payload = request.json or {}
    contract_address = payload.get("address")
    method_name = payload.get("method")
    args = payload.get("args", [])

    if not contract_address or not method_name:
        return jsonify({"error": "address and method are required"}), 400

    try:
        erc20 = ERC20Contract(
            w3_client=w3,
            contract_address=contract_address,
            abi_path=settings.polygon_config.abi_erc20_path,
            default_sender=settings.polygon_config.sender_address
        )
        result = erc20.call(method_name, args)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.post("/send_transaction")
def send_transaction():
    """
    Универсальный вызов транзакции в контракте.
    POST body:
    {
        "address": "0xContractAddress",
        "method": "decimals",
        "args": [arg1, arg2, ...]  # опционально
    }
    """
    payload = request.json or {}
    contract_address = payload.get("address")
    method_name = payload.get("method")
    args = payload.get("args", [])

    if not contract_address or not method_name:
        return jsonify({"error": "address and method are required"}), 400

    try:
        erc20 = ERC20Contract(
            w3_client=w3,
            contract_address=contract_address,
            abi_path=settings.polygon_config.abi_erc20_path,
            default_sender=settings.polygon_config.sender_address
        )
        result = erc20.transact(method_name, args)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500