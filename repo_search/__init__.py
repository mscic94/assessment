import os

from flask import Flask


def app():
    flask_app = Flask(__name__)

    # set config
    app_settings = os.getenv("APP_SETTINGS")
    flask_app.config.from_object(app_settings)

    # register app blueprints
    from repo_search.search_api.router import search_repo_bp

    flask_app.register_blueprint(
        search_repo_bp, url_prefix=flask_app.config.get("BASE_URL")
    )

    return flask_app
