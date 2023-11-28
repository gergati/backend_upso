class Producto():
    def __init__(self, row):
        self._producto_id = row[0]
        self._usuario_id = row[1]
        self._nombreProd = row[2]
        self._marca = row[3]
        self._precio = row[4]
        self._cantidad = row[5]
        self._descripcion = row[6]

    def to_json(self):
        return {
            "id": self._producto_id,
            "nombre del producto": self._nombreProd,
            "marca": self._marca,
            "precio": self._precio,
            "cantidad": self._cantidad,
            "descripcion del producto": self._descripcion 
        }