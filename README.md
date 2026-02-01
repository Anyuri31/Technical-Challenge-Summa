PRUEBA TECNICA: Automatización Frontend – Protección del Ingreso

Este proyecto automatiza el flujo de compra del monitor más costoso en la tienda https://www.demoblaze.com/, garantizando que un usuario pueda encontrar, añadir al carrito y completar la compra, manejando asincronía, modales y alertas del navegador.

Cómo ejecutar el proyecto:

1. Clonar el repositorio
2. Crear y activar un entorno virtual
3. Instalar dependencias con pip install -r requirements.txt
4. Ejecutar las pruebas con pytest

Decisiones de diseño:

1. Se utilizó Page Object Model (POM) para separar la lógica de los tests de la interacción con la UI y facilitar el mantenimiento.
2. Se implementaron esperas explícitas (WebDriverWait) para manejar la asincronía de la aplicación.
3. El monitor más costoso se identifica dinámicamente, sin datos hardcodeados.
4. Se manejan alertas nativas del navegador al agregar productos al carrito.
5. El flujo de compra se automatiza completamente, incluyendo el llenado del formulario y la validación del mensaje de éxito.
6. Se incluye manejo de DOM dinámico para evitar fallos por StaleElementReferenceException.
