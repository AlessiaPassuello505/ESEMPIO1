#Scrivere una classe Cliente che abbia i campi "nome", "email", "categoria" ("Gold", "Silver", "Bronze").
#vorremmo che questa classe avesse un metodo che chiamiamo "descrizione"
# che deve restituire una stringa formattata ad esempio
#"Cliente Fulvio Bianchi (Gold) - fulvio@google.com"
from dataclasses import dataclass


class Cliente:
    def __init__(self, nome, mail, categoria):
        self.nome = nome
        self.mail = mail
        self.categoria = categoria

    def descrizione(self): #to_string
        # "Cliente Fulvio Bianchi (Gold) - fulvio@google.com"
        return f"Cliente {self.nome} ({self.categoria}) - {self.mail}"

def _test_modulo():
    c1 = Cliente("Mario Bianchi", "mario.bianchi@polito.it", "Gold")
    print(c1.descrizione())

@dataclass
class ClienteRecord:
        name: str
        email: str
        categoria: str

if __name__=="__main__":
    _test_modulo()