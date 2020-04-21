class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=10):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f"olá {self.nome} id({id(self)})"
    @staticmethod
    def metodo_estatico():
        return 42
    @classmethod
    def nome_e_atributo_de_clsse(cls):
        return f"{cls} olhos {cls.olhos}"
        
        
        
if __name__ == "__main__":
    joao = Pessoa(nome='João')
    pedro = Pessoa(joao,nome='Pedro')
    print(Pessoa.cumprimentar(pedro))
    print(id(joao))
    for filho in pedro.filhos:
        print(filho.nome)
    joao.sobrenome = "Silva"
    del pedro.filhos
    joao.olhos = 1
    Pessoa.olhos = 3
    print(joao.__dict__)
    print(pedro.__dict__)
    print(Pessoa.olhos)
    print(joao.olhos)
    print(pedro.olhos)
    print(id(Pessoa.olhos),id(joao.olhos),id(pedro.olhos))
    print(Pessoa.metodo_estatico(),joao.metodo_estatico())
    print(Pessoa.nome_e_atributo_de_clsse(),joao.nome_e_atributo_de_clsse())