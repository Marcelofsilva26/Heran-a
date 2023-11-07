class Animal():
    def __init__(self,nome,cor):
        self.nome = nome
        self.cor = cor

    def emitirSom(self):
        print(f'O {self.nome} saída de som')

class Gato(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def emitirSom(self):
        print(f'O gato {self.nome} está miando')


class Vaca(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def emitirSom(self):
        print(f'A vaca {self.nome} está mugindo')


class Coelho(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def emitirSom(self):
        print(f'O coelho {self.nome} está ronronando')

class Cachorro(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def emitirSom(self):
        print(f'O cachorro {self.nome} está latindo')
