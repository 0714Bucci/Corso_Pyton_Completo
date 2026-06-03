"""
while esegue un blocco di codice fino a che 
la condizione restituisce True.
es:
while true:
    print()
    
"""
contatore_valore = 1

while contatore_valore <= 5:
    print(f'Esecuzione programma: {contatore_valore}')
    contatore_valore = contatore_valore + 1

risposta = ''
while risposta != 'logout':
    risposta = input(f'Digitare la richiesta: ')
    print(risposta)
print('Operazione conclusa corrttamente')