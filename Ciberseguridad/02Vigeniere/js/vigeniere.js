var vigenere = vigenere || (function(){ 

    // Función que maneja el cifrado y descifrado
    var proceso = function(txt, desp, action){
        var replace = (function(){
            // Abecedario con la ñ incluida
            var abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
            var longitud = abc.length;

            return function(c){
                var i = abc.indexOf(c.toLowerCase());
                if(i != -1){
                    var pos = i;
                    if(action){
                        // Cifrar
                        pos = (pos + desp) % longitud;
                    }else{
                        // Descifrar
                        pos = (pos - desp + longitud) % longitud;
                    }
                    return abc[pos];
                }
                return c;
            };
        })();

        // Validación de caracteres
        var re = (/([a-z])/ig);
        return String(txt).replace(re,function(match){
            return replace(match);
        });
    };

    return{
        encode : function(txt, desp){
            return proceso(txt, desp, true);
        },
        decode : function(txt, desp){
            return proceso(txt, desp, false);
        }
    };
})();

// Validar que los campos no estén vacíos
function validarEntrada(texto, clave) {
    if (texto.trim() === "" || clave.trim() === "") {
        alert("El texto y la clave no pueden estar vacíos.");
        return false;
    }
    return true;
}

// Ajustar la clave para que tenga la misma longitud que el texto
function ajustarClave(texto, clave) {
    while (clave.length < texto.length) {
        clave += clave;
    }
    return clave.slice(0, texto.length);
}

// Cifrar
function codificar(texto, clave){
    if (!validarEntrada(texto, clave)) return;
    clave = ajustarClave(texto, clave);
    var resultado = "";
    var indiceclave = 0;
    var charartexto = texto.split('');

    for(var i = 0; i < charartexto.length; i++){
        var desp = obindiceClave(clave.charAt(indiceclave));
        var chartexto = charartexto[i];

        resultado += vigenere.encode(chartexto, (desp >= 26) ? desp % 26 : desp);
        indiceclave++;

        if(indiceclave >= clave.length){
            indiceclave = 0;
        }
    }
    document.getElementById("resultado").value = resultado;
    return resultado;
}

// Obtener el índice de la clave en el abecedario
function obindiceClave(reco){
    var abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
    return abc.indexOf(reco.toLowerCase());
}

// Descifrar
function decodificar(texto, clave){
    if (!validarEntrada(texto, clave)) return;
    clave = ajustarClave(texto, clave);
    var resultado = "";
    var indiceclave = 0;
    var charartexto = texto.split('');

    for(var i = 0; i < charartexto.length; i++){
        var desp = obindiceClave(clave.charAt(indiceclave));
        var chartexto = charartexto[i];

        resultado += vigenere.decode(chartexto, (desp >= 26) ? desp % 26 : desp);
        indiceclave++;

        if(indiceclave >= clave.length){
            indiceclave = 0;
        }
    }
    document.getElementById("resultado").value = resultado;
    return resultado;
}

// Reiniciar los campos
function reiniciar(){
    document.getElementById("texto").value = "";
    document.getElementById("clave").value = "";
    document.getElementById("resultado").value = "";
}

// Copiar el texto del resultado al portapapeles
function copiarTexto() {
    var respuesta = document.getElementById("resultado");
    if (respuesta.value.trim() === "") {
        alert("No hay texto para copiar.");
        return;
    }
    respuesta.select();
    document.execCommand("copy");
    alert("Texto copiado al portapapeles");
}
