from flask import Flask
from .main import main_bp

def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']='ec76c39b5935ea247d14b831653d4dbdf147c4e39061b669'

    #register blueprints
    app.register_blueprint(main_bp)

    return app
