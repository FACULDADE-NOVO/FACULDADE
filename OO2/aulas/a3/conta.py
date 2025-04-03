#from rich import print
class Transacao:
    """ Atributos: op, tipo, data, valor, origem, destino, status """
    pass

class Conta: 
    """ Atributos: saldo, limite, pix, transacoes """
    def __init__(self,
                 saldo: float,
                  pix: str,
                  limite: float = 0,      
                 ):
        self.saldo = saldo
        self.pix = pix
        self.limite = limite   
        # 1 Conta possui N transacoes (1-N)
        self.transacoes: list[Transacao] = []
        
    @property
    def saldo_limite(self): #GETTER
        
        """
        Atributo dinamico - calculado com base no saldo da conta + limite disponivel, 
        ou seja, saldo_limite não é declarado no construtor da classe Conta.
        """
        return self._saldo + self.limite
        
        # GET PIX
        # SET PIX
        # validar: (1) é tipo string, (2) min de 4 char
        @pix.setter
        def pix(self, value):
            if not isinstance(value, str):
                raise Exception()
            if len(value) < 4:
                raise Exception("mínimo de 4 caracteres")
            self._value = value
        
    @property
    def saldo(self) -> float:   #MÉTODO GETTER
        return self.saldo;
    
    @saldo.setter    #MÉTODO SETTER
    
    def saldo(self, valor):
        #EXEMPLO DE VALIDAÇÃO
        if self.saldo < 0: 
            raise Exception()
        self._saldo = valor;
    
    
    def transferir(self, destino:"Conta", valor:float):
        cl = "red" if self.saldo < 0 else "blue"    
        """ realiza transferência pix """
          # self.saldo(self._saldo - valor)
        self.saldo -= valor # SETTER
        destino.saldo += valor # SETTER
        print(f"Saldo atual é R$ [{cl}] {self.saldo}[/] (conta {self.pix})");
        
    def consulta(self):
        """ consulta saldo da conta """
        print("-"*40)
        cl = "red" if self.saldo < 0 else "blue"
        print(f"Seu saldo atual é de R$ [{cl}]{self.saldo}[/] e seu pix é {self.pix}");
        pass

if __name__== "__main__":
# Testar:
  maria = Conta(saldo=20_000, pix="maria@pessoa.br", limite=2000)
  jose = Conta(saldo=-6000, pix="jose@pessoa.br")
  
  
  maria.consulta() #12_000
  jose.consulta() #2000
  
  
  maria.transferir(jose,8_000); # Pix de R$ 8.000 para jose@pessoa.br
  
    
  # Pix de R$8000 (maria@pessoa.br --> jose@pessoa.br)
  
  maria.consulta() # Saldo atual R$ de 12_000 (maria@pessoa.br)
  maria.transferir(jose,14_000); # Pix de R$ 8.000 para jose@pessoa.br
  
  jose.consulta()
  
