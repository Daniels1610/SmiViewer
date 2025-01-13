from flask import (render_template, request, flash, redirect, url_for, jsonify)
from base64 import b64encode
from io import BytesIO

from app.main import bp
from app.models.Molecule import Molecule


@bp.route('/')
def init():
    return redirect(url_for('main.index'))

@bp.route('/chemical', methods=('GET', 'POST'))
def index():
    status_code = 200
    if (request.method == 'POST'):
        data = request.get_json()
        mol = Molecule(data['smiles'], data['monomer'])

        if (mol.isValid() and len(data['monomer']) > 0):
            image_io = BytesIO()
            mol.diagram.save(image_io, 'png')
            mol.set_diagram('data:image/png;base64,' + b64encode(image_io.getvalue()).decode('ascii'))
            return jsonify(mol.to_dict())
        else:
            status_code = 400
        
    return render_template("index.html"), status_code
