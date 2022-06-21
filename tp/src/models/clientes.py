
class Clientes():
    def __init__(self, nombre_completo, edad, dni):
        self.nombre_completo = nombre_completo
        self.edad = edad
        self.dni = dni

    def serialize(self):
        return {
            'nombre_completo': self.nombre_completo,
            'edad': self.edad,
            "dni": self.dni
                    }

    def reserva(self):
        return f"\n\tNombre del huesped: {self.nombre_completo}" \
               f"\n\tEdad del huesped: {self.edad}" \
               f"\n\tDNI: {self.dni}"

