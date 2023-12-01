from datetime import datetime
class Servicio():
    def __init__(self, row):
        self._servicio_id = row[0]
        self._usuario_id = row[1]
        self._nombre = row[2]
        self._fecha = row[3].strftime('%Y-%m-%d')
        self._hora = str(row[4])

    def to_json(self):
        return {
            "id del servicio": self._servicio_id,
            "id del usuario": self._usuario_id,
            "servicio realizado": self._nombre,
            "fecha": self._fecha,
            "hora": self._hora
        }