""" Liste in pyton: strutture di dati che si possono salvare insieme

Studenti  = ['Luca', 'Luigi', 'Andrea', 'Rudy']
print (Studenti)

Studenti.append('Teresa')
print(Studenti)

accesso agli elementi
print(Studenti[5])

"""

#esercizio

cliente = input('Buongiorno, selezioni operazione da eseguire: ')
if cliente == 'prelievo':
    importo = int(input('Quale importo vorrebbe prelevare? '))
    if importo == 1000:
        print('Erogazione in corso')
    elif importo == 3000:
        print('Importo non erogabile')
    else:
        print('Terminale al momento non disponibile')
elif cliente == 'estratto conto mensile':
    print('estratto conto dei movimenti degli ultimi 30 giorni')
else:
    print('Operazione non disponibile')
