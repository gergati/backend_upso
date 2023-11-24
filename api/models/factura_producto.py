class FacturaProducto():
    def __init__(self, row):
        self._factura_id = row[0]
        self._producto_id = row[1]
        self._cantidad = row[2]
    
    def to_json(self):
        return {
            "id": self._factura_id,
            "id del producto": self._producto_id,
            "cantidad": self._cantidad
        }