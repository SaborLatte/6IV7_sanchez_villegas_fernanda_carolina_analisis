document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("registroForm");

  form.addEventListener("submit", function (e) {
    e.preventDefault();

    const soloLetras = /^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$/;
    const nombre = document.getElementById("nombre").value.trim();
    const segundoNombre = document.getElementById("segundoNombre").value.trim();
    const apellidoPaterno = document.getElementById("apellidoPaterno").value.trim();
    const apellidoMaterno = document.getElementById("apellidoMaterno").value.trim();
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirmPassword").value;

    if (!soloLetras.test(nombre) || !soloLetras.test(segundoNombre) ||
        !soloLetras.test(apellidoPaterno) || !soloLetras.test(apellidoMaterno)) {
      alert("Los campos de nombre y apellidos solo deben contener letras.");
      return;
    }

    if (password !== confirmPassword) {
      alert("Las contraseñas no coinciden.");
      return;
    }

    alert("¡Registro exitoso!");
    form.reset(); // Limpiar el formulario después del éxito
  });
});
