class Demultiplexor:

    def __init__(self, cantidad_canales, tasa_bits_entrada, bits_por_ranura, senial_multiplexada):
        self.bits_por_ranura = bits_por_ranura
        self.senial_multiplexada = senial_multiplexada
        self.cantidad_canales = cantidad_canales
        self.tasa_bits_entrada = tasa_bits_entrada

    def demultiplexar(self):
        canales_demultiplexados = [[] for i in range(self.cantidad_canales)]
        canal_actual = 0
        for i in range(0, len(self.senial_multiplexada), self.bits_por_ranura):
            j = i
            while j < i + self.bits_por_ranura and j < len(self.senial_multiplexada):
                canales_demultiplexados[canal_actual].append(self.senial_multiplexada[j])
                j += 1
            canal_actual += 1
            if canal_actual > self.cantidad_canales - 1:
                canal_actual = 0

        return canales_demultiplexados

    def obtener_tiempo_de_ranura(self):
        return (self.tasa_bits_entrada / self.cantidad_canales) * self.bits_por_ranura
