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

Before getting to the final step, you will a `.env` file in the project's directory, so you are able to loadthe environment variables for the project such as the `SECRET_KEY` variable. Reach out to dagraz16@gmail.com so I can share that file with you.
    
Finally, run the flask application:
```bash
flask run
```
<br>

Now, you should be able to visit [SmiViewer](http://127.0.0.1:5000) on your localhost!
