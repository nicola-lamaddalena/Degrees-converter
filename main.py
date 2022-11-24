from sys import argv

def main(degrees):
    for degree in degrees[1:]:
        try:
            degree = int(degree)
            print(f'{degree}° Celsius are {round((degree*(9/5))+32, 2)}° Fahrenheit')
        except ValueError:
            print("You need to type numeric values.")

main(argv)
