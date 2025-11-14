import os
from flask import Flask
from src.core.config import settings

from src.analytic.router import app as analitic_app
from src.erc20.router import app as erc20_app



def create_app() -> Flask:
    app = Flask(__name__)
    app.secret_key = os.urandom(69).hex()

    app.register_blueprint(analitic_app, url_prefix="/analytics")
    app.register_blueprint(erc20_app, url_prefix="/erc20")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8080)
