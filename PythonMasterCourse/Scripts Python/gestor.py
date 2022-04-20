from io import open
import pickle

class Personaje:

    def __init__(self, nombre, vida, ataque, defensa, alcance):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.alcance = alcance
    
    def __str__(self):
        return ("{}=> {} vida, {} ataque, {} defensa, {} alcance".format(self.nombre,self.vida, self.ataque, self.defensa, self.alcance))

class Gestor:

    personajes = []

    def __init__(self):
        self.cargar()
    
    def agregar(self,p):
        for pTemp in self.personajes:
            if pTemp.nombre == p.nombre:
                return
        self.personajes.append(p)
        self.guardar()

    def borrar(self,nombre):
        for pTemp in self.personajes:
            if pTemp.nombre == nombre:
                self.personajes.remove(pTemp)
                self.guardar()
                print("\nPersonaje {} borrado".format(nombre))
                return

    def mostrar(self):
        if len(self.personajes) ==0:
            print("El catalogo esta vacio")
            return
        for p in self.personajes:
            print(p)

    def cargar(self):
        fichero = open('personajes.pckl', 'ab+')
        fichero.seek(0)
        try:
            self.personajes = pickle.load(fichero)
        except:
            print("El fichero esta vacio")
        finally:
            fichero.close()
            print("Se han cargado {} personajes".format(len(self.personajes)))

    def guardar(self):
        fichero = open('personajes.pckl', 'wb')
        pickle.dump(self.personajes, fichero)
        fichero.close()

G = Gestor()
G.agregar(Personaje("Caballero", 2, 3, 4, 5))
G.agregar(Personaje("Guerrero", 1, 23, 2 ,3))
G.agregar(Personaje("Arquero", 1 ,2 ,3,4))
G.borrar("Arquero")
G.mostrar()