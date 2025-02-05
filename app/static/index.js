// SmiViewer Form
const monomerInput = document.getElementById('monomer_input');
const smilesInput = document.getElementById('smiles_input');
const submitButton = document.getElementById('submit_btn');

// BadRequestError elements
const badRequestDiv = document.createElement("div");
const badRequestSpan = document.createElement("span");
const badRequestText = "⚠️ Invalid input. The SMILES or Monomer Name is incorrect.";
badRequestDiv.appendChild(badRequestSpan);

// MoleculeResults elements
const molResults = document.querySelector(".mol-results");
const molName = document.querySelector(".mol-name");
const molImage = document.createElement("img");


/** INPUT FORM RESTRICTIONS */

// Prevent Copy-Pase on Monomer Name field
monomerInput.onpaste = e => e.preventDefault();

// Allows only alphanumeric values on monomer name field
monomerInput.addEventListener('beforeinput', (e) => {
    const nextVal =
        e.target.value.substring(0, e.target.selectionStart) +
        (e.data ?? '') +
        e.target.value.substring(e.target.selectionEnd);
        if(!/^[a-zA-Z0-9]+$/gi.test(nextVal)) {
            e.preventDefault();
        }
        return;
});

// Remove flash message about Invalid Smiles after 3 seconds
const removeFlash = () => {
    setTimeout(() => {
        badRequestDiv.remove();
    }, 3000)
}


/** ASYNCHRONOUS LOADING */  

// When user submits form, sends a POST request to the Flask server with values
submitButton.addEventListener('click', (e) => {
    e.preventDefault();
    chemicalPOST();
});

async function chemicalPOST () {
    options = {
        method: "POST",
        body: JSON.stringify({monomer: monomerInput.value, smiles: smilesInput.value}),
        headers: {'Content-Type' : 'application/json'}
    }

    try {
        const response = await fetch("/chemical", options)

        if (response.status == 400) {
            badRequestSpan.innerHTML = badRequestText;
            badRequestDiv.classList.add("flash", "alert","alert-warning");
            document.getElementById("smiles_field").after(badRequestDiv);
            removeFlash();
        }

        const data = await response.json();

        // Set Molecule properties
        let molInfo = [data.name,  
            `<b>Molecule Weight:</b> ${data.weight}`, 
            `<b>Molecule Group:</b> ${data.group}`];

        let molResultsChildren = molResults.children;
        for (i = 0; i < molResultsChildren.length-1; i++) {
                molResultsChildren[i].innerHTML = molInfo[i];
            }
        
        // Set Image attributes
        molImage.src = data.diagram;
        molImage.classList.add("mol-image")
        molName.after(molImage);
        
    }
    catch(error) {
        console.error(error);
    }
}