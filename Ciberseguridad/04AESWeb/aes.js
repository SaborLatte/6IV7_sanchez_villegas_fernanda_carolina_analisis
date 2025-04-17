function showEncrypt() {
    document.getElementById('encrypt-section').classList.remove('hidden');
    document.getElementById('decrypt-section').classList.add('hidden');
}

function showDecrypt() {
    document.getElementById('decrypt-section').classList.remove('hidden');
    document.getElementById('encrypt-section').classList.add('hidden');
}

function cifrarMensaje() {
    const mensaje = document.getElementById('mensaje').value;
    const clave = document.getElementById('clave-encriptar').value;

    if (clave.length < 8) {
        alert("La clave debe tener al menos 8 caracteres.");
        return;
    }

    const cifrado = CryptoJS.AES.encrypt(mensaje, clave).toString();
    const blob = new Blob([cifrado], { type: 'text/plain' });
    const enlace = document.createElement('a');
    enlace.href = URL.createObjectURL(blob);
    enlace.download = 'mensaje_cifrado.txt';
    enlace.click();
}

function descifrarArchivo() {
    const archivo = document.getElementById('archivo-cifrado').files[0];
    const clave = document.getElementById('clave-descifrar').value;

    if (!archivo || clave.length < 8) {
        alert("Debes seleccionar un archivo y una clave válida (mín. 8 caracteres).");
        return;
    }

    const lector = new FileReader();
    lector.onload = function (e) {
        const contenido = e.target.result;
        try {
            const bytes = CryptoJS.AES.decrypt(contenido, clave);
            const texto = bytes.toString(CryptoJS.enc.Utf8);

            if (!texto) throw new Error("Clave incorrecta o archivo dañado.");

            document.getElementById('mensaje-descifrado').value = texto;
        } catch (err) {
            alert("No se pudo descifrar el mensaje: " + err.message);
        }
    };
    lector.readAsText(archivo);
}
