
class Recreaciones():
    def __init__(self, nombre, horario, precio, disponibilidad):
       self.nombre = nombre
       self.horario = horario
       self.precio = precio
       self.disponibilidad = disponibilidad

    def __str__(self):
        return f"\n\tRecreación: {self.nombre}" \
               f"\n\tHorario: {self.horario}" \
               f"\n\tPrecio: {self.precio}" \
               f"\n\tDisponibilidad: {self.disponibilidad}"

    def serialize(self):
        return {
           'nombre': self.nombre,
           'horario': self.horario,
           'precio': self.precio,
           'disponibilidad': self.disponibilidad
        }


class Spa(Recreaciones):
    def __init__(self, nombre, horario, precio, disponibilidad):
        super().__init__(nombre, horario, precio, disponibilidad)


class Restaurante(Recreaciones):
    def __init__(self, nombre, horario, precio, disponibilidad):
        super().__init__(nombre, horario, precio, disponibilidad)


class Pileta(Recreaciones):
    def __init__(self, nombre, horario, precio, disponibilidad):
        super().__init__(nombre, horario, precio, disponibilidad)
        self.__precio = "Gratis"


class Tenis(Recreaciones):
    def __init__(self, nombre, horario, precio, disponibilidad):
        super().__init__(nombre, horario, precio, disponibilidad)





