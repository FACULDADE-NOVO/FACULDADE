from datetime import datetime
from aulas.a3.conta import Conta
from rich import print

class Transacao:

    def __init_(self):
        """ op, data, valor, origem, destino, status
        """
        self.operacao: str = None
        self.data: datetime = None
        self.valor: float = None
        self.origem: Conta = None
        self.destino: Conta = None
        self.status: bool = False
        
                
    # MÉTODOS ESTÁTICOS:
    # não precisamos de uma instância da classe para usá-lo. Não há uso do "self"
        def credito(valor:float, 
                    origem: Conta,
                    destino: Conta) -> "Transacao":
            """cria uma transacao de credito"""
            t = Transacao()
            t.operacao = "C"
            t.data = datetime.now()
            t.valor = valor
            t.origem = origem
            t.destino = destino
            
            return t