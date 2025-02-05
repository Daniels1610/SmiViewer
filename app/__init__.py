from flask import Flask

from rdkit import RDLogger
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    RDLogger.DisableLog('rdApp.*')

    from app.blueprints.main.routes import main as main_bp
    app.register_blueprint(main_bp)

    from app.blueprints.ml.routes import ml as ml_bp
    app.register_blueprint(ml_bp)
        
    return app

