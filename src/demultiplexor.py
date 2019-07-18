class Demultiplexor:

    def __init__(self, cantidad_canales, fs, tiempo_por_canal, senial_multiplexada):
        self.fs = fs
        self.tiempo_por_canal = tiempo_por_canal
        self.senial_multiplexada = senial_multiplexada
        self.cantidad_canales = cantidad_canales

    def demultiplexar(self):
        canales_demultiplexados = [[] for i in range(self.cantidad_canales)]
        muestras_por_canal = self.tiempo_por_canal * self.fs
        canal_actual = 0
        for i in range(0, len(self.senial_multiplexada), muestras_por_canal):
            j = i
            while j < i + muestras_por_canal and j < len(self.senial_multiplexada):
                canales_demultiplexados[canal_actual].append(self.senial_multiplexada[j])
                j += 1
            canal_actual += 1
            if canal_actual > self.cantidad_canales - 1:
                canal_actual = 0

        return canales_demultiplexados
