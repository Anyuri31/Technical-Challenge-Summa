import requests

class BookerAPI:
    BASE_URL = "https://restful-booker.herokuapp.com"

    def __init__(self):
        self.token = None

    def get_token(self):
        """Genera un token de acceso válido para operaciones que requieren autenticación."""
        url = f"{self.BASE_URL}/auth"
        payload = {"username": "admin", "password": "password123"}
        response = requests.post(url, json=payload)
        response.raise_for_status()
        self.token = response.json().get("token")
        return self.token

    def create_booking(self, payload):
        """Crea una nueva reserva en el sistema."""
        url = f"{self.BASE_URL}/booking"
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()

    def get_booking(self, booking_id):
        """Obtiene los datos de una reserva específica."""
        url = f"{self.BASE_URL}/booking/{booking_id}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def update_booking(self, booking_id, payload, token=None):
        """Actualiza una reserva existente usando token válido."""
        if token is None:
            if not self.token:
                raise ValueError("Token no generado. Llama primero a get_token()")
            token = self.token
        headers = {"Content-Type": "application/json", "Cookie": f"token={token}"}
        url = f"{self.BASE_URL}/booking/{booking_id}"
        response = requests.put(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()

    def delete_booking(self, booking_id, token=None):
        """Intenta borrar una reserva. Si el token es inválido, la API devuelve 401/403."""
        if token is None:
            if not self.token:
                raise ValueError("Token no generado. Llama primero a get_token()")
            token = self.token
        headers = {"Cookie": f"token={token}"}
        url = f"{self.BASE_URL}/booking/{booking_id}"
        response = requests.delete(url, headers=headers)
        return response
