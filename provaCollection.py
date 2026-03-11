import copy
from collections import Counter

from gestionale.core.clienti import ClienteRecord
from gestionale.core.prodotti import ProdottoRecord
from gestionale.vendite.ordini import Ordine

p1=ProdottoRecord("Laptop", 1200)
p2=ProdottoRecord("Mouse", 20)
p3=ProdottoRecord("Auricolari", 250)

carrello=[p1,p2,p3, ProdottoRecord("Tablet", 700)] #posso anche crearlo dentro

carrello.sort(key=lambda x: x.prezzo_unitario)

print("Prodotti nel carrello")
for i,p in enumerate(carrello):
    print(f"{i}) {p.name} - {p.prezzo_unitario}")

#aggiungere a una lista
carrello.append(ProdottoRecord("Monitor", 150))


carrello.sort(key=lambda x: x.prezzo_unitario)

print("Prodotti nel carrello ordinati")
for i,p in enumerate(carrello):
    print(f"{i}) {p.name} - {p.prezzo_unitario}")

tot=sum(p.prezzo_unitario for p in carrello)
print(f"Totale del carrello: {tot}")

carrello.extend([ProdottoRecord("aaaa", 75), ProdottoRecord("bbbb", 60)])#aggiungo più cose
carrello.insert(2, ProdottoRecord("cccc",100))

#rimuovere
carrello.pop(2)         #rimuove l'elemento in pos 2
carrello.remove(p1)   #rimuove la prima occorrenza di p1
carrello.clear()    #elimina tutto

#ordinamento
carrello.sort(reverse=True) #ordina al contrario
carrello_ordinato=sorted(carrello) #crea una nuova lista ordinata di carrello
carrello.reverse()          #inverte l'ordine della lista
carrello_copia=carrello.copy()  #crea una copia di carrello(se modifico carrello, modifico anche questo)
carrello_copia2=copy.deepcopy(carrello) # copia di carrello fissa

#TUPLA

sede_principale=(45,8) #latitudine e longitudine sede di torino
sede_milano=(45,9)      #milano

print(f"Sede principale lat: {sede_principale[0]}, long: {sede_principale[1]}")

aliquoteIVA=(
("Standard", 0.22),
("Ridotta" ,0.10),
("Alimentari", 0.04),
("Esente",0)
)
for descr,valore in aliquoteIVA:
    print(f" {descr} - {valore} %")

def calcola_statistiche_carrello(carrello):
    if  not carrello:
        return(0,0,0,0)
    prezzi=[(p.prezzo_unitario )for p in carrello]
    return (sum(prezzi),sum(prezzi)/len(prezzi), max(prezzi), min(prezzi))

tupla=calcola_statistiche_carrello(carrello)  #creo tupla
tot,media,max,min=calcola_statistiche_carrello(carrello)   #unpacking
tot,*altri_campi=calcola_statistiche_carrello(carrello) #il primo è tot, gli altri vanno in "altri campi"

#INSIEMI,SET: no duplicati

categorie={"Gold","Silver","Bronze", "Gold"}
print(categorie)

categorie2={"Elite"," Platinum", "Gold"}
#tutte_cat=categorie.unionAll(categorie2)
cat_all=categorie | categorie2      #unione

cat_comuni=categorie & categorie2   #interesezione
print(cat_comuni)

s=set()
#s.update([ProdottoRecord("aaaa",20), ProdottoRecord("bbb",70)])# ne aggiunge più di 1 alla volta

#eliminare
#s.remove(elemento) #elimina l'elemento, KeyError se non esiste
#s.discard(elemento) #non dà l'errore se non esiste
#s.pop() # rimuove e restituisce l'elemento
#s.clear() #svuota tutto


s1=set()
s.union(s1) # equiv a s|s1
s.intersection(s1) #equiv a s&s1
s.difference(s1)  #elem di s che non sono in s1
s.symmetric_difference(s1) #elem di s1 non in s e elem di s non in s1
s.issubset(s1 )      #vedere se s è sottoinsieme di s1
s1.isdisjoint(s)  #insiemi disgiunti(elem diversi)

#DIZIONARIO
catalogo={
    "LAP001" : ProdottoRecord("Laptop", 1200),
    "LAP002" :ProdottoRecord("laptop Pro", 2300),
    "MAU001" :ProdottoRecord("mouse", 20),
    "AUR001" :ProdottoRecord("auricolari", 250)
}

