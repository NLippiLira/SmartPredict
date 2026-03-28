const form = document.getElementById("form");
const resultado = document.getElementById("resultado");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const edad = document.getElementById("edad").value;
    const ingresos = document.getElementById("ingresos").value;
    const score = document.getElementById("score").value;

    const data = {
        edad: Number(edad),
        ingresos: Number(ingresos),
        score: Number(score)
    };

    try {
        const response = await fetch("https://smartpredict-sn4v.onrender.com/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (result.prediccion === 1) {
            resultado.innerHTML = "✅ Crédito Aprobado";
            resultado.style.color = "green";
        } else {
            resultado.innerHTML = "❌ Crédito Rechazado";
            resultado.style.color = "red";
        }

    } catch (error) {
        resultado.innerHTML = "Error al conectar con la API";
        resultado.style.color = "orange";
    }
});