""" 
CICLO FOR E FUNZIONE RANGE:
permette di ripetere un blocco di codice 
per un numero specifico di volte

range(5) ossia il range di numeri da 0 a 4
range(6) genera numeri da 0 a 5
range(2,7,2) genera i numeri da 2 4 6 

for 'valore di default(i)' in range(numero(5)):
    print(f'messaggio: {i}')
"""

"""for i in range(5):
    print(f'Sono il numero:{i}')

Studenti  = ['Luca', 'Luigi', 'Andrea', 'Rudy','Rudy', 'Claudia']

for Studenti in Studenti:
    print(f'Mi chiamo: {Studenti}')"""

#restituisci un numero moltiplicato x tot volte

numeri = 5

print(f'\nTavolo di moltiplicazione {numeri}\n')
for i in range(1, 11):
    risultato = numeri * i
    print(f"{numeri} x {i} = {risultato}")

print(f'\nTavolo di moltiplicazione Completa da 1 a 10\n')
for i in range(1, 12):
    for j in range(1, 12):
        risultato = i * j
        print(f"{i} x {j} = {risultato}\n")



