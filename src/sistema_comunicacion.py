from multiplexor import Multiplexor
from demultiplexor import Demultiplexor
from conversor import ConversorDecimalBinario, ConversorBinarioDecimal
import matplotlib.pyplot as plt
import numpy as np


def main():
    '''
    En este ejemplo se multiplexan tres canales, tomando una muestra por canal. De acuerdo a lo esperado, como fs = 4
    y cada muestra se compone de 4 bits, entonces la tasa de bits de cada entrada es de 16 bps. Al tener 3 entradas, la
    capacidad de la linea de salida sera de 48 bps. La duracion de una trama es (1/16bps)*4bits = 0.25 segundos.
    Como es una multiplexacion sincrona, se asignarán las ranuras al tercer canal aun cuando no tenga más datos para
    transmitir.
    '''

    bits_por_muestra = 4
    conversor_decimal_binario = ConversorDecimalBinario(bits_por_muestra)
    conversor_binario_decimal = ConversorBinarioDecimal(bits_por_muestra)

    canales = [[1, 2, 3, 4, 5, -8, 6, 0], [-1, -2, -4, -3, -5, -8, -6, 0], [5, 6, 7, -3]]
    fs = 4
    bits_por_ranura = 4
    tasa_bits_canales_entrada = bits_por_muestra * fs
    cantidad_canales = len(canales)

    print('Canales entrantes: ', canales)
    bits_canales = conversor_decimal_binario.convertir_canales(canales)
    print('Entran al demultiplexor: ', bits_canales)
    print()

    mux = Multiplexor(tasa_bits_canales_entrada, bits_por_ranura, bits_canales)
    print('Tiempo por canal: {} seg'.format(mux.obtener_tiempo_de_ranura()))
    print()
    senial_multiplexada = mux.multiplexar()

    t = np.linspace(0, 2, fs * bits_por_muestra * 2 * cantidad_canales)
    plt.title('Señal multiplexada con duracion de trama {} seg. Entradas con fs = {} y {} bits por muestra'
              .format(mux.obtener_tiempo_de_ranura(), fs, bits_por_muestra))
    plt.stem(t, senial_multiplexada)
    plt.grid()
    plt.show()

    print('Señal multiplexada en binario: ', senial_multiplexada)
    print('Señal multiplexada en decimal: ', conversor_binario_decimal.convertir_muestras(senial_multiplexada))
    print()

    tasa_bits_entrada_demux = tasa_bits_canales_entrada * cantidad_canales
    demux = Demultiplexor(cantidad_canales, tasa_bits_entrada_demux, bits_por_ranura, senial_multiplexada)
    senial_demultiplexada = demux.demultiplexar()

    print('Canales demultiplexados: ', senial_demultiplexada)
    canales_recuperados = conversor_binario_decimal.convertir_canales(senial_demultiplexada)
    print('Canales demultiplexados en decimal: ', canales_recuperados)


main()
