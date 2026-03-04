from gestionale.vendite.ordini import Ordine, OrdineConSconto, RigaOrdine
from gestionale.core.prodotti import Prodotto, crea_prodotto_standard, ProdottoRecord
from gestionale.core.clienti import Cliente, ClienteRecord

p1=Prodotto(name="ebook",price=120, quantity=1, supplier="AAA" )
p2=crea_prodotto_standard(nome="tablet", prezzo=750)
print("=========================================0")
print(p1)
print(p2)
print("======================================================")


c1=Cliente(nome="Mario Rossi", mail="marioross@example.com", categoria="Gold" )

cliente1=ClienteRecord("Mario Rossi", "marioross@example.com", "Gold")
p1=ProdottoRecord("Laptotp", 1200.0)
p2=ProdottoRecord("Mouse", 20)
ordine=Ordine([RigaOrdine(p1,2), RigaOrdine(p2,10)], cliente1)
ord_scontato=OrdineConSconto([RigaOrdine(p1,2), RigaOrdine(p2,10)], cliente1,0.1)

print(ordine)
print(f"Numero righe ordine: {ordine.numero_righe()}")
print(f"Totale netto: {ordine.totale_netto()}")
print(f"Totale lordo (IVA 22%)  : {ordine.totale_lordo(0.22)}")
print(ord_scontato)
print(f"Totale netto sconto: {ord_scontato.totale_netto()}")
print(f"Totale lordo scontato: {ord_scontato.totale_lordo(0.22)}")


print("-------------------------------------------------------------")










