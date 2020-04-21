class Pessoa:
    def __init__(self, *filhos, nome=None, idade=10):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f"olá {self.nome} id({id(self)})"
        
if __name__ == "__main__":
    joao = Pessoa(nome='João')
    pedro = Pessoa(joao,nome='Pedro')
    print(Pessoa.cumprimentar(pedro))
    print(id(joao))
    for filho in pedro.filhos:
        print(filho.nome)