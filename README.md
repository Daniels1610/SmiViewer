# SmiViewer 🧪

**SmiViewer** is a Flask Web Application that takes a chemical structure by their SMILES (Simplified Molecular Input Line Entry System)
notation an extracts the molecule properties such as the molecular weight, functional group and a 2D representation of the compound.<br>  
![Smiviewer](app/static/smiviewer-demo.png?raw=true "Smiviewer Home Page")

### Getting Started
To obtain the project's content,  use _git clone_ command (verify that you have `git` installed):  
```bash
git clone https://github.com/Daniels1610/SmiViewer.git
```
Or use the option "Download ZIP" on the repository's green button labeled as "code".<br><br>
  
  
After you cloned this repository, open the project in your preferred IDE and execute this command on your terminal:
```bash
python -m venv venv
```
  
This will create a python virtual environment where you would be able to install all the required depedencies for the project.<br><br>
  
    
To activate the virtual environment:    
- **Linux/MacOS:**
```bash
source venv/bin/activate
```

- **Windows:**
```bash
venv\Scripts\activate
```
<br>
    
To install the project dependencies.
```bash
pip install -r requirements.txt
```
<br>

Before getting to the final step, you will need to put a `.env` file in the project's directory, so you are able to load the environment variables for the project such as the `SECRET_KEY` variable. Send a message to dagraz16@gmail.com so I can share that file with you.
    
Finally, run the flask application:
```bash
flask run
```
<br>

Now, you should be able to visit [SmiViewer](http://127.0.0.1:5000) on your localhost! <br>

### Quickstart
Smiviewer works by entering:
- Monomer Name: A name of your choice, that will make reference to your Monomer
- SMILES: Chemical structure that follows SMILES [notation](https://chem-libretexts-org.translate.goog/Courses/Fordham_University/Chem1102%3A_Drug_Discovery_-_From_the_Laboratory_to_the_Clinic/05%3A_Organic_Molecules/5.08%3A_Line_Notation_(SMILES_and_InChI)?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=wa).

To get you started you can try any of the following SMILES:
- CC(CC(=O)OCC(COC(=O)CC(C)S)(COC(=O)CC(C)S)COC(=O)CC(C)S)S
- C=CCN1C(=O)N(C(=O)N(C1=O)CC=C)CC=C
- CC(S)CC(=O)OCCN1C(=O)N(CCOC(=O)CC(C)S)C(=O)N(CCOC(=O)CC(C)S)C1=O
- C=CC(=O)OCCCOCCCOCCCOC(=O)C=C
- C=CC(=O)OC(=O)NCCCCCn1c(==O)n(CCCCCNC(O)OCCOC(=O)C-C)c(=O)n(CCCCCCNC(=OOCCOC(=O)C=C)c1 (This is one is Invalid 👀)

![Smiviewer](app/static/smiviewer-formfilled.png?raw=true "Smiviewer with Form Filled")

Then click on Submit to discover the fantastic structure and some properties of your Monomer!
![Smiviewer](app/static/smiviewer-results.png?raw=true "Smiviewer Results Display")
