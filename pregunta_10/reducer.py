#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
from dataclasses import replace
import operator
import sys
from collections import defaultdict

if __name__ == '__main__':
    Dict = defaultdict(list)
    for line in sys.stdin:
        key, val = line.replace("\n", "").strip().split("\t")
        val = val.split(",")
        
        for word in val:
            Dict[word].append(key)

sortedDict = sorted(Dict.items(), key=operator.itemgetter(0))
        
for k, v in sortedDict:
    res = sorted(v, key = int)
    v = ",".join(map(str, res))
    sys.stdout.write("{}\t{}\n".format(k, v))