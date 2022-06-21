
class Contacto():
   def __init__(self):
       self.mail = "rakotomala@hotel.com"
       self.direccion = "Rue Andriba 232, Antananarivo"
       self.telefono = "+261 367-864"

   def serialize(self):
       return {
                'mail': self.mail,
                'direccion': self.direccion,
                "telefono": self.telefono
            }

