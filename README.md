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