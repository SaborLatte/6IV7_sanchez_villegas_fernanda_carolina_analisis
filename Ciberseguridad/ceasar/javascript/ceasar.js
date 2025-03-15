const desplazamiento = document.getElementById("desplazamiento");
const texto = document.getElementById("texto");
const textoCifrado = document.getElementById("cifrado");
const textoDescifradoInput = document.getElementById("descifrado");
const textoDescifradoOutput = document.getElementById("textoDescifrado");
const btnCifrar = document.createElement("button");
const btnDescifrar = document.createElement("button");

// Asegurar que el script se ejecute cuando el DOM está completamente cargado
document.addEventListener("DOMContentLoaded", function() {
    function cifrado(){
        const textoIngresado = texto.value;
        textoCifrado.value = textoIngresado.split('').map( c => {
            let mayus = (c === c.toUpperCase());
            let valorEntero = c.toLowerCase().charCodeAt(0);
            
            if(valorEntero >= 97 && valorEntero <= 122){
                const valorDesplazamiento = parseInt(desplazamiento.value);
                if(valorEntero + valorDesplazamiento > 122){
                    valorEntero = 97 + (valorEntero - 122 ) + valorDesplazamiento - 1;
                } else {
                    valorEntero = valorEntero + valorDesplazamiento;
                }
            }
            let cifrado = String.fromCharCode(valorEntero);
            return mayus ? cifrado.toUpperCase() : cifrado;
        }).join('');
    }

    function descifrado(){
        const textoIngresado = textoDescifradoInput.value;
        textoDescifradoOutput.value = textoIngresado.split('').map( c => {
            let mayus = (c === c.toUpperCase());
            let valorEntero = c.toLowerCase().charCodeAt(0);
            if(valorEntero >= 97 && valorEntero <= 122){
                const valorDesplazamiento = parseInt(desplazamiento.value);
                if(valorEntero - valorDesplazamiento < 97){
                    valorEntero = 122 - (97 - (valorEntero - valorDesplazamiento)) + 1;
                } else {
                    valorEntero = valorEntero - valorDesplazamiento;
                }
            }
            let descifrado = String.fromCharCode(valorEntero);
            return mayus ? descifrado.toUpperCase() : descifrado;
        }).join('');
    }
    desplazamiento.addEventListener("change", cifrado);

    // Agregar eventos a los botones (si están en el HTML)
    const btnCifrar = document.querySelector(".btn-primary");
    const btnDescifrar = document.querySelector(".btn-secondary");

    if (btnCifrar) btnCifrar.addEventListener("click", cifrado);
    if (btnDescifrar) btnDescifrar.addEventListener("click", descifrado);
});
