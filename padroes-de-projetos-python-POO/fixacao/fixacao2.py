# Implemente as classes Secador, Batedeira e MaquinaDeLavar,
# sempre herdando da classe Eletrodomestico.
# Para testar, instancie as novas classes e
# realize alguns prints, como por exemplo,
#  divulgando o preço do Eletrodoméstico.

class Eletrodomestico:
    def __init__(self, cor, potencia, tensao, preco):
        self.preco = preco
        self.cor = cor
        self._potencia = potencia
        self._tensao = tensao
        self.__ligado = False
        self.__velocidade = 0
        self.__velocidade_maxima = 3
        self.__corrente_atual_no_motor = 0

    def ligar(self, velocidade):
        if velocidade > self.__velocidade_maxima or velocidade < 0:
            raise ValueError(
                f"Velocidade deve estar entre 0 e {self.__velocidade_maxima}"
            )

        self.__velocidade = velocidade
        self.__corrente_atual_no_motor = (
            (self._potencia / self._tensao) / self.__velocidade_maxima
        ) * velocidade
        self.__ligado = True

    def desligar(self):
        self.__ligado = False
        self.__velocidade = 0

    def esta_ligado(self):
        return self.__ligado

    @property
    def cor(self):
        return self.__cor.upper()

    @cor.setter
    def cor(self, nova_cor):
        self.__cor = nova_cor


class Secador(Eletrodomestico):
    def __str__(self) -> str:
        return f"O secador {secador.cor} custa {secador.preco}."


class Batedeira(Eletrodomestico):
    def __str__(self) -> str:
        return f"A batedeira {batedeira.cor} custa {batedeira.preco}."


class MaquinaDeLavar(Eletrodomestico):
    def __str__(self) -> str:
        return f"""A maquina de lavar {maquina_de_lavar.cor}
        custa {maquina_de_lavar.preco}."""


secador = Secador("Branco", "450", "127", "400")
batedeira = Batedeira("Preto", "400", "127", "200")
maquina_de_lavar = MaquinaDeLavar("Laranja", "6000", "127", "3400")
print(secador)
print(batedeira)
print(maquina_de_lavar)
