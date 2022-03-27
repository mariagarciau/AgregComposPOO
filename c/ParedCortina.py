class Pared:
    def __init__(self, orientacion, dimension):
        self.orientacion = orientacion
        self.dimension = dimension
        self.ventanas = []
    def superficie_cristal(self):
        superficie = 0
        for ventana in self.ventanas:
            superficie += ventana.dimension
        return superficie
class Ventana:
    def __init__(self, pared, tamañoVentana, proteccion):
        self.pared = pared
        self.dimension = tamañoVentana
        self.pared.ventanas.append(self)
        if proteccion is None:
            raise Exception("Campo de proteccion obligatorio")
        else:
            self.proteccion = proteccion

class Casa:
    def __init__(self, listaParedes):
        self.paredes = listaParedes
    def superficie_acristalada(self):
        superficie = 0
        for pared in self.paredes:
            superficie = superficie + pared.superficieCristal()
    def superficieNoCristal(self):
        suma = 0
        for pared in self.paredes:
            suma = suma + pared.dimension
        suma = suma - self.superficieAcristalada()
        return suma
class Proteccion:
    def __init__(self, proteccion):
        self.proteccion = proteccion


pared_norte = Pared("NORTE")
pared_oeste = Pared("OESTE")
pared_sur = Pared("SUR")
pared_este = Pared("ESTE")
ventana_norte = Ventana(pared_norte, 0.5)
ventana_oeste = Ventana(pared_oeste, 1)
ventana_sur = Ventana(pared_sur, 2)
ventana_este = Ventana(pared_este, 1)
casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este])
print(casa.superficie_acristalada())
print(casa.superficieNoCristal())

