import numpy as np


def generate_bits(num_bits):
    return np.random.randint(0,2,num_bits) #generation of random DeprecationWarning


def  bpsk_modulation(bits):
    return 2* bits-1


#demodulation , after receiving the noisy signal we have to convert into the original binary form


def bpsk_demodulation(received_signal):
    return(received_signal>0).astype(int)
    #Value > 0 → 1
    #Value <= 0 → 0
    