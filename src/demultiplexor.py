class Demultiplexor:

    def __init__(self, cantidad_canales, fs, bits_por_muestra, bits_por_ranura, senial_multiplexada):
        self.fs = fs
        self.bits_por_ranura = bits_por_ranura
        self.tiempo_por_canal = (1 / (bits_por_muestra * fs)) * bits_por_ranura
        self.senial_multiplexada = senial_multiplexada
        self.cantidad_canales = cantidad_canales

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
