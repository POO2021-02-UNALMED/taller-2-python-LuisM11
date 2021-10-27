class Asiento:
    def __init__(self,a,b,c):
        self.color=a
        self.precio=b
        self.registro=c
    def cambiarColor(self,c):
        if c == "rojo" or c== "amarillo" or c== "verde" or c== "negro" or c== "blanco":
            self.color=c
        
class Auto :
    cantidadCreados = 0
    def __init__(self,a,b,c,d,e,f):
        self.modelo=a
        self.precio=b
        self.asientos=c
        self.marca =d 
        self.motor= e
        self.registro = f

    def cantidadAsientos(self):
        c=0
        for i in self.asientos:
            if isinstance(i,Asiento) == True:
                c+=1
        return c

    def verificarIntegridad(self):
        a="Auto original"
        b="Las piezas no son originales"
        c=""
        for i in self.asientos:
            if isinstance(i,Asiento) == True:
                if i.registro == self.motor.registro and  i.registro == self.registro and self.registro== self.motor.registro:
                    c=a
                else:
                    c=b
                    break
        return c        

class Motor:
    def __init__(self,a,b,c):
        self.numeroCilindros=a
        self.tipo=b
        self.registro=c

    def cambiarRegistro(self,registro):
        self.registro=registro
        
    def asignarTipo(self,tipo):
        if tipo == "electrico" or tipo=="gasolina":
             self.tipo=tipo




