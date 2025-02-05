from flask import Flask

from rdkit import RDLogger
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    RDLogger.DisableLog('rdApp.*')
        
    return app

