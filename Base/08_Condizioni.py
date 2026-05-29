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