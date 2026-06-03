""" creare lista:
Clienti
Credito """

clienti = [ ]
credito = [ ]
print(clienti)
print(credito)

clienti.append('Giovanni Rossi')
clienti.append('Francesco Papa') 
clienti.append('Giulia Rossetti')
clienti.append('Adelaide Ceretti')
clienti.append('Jules McBrite')
credito.append(1250.95)

credito.append(2540)
credito.append(723.80)
credito.append(10)
credito.append(7500.36)
print(clienti)
print(credito)

clienti[0] = 'Enrico Pavone'
credito[0] = 12500.80
print(clienti)
print(credito)

clienti.remove(clienti[3])
credito.remove(credito[3])
print(clienti)
print(credito)


