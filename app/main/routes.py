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
        name = request.form['monomer']
        smile = request.form['smiles']

        mol = Molecule(smile, name)

        if (mol.isValid()):
            image_io = BytesIO()
            mol.diagram.save(image_io, 'png')
            mol.set_diagram('data:image/png;base64,' + b64encode(image_io.getvalue()).decode('ascii'))
            return render_template("results.html", mol=mol.to_dict()), 200
        else:
            flash("Invalid input. Enter your SMILES again")
            status_code = 400
        
    return render_template("index.html"), status_code
