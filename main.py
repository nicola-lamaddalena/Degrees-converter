from sys import argv

def main(gradi):
    for grado in gradi[1:]:
        try:
            grado = int(grado)
            print(f'{grado}° Celsius sono {round((grado*(9/5))+32, 2)}° Fahrenheit')
        except ValueError:
            print("Inserisci valori numerici.")

main(argv)