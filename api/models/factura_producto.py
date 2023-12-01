class FacturaProducto():
    def __init__(self, row):
        self._facturaProd_id = row[0]
        self._producto_id = row[1]
        self._usuario_id = row[2]
    
    def to_json(self):
        return {
            "id": self._facturaProd_id,
            "id del producto": self._producto_id,
            "cantidad": self._usuario_id
        }