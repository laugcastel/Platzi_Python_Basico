import random


def run():
    numero_aleatortorio = random.randint (1, 100)
    numero = int(input ('Elige un numero del 1 al 100: '))
    while numero != numero_aleatortorio:
        if numero < numero_aleatortorio:
            print ('Busca un número más grande')
        else:
            print ('Busca un número más pequeño')
        numero = int(input ('Elige otro numero del 1 al 100: '))
    print ('Ganaste!!')
    
if __name__ == '__main__':
    run()