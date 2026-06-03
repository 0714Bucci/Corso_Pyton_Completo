#condizione IF,ELIF,else
cliente = input('Hai una prenotazione? ')
if cliente == 'si':
    print('ok')
else:
    print('Non abbiamo posti disponibili')

cliente = input('Hai una prenotazione? ')
if cliente == 'si':
    print('ok')
elif cliente == 'no':
    print('Siamo Spiacenti non ci sono posti disponibili')
else:
    print('Errore, devi rispondere si o no')


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
