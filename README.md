## Automatización Frontend – Protección del Ingreso

Se automatiza el flujo de compra del monitor más costoso en la tienda https://www.demoblaze.com/, garantizando que un usuario pueda encontrar, añadir al carrito y completar la compra, manejando asincronía, modales y alertas del navegador.

### Cómo ejecutar el proyecto:

1. Clonar el repositorio
2. Crear y activar un entorno virtual
3. Instalar dependencias con pip install -r requirements.txt
4. Ejecutar las pruebas con pytest

### Decisiones de diseño:

1. Se utilizó Page Object Model (POM) para separar la lógica de los tests de la interacción con la UI y facilitar el mantenimiento.
2. Se implementaron esperas explícitas (WebDriverWait) para manejar la asincronía de la aplicación.
3. El monitor más costoso se identifica dinámicamente, sin datos hardcodeados.
4. Se manejan alertas nativas del navegador al agregar productos al carrito.
5. El flujo de compra se automatiza completamente, incluyendo el llenado del formulario y la validación del mensaje de éxito.
6. Se implementa manejo de DOM dinámico mediante reintentos controlados para mitigar errores StaleElementReferenceException provocados por el re-renderizado del sitio

---
## Automatización Backend – Ciclo de Vida de Reservas
Se automatiza la validación del flujo completo de reservas usando la API **Restful-Booker** (https://restful-booker.herokuapp.com/) con el objetivo de asegurar la integridad y seguridad de las reservas.

1. Crear una nueva reserva.
2. Validar que los datos fueron guardados correctamente.
3. Actualizar la reserva y verificar que los cambios persisten.
4. Intentar borrar la reserva con un token inválido y validar que la API lo rechaza.

### Estructura

- `utils/api_client.py` → Cliente modular para manejar requests a la API.
- `tests/test_booking_lifecycle.py` → Test principal que ejecuta el flujo completo.

### Cómo ejecutar los tests
Desde la carpeta raíz del backend:
python -m pytest tests/test_booking_lifecycle.py -v -s

### Decisiones de diseño

1. Se implementó un cliente API (BookerAPI) para centralizar requests y manejo de token.
2. Se usa pytest con fixtures para generar el token antes de ejecutar los tests.
3. Se manejan respuestas de la API con raise_for_status() para capturar errores HTTP.
4. Se valida la persistencia de los cambios y la respuesta de seguridad al usar un token inválido.
5. El flujo de prueba es end-to-end, cubriendo creación, actualización y validación de seguridad.

# DevOps & CI/CD (Shift-Left Testing)
Se realiza la ejecución de pruebas UI con Selenium en un entorno limpio, utilizando Docker para el backend y el frontend, y un workflow de CI/CD para integrarlas en un proceso de Integración Continua.

### Como ejecutar los test

# Construir contenedores
docker build -t backend-tests ./backend
docker build -t frontend-app ./frontend

# Levantar contenedores
docker run -d --name backend-container -p 3000:3000 backend-tests
docker run -d --name frontend-container -p 8080:80 frontend-app

# Ejecutar tests Selenium
docker run --rm --network host -v $(pwd)/frontend:/frontend frontend-app \
bash -c "pip install -r /frontend/requirements.txt && python3 -m unittest discover -s /frontend/tests"

# Detener contenedores
docker stop backend-container frontend-container

### Decisiones de diseño
1. Se dockerizó backend y frontend para garantizar entornos limpios y reproducibles.
2. Los tests Selenium se ejecutan en un contenedor temporal con las dependencias necesarias, evitando dependencias de la máquina local.
3. Se implementó un workflow de CI/CD (pipeline.yml) en GitHub Actions para ejecutar los tests automáticamente en cada push o pull request, aplicando Shift-Left Testing.
4. La carpeta frontend se monta en el contenedor para acceder a tests y dependencias de forma sencilla.
5. La estructura separa claramente backend, frontend y tests, facilitando mantenimiento y escalabilidad.

##  Base de Datos y Análisis (SQL)

**Objetivo:** Identificar usuarios "VIP" recientes con compras mayores a $500 USD en los últimos 30 días.

### Explicación
1. Se filtran solo órdenes completadas.
2. Se consideran compras en los últimos 30 días.
3. Se agrupan por usuario para obtener el gasto total.
4. Se muestran los usuarios que superan $500 USD ordenados de mayor a menor gasto.

## Consulta:
SELECT
    u.id AS user_id,
    u.name AS user_name,
    u.email,
    SUM(o.total_amount) AS total_spent
FROM
    Users u
JOIN
    Orders o
    ON u.id = o.user_id
WHERE
    o.status = 'completed'
    AND o.purchase_date >= CURRENT_DATE - INTERVAL 30 DAY
GROUP BY
    u.id, u.name, u.email
HAVING
    SUM(o.total_amount) > 500
ORDER BY
    total_spent DESC;


## Performance
Verificar si el endpoint de reservas soporta 20 usuarios concurrentes con tiempo de respuesta menor a 800 ms, identificando posibles problemas de rendimiento.

### Como ejecutar los test
npm install
node test_reservas.js

Usuario	Tiempo (ms)
3	    915
20	    1113
12	    1117
2	    1126
7	    1326
6	    1396
11	    1676

Conclusión:
El endpoint no cumple con el objetivo de rendimiento (<800ms) bajo 20 usuarios concurrentes, mostrando que hay margen de mejora para soportar carga simultánea.