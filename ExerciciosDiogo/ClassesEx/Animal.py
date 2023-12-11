class Animal:
    def falar(self):
        print("Um animal faz algum som.")
        
        
        
class Cachorro(Animal):
    def falar(self):
        # super().falar() chama o método falar da classe pai
        print("O cachorro late.")
        
        
        
        
class Gato(Animal):
    def falar(self):
        print("O gato mia.")
        
        
        
chachorro = Cachorro()
chachorro.falar()

gato = Gato()
gato.falar()

