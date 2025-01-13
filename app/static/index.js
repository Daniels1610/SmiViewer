const monomerInput = document.getElementById('monomer_input');
const smilesInput = document.getElementById('smiles_input');
const flashAlert = document.querySelector('.flash');
const submitButton = document.getElementById('submit_btn');
const molResults = document.querySelector('.mol-results');

/// INPUT FORM RESTRICTIONS ///

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
        flashAlert.style.display = "none";
    }, 3000)
}

/// ASYNCHRONOUS LOADING ///

// When user submits form, sends a POST request to the Flask server with values
submitButton.addEventListener('click', (e) => {
    e.preventDefault();
    chemicalPOST();
});

async function chemicalPOST () {
    options = {
        method: "POST",
        body: JSON.stringify({monomer: monomerInput.value, smiles: smilesInput.value}),
        headers: {
            'Content-Type' : 'application/json'
        }
    }

    try {
        const response = await fetch("/chemical", options)

        if (response.status == 400) {
            flashAlert.style.display = "block";
            removeFlash();
        }

        const data = await response.json();

        // Set Molecule properties
        let molInfo = [data.name, 
            data.diagram, 
            `<b>Molecule Weight:</b> ${data.weight}`, 
            `<b>Molecule Group:</b> ${data.group}`];

        let molResultsChildren = molResults.children;
        for (i = 0; i < molResultsChildren.length; i++) {
            if (molResultsChildren[i].className === "mol-image") {
                molResultsChildren[i].src = molInfo[i];
            } else {
                molResultsChildren[i].innerHTML = molInfo[i];
            }
            
            molResultsChildren[i].style.display = "block"
        }
    }
    catch(error) {
        console.error(error);
    }
}