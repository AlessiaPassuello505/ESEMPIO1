import copy

from gestionale.core.prodotti import ProdottoRecord

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
s.update([ProdottoRecord("aaaa",20), ProdottoRecord("bbb",70)])# ne aggiunge più di 1 alla volta

#eliminare
s.remove(elemento) #elimina l'elemento, KeyError se non esiste
s.discard(elemento) #non dà l'errore se non esiste
s.pop() # rimuove e restituisce l'elemento
s.clear() #svuota tutto


s1=set()
s.union(s1) # equiv a s|s1
s.intersection(s1) #equiv a s&s1
s.difference(s1)  #elem di s che non sono in s1
s.symmetric_difference(s1) #elem di s1 non in s e elem di s non in s1
s.issubset(s1 )      #vedere se s è sottoinsieme di s1
s1.isdisjoint(s)  #insiemi disgiunti(elem diversi)

#DIZIONARIO








