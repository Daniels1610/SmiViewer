const monomerInput = document.getElementById('monomer_input');
const smilesInput = document.getElementById('smiles_input');
const flashAlert = document.querySelector('.flash');

// Prevent Copy-Pase on Monomer Name field
window.onload = (e) => {
    monomerInput.onpaste = e => e.preventDefault();
    removeFlash();
}

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

const removeFlash = () => {
    setTimeout(() => {
        flashAlert.remove();
    }, 3000)
}


