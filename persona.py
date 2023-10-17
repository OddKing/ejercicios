class Persona:
    nombre="carlos"
    edad=None

def __init__(self,nombre=None,edad=None):
    self.nombre=nombre
    self.edad=edad


p=Persona()

print("el nombre de la persona es: ",getattr(p,"nombre"))
print("la edad de la persona es: ",getattr(p,"edad"))
setattr(p,"edad",30)
print("la edad de la persona es: ",getattr(p,"edad"))
print(hasattr(p,"apellido"))