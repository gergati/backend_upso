class FacturaServicio():
    def __init__(self, row):
        self._facturaServicio_id = row[0]
        self._servicio_id = row[1]

    def to_json(self):
        return {
            "id de la factura": self._facturaServicio_id,
            "id del servicio": self._servicio_id,
        }