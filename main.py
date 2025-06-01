import sys
from src.TAREA import ejecutar_TAREA1
def main(options):
    if options[1] == "tarea_1":
        ejecutar_TAREA1()
    elif options[1] == "tarea_2":
        if len(options) > 2:
            understanding_freq(options[2])
        else:
            print("Da una frecuencia. Ejemplo: python main.py tarea_2 2")

if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        main(args)
    else:
        print("Da un argumento")
        print("Ejemplo ( run activity 1 ) : python main.py tarea_1")
        print("Ejemplo ( run activity 2 ) : python main.py tarea_2 1")