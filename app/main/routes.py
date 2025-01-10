from flask import (render_template, request, flash, redirect)
from base64 import b64encode
from io import BytesIO

from app.main import bp
from app.models.Molecule import Molecule


@bp.route('/')
@bp.route('/chemical', methods=('GET', 'POST'))
def index():
    if (request.method == 'POST'):
        smile = request.form['smile']
        name = request.form['monomer']
        status_code = 200

        mol = Molecule(smile, name)

        if (mol.isValid()):
            image_io = BytesIO()
            mol.diagram.save(image_io, 'png')
            mol.set_diagram('data:image/png;base64,' + b64encode(image_io.getvalue()).decode('ascii'))
            return render_template("results.html", mol=mol.to_dict()), status_code
        else:
            status_code = 400
            flash("Invalid input. Enter your SMILES again")
            return render_template('index.html'), status_code 
        

    
    return render_template('index.html')
