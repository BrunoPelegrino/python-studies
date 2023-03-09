# Para fixar crie uma objeto da classe Ventilador, em seguida
# faça com que a pessoa tenha um
# ventilador como atributo através da composição.
# Crie também um método comprar_ventilador.
# Faça com que o print (__str__) de Pessoa informe se sua instância
# possui ou não um ventilador.

class Ventilador:
    def __init__(self, cor, potencia, tensao, preco):
        self.preco = preco
        self.__cor = cor
        self.__potencia = potencia
        self.__tensao = tensao
        self.__ligado = False

    @property
    def cor(self):
        return self.__cor.upper()

    def __str__(self) -> str:
        return f"""
        a cor do ventilador é {self.__cor}
        """


class Pessoa:
    def __init__(self, nome, saldo_na_conta):
        self.nome = nome
        self.saldo_na_conta = saldo_na_conta
        self.ventilador = None

    def comprar_ventilador(self, ventilador):
        if ventilador.preco <= self.saldo_na_conta:
            self.saldo_na_conta -= ventilador.preco
            self.ventilador = ventilador

    def __str__(self) -> str:
        if self.ventilador:
            return f"""
        {self.nome} possui um ventilador e restam {self.saldo_na_conta}
        na conta
        """
        return f"""{self.nome} - não possui um ventilador
        e restam {self.saldo_na_conta} na conta
        """


ventilador_preto = Ventilador("Preto", 300, 220, 250)
pessoa_ventilador = Pessoa("Bruno", 5000)
pessoa_ventilador.comprar_ventilador(ventilador_preto)
print(pessoa_ventilador)
print(ventilador_preto.cor)
