import sys
from src.TAREA import ejecutar_TAREA1
from src.TAREA2 import understanding_freq
from src.TAREA3 import ejecutar_tarea3
from src.TAREA4 import ejecutar_tarea4


def main(options):
    if options[1] == "tarea_1":
        ejecutar_TAREA1()


    elif options[1] == "tarea_2":
        if len(options) > 2:
            understanding_freq(options[2])
        else:
            print("Da una frecuencia. Ejemplo: python main.py tarea_2 2")
            

    elif options[1] == "tarea_3":
        if len(options) == 5:
            A = float(options[2])
            f = float(options[3])
            phi = float(options[4])
            ejecutar_tarea3(A, f, phi)
        else:
            print("Porfavor da los 3 parametros : Amplitud, Frequencia, y fase.")
            print("Ejemplo: python main.py tarea_3 1 2 0.785")

        
    elif options[1] == "tarea_4":
        if len(options) > 2:
            ejecutar_tarea4(options[2])
        else:
            print("Uso: python main.py tarea_4 <número_de_bits>")

if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        main(args)
    else:
        print("Da un argumento")
        print("Ejemplo ( run activity 1 ) : python main.py tarea_1")
        print("Ejemplo ( run activity 2 ) : python main.py tarea_2 1")
        print("Example ( run activity 3 ) : python main.py tarea_3 1 2 0.785")
        print("Example ( run activity 4 ) : python main.py tarea_4 3")