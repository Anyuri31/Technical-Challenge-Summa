import pytest
from utils.api_client import BookerAPI

@pytest.fixture
def api_client():
    """Fixture que devuelve un cliente con token válido listo para usar."""
    client = BookerAPI()
    token = client.get_token()
    print(f"Token generado para pruebas: {token}")
    return client

def test_booking_lifecycle(api_client):
    # Crear reserva
    payload_create = {
        "firstname": "Anyuri",
        "lastname": "Leon",
        "totalprice": 10000,
        "depositpaid": True,
        "bookingdates": {"checkin": "2026-02-01", "checkout": "2026-02-10"},
        "additionalneeds": "Snacks"
    }
    booking = api_client.create_booking(payload_create)
    booking_id = booking["bookingid"]

    # Validación
    booking_data = api_client.get_booking(booking_id)
    assert booking_data["firstname"] == "Anyuri"
    assert booking_data["totalprice"] == 10000

    # Actualizar reserva
    payload_update = {
        "firstname": "Anyuri",
        "lastname": "Gutierrez",
        "totalprice": 2000,
        "depositpaid": False,
        "bookingdates": {"checkin": "2026-03-01", "checkout": "2026-03-15"},
        "additionalneeds": "Snacks + gift"
    }
    updated_booking = api_client.update_booking(booking_id, payload_update)

    # Validación de cambios
    assert updated_booking["lastname"] == "Gutierrez"
    assert updated_booking["totalprice"] == 2000
    assert updated_booking["depositpaid"] is False

    # Intentar borrar con token inválido
    response_invalid = api_client.delete_booking(booking_id, token="TOKEN_INVALIDO")
    assert response_invalid.status_code in [401, 403]  # Esperamos rechazo
