class Pessoa:
    def __init__(self, nome=None, idade=10):
        self.nome = nome
        self.idade = idade
    def cumprimentar(self):
        return f"olá {self.nome} id({id(self)})"
        
if __name__ == "__main__":
    p = Pessoa('João')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    p.nome= "Ari"
    print(p.cumprimentar())
    print(p.idade)