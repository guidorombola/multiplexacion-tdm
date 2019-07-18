from multiplexor import Multiplexor
from demultiplexor import Demultiplexor
import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wav
from conversor import ConversorDecimalBinario, ConversorBinarioDecimal


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
    bits_por_muestra = 16
    bits_por_ranura = 16
    conversor_decimal_binario = ConversorDecimalBinario(bits_por_muestra)
    conversor_binario_decimal = ConversorBinarioDecimal(bits_por_muestra)

    canales, fs = leer_pistas(['../seno.wav', '../cuadrado.wav', '../sierra.wav'])

    bits_canales = conversor_decimal_binario.convertir_canales(canales)

    mux = Multiplexor(fs, bits_por_muestra, bits_por_ranura, bits_canales)
    senial_multiplexada = mux.multiplexar()

    demux = Demultiplexor(3, fs, bits_por_muestra, bits_por_ranura, senial_multiplexada)
    senial_demultiplexada = demux.demultiplexar()
    canales_recuperados = conversor_binario_decimal.convertir_canales(senial_demultiplexada)

    escribir_pistas(canales_recuperados, fs)


main()
