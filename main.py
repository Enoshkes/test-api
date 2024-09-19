from flask import Flask

from controllers.user_controller import user_blueprint

def create_app():
    flask_app = Flask(__name__)
    flask_app.register_blueprint(user_blueprint, url_prefix="/api/user")
    return flask_app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
