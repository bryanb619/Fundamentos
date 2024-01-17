class Pessoa:
    
    nome=''
    idade=0
    
    def __init__(self, nome, idade):
        self.nome=nome
        self.idade=idade
        
    def sayHello(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")
        


joao = Pessoa('João', 20)

beatriz = Pessoa('Beatriz', 19)


joao.sayHello()
beatriz.sayHello()


