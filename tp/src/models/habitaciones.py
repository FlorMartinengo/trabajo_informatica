class Habitaciones:
    def __init__(self, tipo, cantidad_de_huespedes, precio):
        self.tipo = tipo
        self.cantidad_de_huespedes = cantidad_de_huespedes
        self.precio = precio

    def __str__(self) -> str:
        return f"\n\tTipo de la habitación: {self.tipo}" \
               f"\n\tCantidad de huéspedes: {self.cantidad_de_huespedes}" \
               f"\n\tPrecio: {self.precio}"

    def tipo_habitacion(self):
        return self.tipo

    def serialize(self):
        return {
            'tipo': self.tipo,
            'cantidad_de_huespedes': self.cantidad_de_huespedes,
            "precio": self.precio,
                                }


class Simple(Habitaciones):
    def __init__(self, tipo, cantidad_de_huespedes, precio):
        super().__init__(tipo, cantidad_de_huespedes, precio)


class Doble(Habitaciones):
    def __init__(self, tipo, cantidad_de_huespedes, precio):
        super().__init__(tipo, cantidad_de_huespedes, precio)


class Cuadruple(Habitaciones):
    def __init__(self, tipo, cantidad_de_huespedes, precio):
        super().__init__(tipo, cantidad_de_huespedes, precio)


class Suite(Habitaciones):
    def __init__(self, tipo, cantidad_de_huespedes, precio, jacuzzi):
        super().__init__(tipo, cantidad_de_huespedes, precio)
        self.jacuzzi = jacuzzi

    def __str__(self) -> str:
        return f"\n\tTipo de la habitación: {self.tipo}" \
               f"\n\tCantidad de huéspedes: {self.cantidad_de_huespedes}" \
               f"\n\tPrecio: {self.precio}" \
               f"\n\tJacuzzi: {self.jacuzzi}"


class Premium(Habitaciones):
    def __init__(self, tipo, cantidad_de_huespedes, precio, jacuzzi, sauna):
        super().__init__(tipo, cantidad_de_huespedes, precio)
        self.jacuzzi = jacuzzi
        self.sauna = sauna

    def __str__(self) -> str:
        return f"\n\tTipo de la habitación: {self.tipo}" \
               f"\n\tCantidad de huéspedes: {self.cantidad_de_huespedes}" \
               f"\n\tPrecio: {self.precio}" \
               f"\n\tJacuzzi: {self.jacuzzi}" \
               f"\n\tSauna: {self.sauna}"







