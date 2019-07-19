from multiplexor import Multiplexor
from demultiplexor import Demultiplexor
from conversor import ConversorDecimalBinario, ConversorBinarioDecimal

import numpy as np
import scipy.io.wavfile as wav

def leer_pistas(nombres):
    canales = []
    fs = 44100
    for nombre in nombres:
        _, senial = wav.read(nombre)
        canales.append(senial)
    return canales, fs


def escribir_pistas(canales, fs):
    for num_canal, canal in enumerate(canales):
        nombre = "../canal{}_demultiplexado.wav".format(num_canal + 1)
        canal = np.array(canal)
        canal = canal.astype(dtype='int16')
        wav.write(nombre, fs, canal)


def main():
    canales, fs = leer_pistas(['../seno.wav', '../cuadrado.wav', '../sierra.wav'])
    cantidad_canales = len(canales)
    bits_por_muestra = 16
    bits_por_ranura = 16
    tasa_bits_canales_entrada = bits_por_muestra * fs

    conversor_decimal_binario = ConversorDecimalBinario(bits_por_muestra)
    conversor_binario_decimal = ConversorBinarioDecimal(bits_por_muestra)

    bits_canales = conversor_decimal_binario.convertir_canales(canales)

    mux = Multiplexor(tasa_bits_canales_entrada, bits_por_ranura, bits_canales)
    senial_multiplexada = mux.multiplexar()

    tasa_bits_entrada_demux = tasa_bits_canales_entrada * cantidad_canales
    demux = Demultiplexor(cantidad_canales, tasa_bits_entrada_demux, bits_por_ranura, senial_multiplexada)
    senial_demultiplexada = demux.demultiplexar()
    canales_recuperados = conversor_binario_decimal.convertir_canales(senial_demultiplexada)

    escribir_pistas(canales_recuperados, fs)


main()
