from multiplexor import Multiplexor
from demultiplexor import Demultiplexor

from src.conversor import ConversorDecimalBinario, ConversorBinarioDecimal


def main():
    bits_por_muestra = 8
    canales = [[1, 2, 3, 4, 9, 10, 11], [5, 6, 7, 8]]
    conversor_decimal_binario = ConversorDecimalBinario(bits_por_muestra)
    conversor_binario_decimal = ConversorBinarioDecimal(bits_por_muestra)
    bits_canales = conversor_decimal_binario.convertir_canales(canales)
    mul = Multiplexor(3, 1, bits_canales)
    print(bits_canales)
    senial_multiplexada = mul.multiplexar()
    print(senial_multiplexada)
    d = Demultiplexor(2, 3, 1, senial_multiplexada)
    senial_demultiplexada = d.demultiplexar()
    print(senial_demultiplexada)
    canales_recuperados = conversor_binario_decimal.convertir_canales(senial_demultiplexada)
    print(canales_recuperados)


main()
