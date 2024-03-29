import math


class Multiplexor:

    def __init__(self, tasa_bits_canales_entrada, bits_por_ranura, canales):
        self.bits_por_ranura = bits_por_ranura
        self.tasa_bits_canales_entrada = tasa_bits_canales_entrada
        self.canales = canales

    def multiplexar(self):
        senial_multiplexada = []
        canales_estandarizados = self.igualar_longitudes(self.bits_por_ranura)
        muestras_multiplexadas = 0
        while (len(canales_estandarizados[0]) - muestras_multiplexadas) > 0:
            trama = []
            for j in range(len(canales_estandarizados)):
                slot_canal = []
                slot_canal.extend(
                    canales_estandarizados[j][muestras_multiplexadas: muestras_multiplexadas + self.bits_por_ranura])
                trama.extend(slot_canal)

            muestras_multiplexadas += self.bits_por_ranura
            senial_multiplexada.extend(trama)

        return senial_multiplexada

    def obtener_tiempo_de_ranura(self):
        return (1 / self.tasa_bits_canales_entrada) * self.bits_por_ranura

    def igualar_longitudes(self, muestras_por_canal):
        senial_mas_larga = max([len(canal) for canal in self.canales])
        a = math.floor(senial_mas_larga / muestras_por_canal)
        b = a * muestras_por_canal
        canales_estandarizados = []
        for canal in self.canales:
            canal_estandarizado = []
            vacios = [None] * (b - len(canal))
            canal_estandarizado.extend(canal)
            canal_estandarizado.extend(vacios)
            canales_estandarizados.append(canal_estandarizado)
        return canales_estandarizados

