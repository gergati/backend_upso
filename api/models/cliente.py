from datetime import datetime

class Cliente:
    def __init__(self, row):
        self.cliente_id = row[0]
        self.usuario_id = row[1]
        self.apellido = row[2]
        self.nombre = row[3]
        self.dni = row[4]
        self.email = row[5]
        self.telefono = row[6]
        self.contraseña = row[7]
        self.fechaNac = row[8]

    def to_json(self):
        return {
            "cliente_id": self.cliente_id,
            "usuario_id": self.usuario_id,
            "apellido": self.apellido,
            "nombre": self.nombre,
            "dni": self.dni,
            "email": self.email,
            "telefono": self.telefono,
            "contraseña": self.contraseña,
            "fechaNac": self.fechaNac.strftime('%Y-%m-%d')  # Formatea la fecha como 'YYYY-MM-DD'
        }
