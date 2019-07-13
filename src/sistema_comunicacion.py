from multiplexor import Multiplexor
from demultiplexor import Demultiplexor


def main():
    canales = [[1, 2, 3, 4, 9, 10, 11], [5, 6, 7, 8]]
    mul = Multiplexor(3, 1, canales)
    senial_multiplexada = mul.multiplexar()
    print(senial_multiplexada)
    d = Demultiplexor(2, 3, 1, senial_multiplexada)
    print(d.demultiplexar())


main()
