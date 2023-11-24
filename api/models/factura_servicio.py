class FacturaProducto():
    def __init__(self, row):
        self._factura_id = row[0]
        self._servicio_id = row[1]
        self._cantidad = row[2]

    def to_json(self):
        return {
            "id de la factura": self._factura_id,
            "id del servicio": self._servicio_id,
            "cantidad": self._cantidad
        }