from flask import (Blueprint, render_template, request, redirect, url_for, jsonify, flash)
from flask.views import MethodView

from base64 import b64encode
from io import BytesIO

from app.models.Molecule import Molecule

main = Blueprint(
    'main', __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='main/static',
    url_prefix='/main'
)

class Root(MethodView):
    def get(self):
        return redirect(url_for('main.index'))

class HomePage(MethodView):
    def get(self):
        render_template("index.html"), 200

    def post(self):
        data = request.get_json()
        mol = Molecule(data['smiles'], data['monomer'])

        if (mol.isValid() and data.get('monomer')):
            image_io = BytesIO()
            mol.diagram.save(image_io, 'png')
            mol.set_diagram('data:image/png;base64,' + b64encode(image_io.getvalue()).decode('ascii'))
            return jsonify(mol.to_dict())
        else:
            flash("Invalid input. Please check your Monomer Name or SMILES")
            render_template("index.html"), 400

main.add_url_rule('/', view_func=Root.as_view("root"))
main.add_url_rule('/chemical', view_func=HomePage.as_view("homepage"))