cod="LAP002"
prod=catalogo[cod]
print(f"Il prodotto con codice {cod} è {prod}")

prod1=catalogo.get("NonEsiste")
if prod1 is None:
    print("Prodotto non trovato")

prod2=catalogo.get("NonEsiste2", ProdottoRecord("Sconosciuto", 0))

print(prod2)

keys=list(catalogo.keys())
valori=list(catalogo.values())
for k in keys:
    print(k)
for v in valori:
    print(v)

for k,v in catalogo.items():
    print(f"Cod: {k} è associata a :{v}")

rimosso=catalogo.pop("LAP002")
print(f"Rimosso: {rimosso}")

#dict comprehension
prezzi={ codice: prod.prezzo_unitario for codice,prod in catalogo.items()}

#METODI PER DICT
# if key in d : condiz che verifica se d è presente in d

#ESERCIZIO: decidere la struttura dati migliore

#1) Lista di ordini processati in ordine di arrivo
lista_ordini=[]
o1=Ordine([], ClienteRecord("Mario","marioro@gmail.it","Gold"))
o2=Ordine([], ClienteRecord("Elisa","elisabi@gmail.it","Gold"))
o3=Ordine([], ClienteRecord("Luisa","luisagi@gmail.it","Gold"))
o4=Ordine([], ClienteRecord("Matteo","matteokki@gmail.it","Silver"))
lista_ordini.append((o1,0))
lista_ordini.append((o2,10))
lista_ordini.append((o3, 3))
lista_ordini.append((o4,45))   #tuple con valore e tempo di arrivo


#2) Memorizza codici fiscali dei clienti(univoco)
codici_fiscali={"fjfjjdfdkn", "hjfjhfjkdkj", "eleiwqoeop", "eleiwqoeop"}
print(codici_fiscali)

#3) database di prodotti che posso cercare con un codice univoco
diz_prodotti={"lap001" : ProdottoRecord("Laptop", 1200),
              "KEY002": ProdottoRecord("Keyboard", 30)
              }

#4) memorizza coordinate GPS sede di Roma
coordinate_Roma=(45,7)

#5) memorizza categorie di clienti che hanno fatto un ordine in un range temporale
categorie_ordini_periodo=set()
categorie_ordini_periodo.add("Gold")
categorie_ordini_periodo.add("Bronze")

print("=============================================================================================")

#COUNTER
lista_clienti=[
    ClienteRecord("Mario","marioro@gmail.it","Gold"),
    ClienteRecord("Elisa","elisabi@gmail.it","Bronze"),
    ClienteRecord("Luisa","luisagi@gmail.it","Gold"),
    ClienteRecord("Matteo","matteokki@gmail.it","Silver"),
    ClienteRecord("Anna","annari@gmail.it","Silver"),
    ClienteRecord("Giulia","giuliade@gmail.it","Bronze"),
    ClienteRecord("Luca","lucabl@gmail.it","Silver"),
    ClienteRecord("Emma", "emmagi@gmail.it", "Gold"),
    ClienteRecord("Serena", "sereti@gmail.it", "Gold")


    ]
categorie=[c.categoria for c in lista_clienti]
categorie_counter=Counter(categorie)

print("Distribuzione categorie clienti: ")
print(categorie_counter)
print("Categoria più frequente")
print(categorie_counter.most_common(1)) #prende LA più frequente
print("Totale")
print(categorie_counter.total())

vendite_gennaio=Counter(
    {"Laptop": 13, "Tablet": 15}
)
vendite_febbraio=Counter(
    {"Laptop": 3, "Stampante": 1}

)

#AGGREGARE
vendite_bimestre=vendite_gennaio+vendite_febbraio
print(f"vendite Gennaio: {vendite_gennaio}")
print(f"vendite Febbraio: {vendite_febbraio}")
print(f"vendite bimestre: {vendite_bimestre}")

#DIFFERENZA
print(f"Differenza di vendite : {vendite_gennaio-vendite_febbraio}")

vendite_gennaio["Laptop"]+=4
print(f"vendite Gennaio: {vendite_gennaio}")

#metodi
#c.most_common(n)   el più frequenti
# c.total() somma conteggi
















