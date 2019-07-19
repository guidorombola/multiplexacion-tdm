import numpy
from bitstring import Bits


class ConversorDecimalBinario:

    def __init__(self, bits_por_muestra):
        self.bits_por_muestra = bits_por_muestra

    def convertir_canales(self, canales):
        return [self.convertir_muestras(canal) for canal in canales]

    def convertir_muestras(self, muestras):
        # array_bits_agrupados = [Bits(int=muestra, length=self.bits_por_muestra).bin for muestra in muestras]
        array_bits_agrupados = []
        for muestra in muestras:
            if muestra == -32768:
                muestra += 1
            bits = Bits(int=muestra, length=self.bits_por_muestra).bin
            array_bits_agrupados.append(bits)
        array_bits = list(numpy.array([[int(bit) for bit in bit16] for bit16 in array_bits_agrupados]).flatten())

        return array_bits


class ConversorBinarioDecimal:

    def __init__(self, bits_por_muestra):
        self.bits_por_muestra = bits_por_muestra

    def convertir_canales(self, canales):
        return [self.convertir_muestras(canal) for canal in canales]

    def convertir_muestras(self, muestras):
        array_string_bits = [str(bit) for bit in muestras]
        cantidad_grupos_de_bits = len(array_string_bits) // self.bits_por_muestra
        array_de_arrays_bits = list(numpy.split(numpy.array(array_string_bits), cantidad_grupos_de_bits))
        array_bits_agrupados = ["".join(array_bits) for array_bits in array_de_arrays_bits]
        array_muestras_convertidas = [None if grupo_bits.startswith("None") else Bits(bin=grupo_bits).int for grupo_bits in array_bits_agrupados]

        return array_muestras_convertidas
