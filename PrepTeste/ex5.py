
" Classe Pai " 
class Animal: 
    def falar(self):
        print ("Animal fez barulho!")
    
" Subclasses de Animal "
class Dog(Animal): 
    def falar(self):
        print("Dog is barking")
    
class Cat(Animal):
    def falar(self):
        print("Cat is purring")
    
class Bird(Animal):
    pass


# criação de intancias e chamadas de seus métodos existentes
dog = Dog()
dog.falar()

cat = Cat()
cat.falar()

bird = Bird()
bird.falar()
