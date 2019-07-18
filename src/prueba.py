import numpy
from bitstring import Bits
from scipy.io import wavfile

if __name__ == '__main__':
    fs, wav = wavfile.read("../tono.wav")
    print(fs)
    print(wav)

    bit16_wav = [Bits(int=muestra, length=16).bin for muestra in wav]
    print(bit16_wav)
    bit_wav = list(numpy.array([[int(bit) for bit in bit16] for bit16 in bit16_wav]).flatten())
    print(bit_wav)

    str_bit_wav = [str(bit) for bit in bit_wav]
    new_bitchunk_wav = list(numpy.split(numpy.array(str_bit_wav), len(str_bit_wav) // 16))
    print(new_bitchunk_wav)
    new_bit16_wav = ["".join(bitchunk) for bitchunk in new_bitchunk_wav]
    print(new_bit16_wav)
    new_wav = [Bits(bin=bit16).int for bit16 in new_bit16_wav]
    print(new_wav)

    print("wav == new_wav ->", wav == new_wav)
