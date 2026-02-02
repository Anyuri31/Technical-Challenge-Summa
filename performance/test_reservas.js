const axios = require('axios');

const URL = 'https://restful-booker.herokuapp.com/booking';
const NUM_USUARIOS = 20;
const MAX_RESPUESTA_MS = 800;

async function medirCarga() {
    const tiempos = [];

    const requests = Array.from({ length: NUM_USUARIOS }, async (_, i) => {
        const inicio = Date.now();
        try {
            await axios.get(URL);
            const fin = Date.now();
            const duracion = fin - inicio;
            tiempos.push(duracion);
            console.log(`Usuario ${i + 1}: ${duracion} ms`);
        } catch (error) {
            console.log(`Usuario ${i + 1}: ERROR`, error.message);
        }
    });

    await Promise.all(requests);

    const maxTiempo = Math.max(...tiempos);
    const promedio = tiempos.reduce((a, b) => a + b, 0) / tiempos.length;
    console.log(`\nTiempo máximo: ${maxTiempo} ms`);
    console.log(`Tiempo promedio: ${promedio.toFixed(2)} ms`);

    if (maxTiempo <= MAX_RESPUESTA_MS) {
        console.log("El endpoint soporta 20 usuarios concurrentes dentro de 800ms");
    } else {
        console.log("El endpoint NO cumple con el objetivo de rendimiento");
    }
}

// Ejecutar prueba
medirCarga();
