class Servicio():
    def __init__(self, row):
        self._servicio_id = row[0]
        self._usuario_id = row[1]
        self._nombre = row[2]

    def to_json(self):
        return {
            "id": self._servicio_id,
            "nombre": self._nombre
        }