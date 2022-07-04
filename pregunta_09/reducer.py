#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':

    value = []
    ky = []
    fech = []

    for line in sys.stdin:
        ky.append(line.split("\t")[0])
        fech.append(line.split("\t")[1])
        value.append(int(line.split("\t")[2]))

    ky_value = zip(ky, fech, value)

    ky_value_2 = sorted(ky_value,key=lambda x:x[2])
    final = ky_value_2[:6]

    for ky, fech, value in final:
      sys.stdout.write("{}   {}   {}\n".format(ky, fech, value))