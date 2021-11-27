dolares = input("Ingresa la cantidad de dolares: ")
dolares = float (dolares)
valor_peso = 0.00027
pesos = dolares / valor_peso
pesos = round(pesos, 2)
pesos = str (pesos)
print ("Tienes $" + pesos + " pesos colombianos")