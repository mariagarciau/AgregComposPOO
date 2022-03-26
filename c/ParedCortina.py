class Pared(str):
    def z():
        pass

class Ventana(float):
    def z():
        pass

class Casa(list):
    def z():
        pass

class ParedCortina(list):
    def z():
        pass

# Instanciación de las paredes 
pared_norte = Pared("NORTE") 
pared_oeste = Pared("OESTE") 
pared_sur = Pared("SUR") 
pared_este = Pared("ESTE") 
# Instanciación de las ventanas 
ventana_norte = Ventana(pared_norte, 0.5) 
ventana_oeste = Ventana(pared_oeste, 1) 
ventana_sur = Ventana(pared_sur, 2) 
ventana_este = Ventana(pared_este, 1)
# Instanciación de la casa con las 4 paredes 
casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este])
print(casa.superficie_acristalada())
# >>> 4.5 # 0.5 + 1 + 2 + 1

casa.paredes[2] = ParedCortina("SUR", 10)
print(casa.superficie_acristalada())


ventana_norte = Ventana(pared_norte, 0.5)
ventana_norte = Ventana(pared_norte, 0.5, None)
ventana_norte = Ventana(pared_norte, 0.5, "Persiana")
print(casa.superficie_acristalada())