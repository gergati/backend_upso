class Factura():
    def __init__(self, row):
        self._factura_id = row[0]
        self._usuario_id = row[1]
        self._cliente_id = row[2]
        self._fecha = row[3]
        self._total = row[4]

    def to_json(self):
        return {
            "id": self._factura_id,
            "id del usuario": self._usuario_id,
            "id del cliente": self._cliente_id,
            "fecha": self._fecha,
            "total": self._total
        }