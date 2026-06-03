#Liste in pyton: strutture di dati che si possono salvare insieme
#puoi mettere più tipologie di dati

Studenti  = ['Luca', 'Luigi', 'Andrea', 'Rudy','Rudy', 'Claudia']
print (Studenti)

Studenti.append('Teresa')
print(Studenti)

#accesso agli elementi
print(Studenti[5])

Studenti.append('Marco')
print(Studenti)
print(Studenti[-1])

#modificare gli elementi
Studenti[0] = 'Gaia'#metti posizione e nuovo valore
print(Studenti[0])

#rimuovere elementi
Studenti.remove(Studenti[6])
print(Studenti)

