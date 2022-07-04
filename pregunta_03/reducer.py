#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
#
# Esta funcion reduce los elementos que tienen la misma clave
#
if __name__ == '__main__':

    lista1 = []
    lista2 = []
    #
    # cada linea de texto recibida se adiciona a la lista1
    #
    for line in sys.stdin:
        lista1.append(line)

    #ordenamiento de la lista1 y se guarda en la lista2
    lista2 = sorted(lista1, key=lambda x: x[2])

    for item in lista2:
        sys.stdout.write("{}".format(item))

    