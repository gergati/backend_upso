class Cliente():
    def __init__(self, row):
        self._cliente_id = row[0]
        self._usuario_id = row[1]
        self._nombre = row[2]
        self._apellido = row[3]
        self._dni = row[4]
        self._email = row[5]
        self._telefono = row[6]
        self._nacimiento = row[7]
        self._contraseña = row[8]

    def to_json(self):
        return {
            "id": self._cliente_id,
            "nombre": self._nombre,
            "apellido": self._apellido,
            "dni": self._dni,
            "email": self._email,
            "telefono": self._telefono,
            "nacimiento": self._nacimiento,
            "contraseña": self._contraseña
        }
