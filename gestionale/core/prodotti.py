# Scriviamo un codice python che modelli un semplice
# gestionale aziendale. Dovremo prvedere la possibilità di
# definire entità che modellano i prodotti, i clienti,
# offrire interfacce per calcolare i prezzi, eventualmente
# scontati, ...
from contextlib import suppress
from dataclasses import dataclass
from idlelib.debugobj import myrepr


class Prodotto:
    aliquota_iva = 0.22 #variabile di classe -- ovvero è la stessa per tutte le istanze che verranno create.

    def __init__(self, name: str, price: float, quantity: int, supplier = None):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.supplier = supplier

    def valore_netto(self):
        return self.price*self.quantity

    def valore_lordo(self):
        netto = self.valore_netto()
        lordo = netto*(1+self.aliquota_iva)
        return lordo

    def prezzo_finale(self):
        return self.price*(1+self.aliquota_iva)

    @classmethod
    def costruttore_con_quantità_uno(cls, name: str, price: float, supplier: str):
        return cls(name, price, 1, supplier)

    @staticmethod
    def applica_sconto(prezzo, percentuale):
        return prezzo*(1-percentuale)


    @property
    def price(self):
        return self._price
    @price.setter
    def price(self , valore):
        if valore<0:
            raise ValueError("Il prezzo non può essere negativo")
        self._price=valore

    def __str__(self ):
        return f"{self.name}- disponibili {self.quantity} pezzi a {self.price} $"

    def __repr__(self ):
        return f" Prodotto (name={self.name},price{self.price}, quantity={self.quantity}, supplier={self.supplier})"

    def __eq__(self,other:object):
        if not isinstance(other,Prodotto):
            return NotImplemented
        return(self.name==other.name and self.price==other.price and self.quantity==other.quantity
               and self.supplier==other.supplier)

    def __lt__(self,other:"Prodotto"):
        return self.price<other.price

class ProdottoScontato(Prodotto):
    def __init__(self,name:str, price:float, quantity:int,supplier:str,sconto_perc:float):
        super().__init__(name,price,quantity,supplier)
        self.sconto_perc=sconto_perc

    def prezzo_finale(self):
        return self.valore_lordo()*(1-self.sconto_perc/100)


class Servizio(Prodotto):
    def __init__(self,name:str, tariffa_oraria:float, ore:int):
        super().__init__(name=name,price=tariffa_oraria,quantity=1,supplier=None)
        self.ore=ore

    def prezzo_finale(self ):
        return self.price*self.ore


myproduct1 = Prodotto(name = "Laptop", price = 1200.0, quantity=12, supplier="ABC")

print(f"Nome prodotto: {myproduct1.name} - prezzo: {myproduct1.price}")

print(f"Il totale lordo di myproduct1 è {myproduct1.valore_lordo()}") #uso un metodo di istanza
p3 = Prodotto.costruttore_con_quantità_uno("Auricolari", 200.0, "ABC") #Modo per chiamare un metodo di classe.
print(f"Prezzo scontato di myproduct1 {Prodotto.applica_sconto(myproduct1.price, 0.15)}")#Modo per chiamare un metodo statico.

myproduct2 = Prodotto("Mouse", 10, 25, "CDE")
print(f"Nome prodotto: {myproduct2.name} - prezzo: {myproduct2.price}")

p_a = Prodotto(name="Laptop", price=1200.0, quantity= 12, supplier="ABC")
p_b=Prodotto( name="Mouse ", price=10, quantity= 14, supplier="CDE")
print(p3)

mylist=[p_a, p_b, myproduct1]
mylist.sort()
print("Lista prodotti ordinata")
for p in mylist:
    print(p)

prod_scontato=ProdottoScontato(name="Auricolari", price= 320, quantity=1,supplier="ABC",sconto_perc=10)
my_servizio=Servizio(name="Consulenza",tariffa_oraria=100, ore=3)

mylist.append(prod_scontato)
mylist.append(my_servizio)
mylist.sort(reverse=True)

for p in mylist:
    print(p.name, "-->", p.prezzo_finale())

print("----------------------------------------------------------------------")
class Abbonamento:
    def __init__(self,nome:str,prezzo_mensile:float, mesi:int):
        self.name=nome
        self.prezzo_mensile=prezzo_mensile
        self.mesi=mesi

    def prezzo_finale(self )->float:
        return self.prezzo_mensile*self.mesi

MAX_QUANTITA=1000

def crea_prodotto_standard(nome:str, prezzo:float):
    return Prodotto(nome,prezzo,quantity=1, supplier=None)

abb=Abbonamento(nome= "software gestionale", prezzo_mensile= 30.0, mesi=24)
mylist.append(abb)
for p in mylist:
    print(p.name, "-->", p.prezzo_finale())

def calcola_totale(elementi):
    tot=0
    for e in elementi:
        tot+=e.prezzo_finale()
    return tot

print(f"Il prezzo totale è: {calcola_totale(mylist)}")

from typing import Protocol

class HaPrezzoFinale(Protocol):
    def prezzo_finale(self  )->float :
        ...

def calcola_totale(elementi: list[HaPrezzoFinale])->float:
    return sum(e.prezzo_finale() for e in elementi)

@dataclass
class ProdottoRecord:
    name:str
    prezzo_unitario:float

    def __hash__(self):
        return hash((self.name,self.prezzo_unitario))

    def __str__(self):
        return f"{self.name} -- {self.prezzo_unitario}"


print(f"Il prezzo totale è: {calcola_totale(mylist)}")
print("-----------------------------------------------")