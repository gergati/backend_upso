class Usuario():
    def __init__(self, row):
        self._usuario_id = row[0]
        self._nombre = row[1]
        self._apellido = row[2]
        self._dni = row[3]
        self._email = row[4]
        self._telefono = row[5]
        self._contraseña = row[6]
        self._tipo = row[7]  #Empresa o persona

    def to_json(self):
        return {
            "id": self._usuario_id,
            "nombre": self._nombre,
            "apellido": self._apellido,
            "dni": self._dni,
            "email": self._email,
            "telefono": self._telefono,
            "contraseña": self._contraseña,
            "tipo": self._tipo
        }