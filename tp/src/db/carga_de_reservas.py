import json
from models.reservas import Reserva


def cargar_reservas():
    reservas = []

    with open('db/reservas_mock.json', 'r') as file:
        reservas_json = json.load(file)
        for reserva in reservas_json:
            reservas.append(
                Reserva(
                    reserva['numero_reserva'],
                    reserva['tipo_habitacion'],
                    reserva['cantidad_huespedes'],
                    reserva['fecha_entrada'],
                    reserva['fecha_salida']
                )
            )
    return reservas

