class Perro():
       
    def __init__(self,raza,nombre,color) -> None:
        self.raza= raza
        self.nombre = nombre
        self.color= color
    
    def ladrar (self):
        print(self.nombre + " dice gua guau")
    def __str__(self) -> str:
        return self.nombre + " es " + self.raza + " " + self.color
#main


