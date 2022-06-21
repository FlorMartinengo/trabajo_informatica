import random


def generador_nro_reserva():
    return str(random.randint(1000000, 9000000))


class Reserva():
    def __init__(self, numero_reserva, tipo_habitacion, cantidad_huespedes, fecha_entreda, fecha_salida):
        self.numero_reserva = numero_reserva
        self.tipo_habitacion = tipo_habitacion
        self.cantidad_huespedes = cantidad_huespedes
        self.fecha_entrada = fecha_entreda
        self.fecha_salida = fecha_salida

    def __str__(self):
        return f"\n\tNúmero de reserva: {self.numero_reserva}" \
               f"\n\tTipo de habitación: {self.tipo_habitacion}" \
               f"\n\tCantidad de huéspedes: {self.cantidad_huespedes}" \
               f"\n\t Fecha de de ingreso: {self.fecha_entrada}" \
               f"\n\tFecha de salida: {self.fecha_salida}"

    def serialize(self):
        return {
            "numero_reserva": self.numero_reserva,
            "tipo_habitación": self.tipo_habitacion,
            "cantidad_huespedes": self.cantidad_huespedes,
            "fecha_entrada": self.fecha_entrada,
            "fecha_salida": self.fecha_salida
            }

