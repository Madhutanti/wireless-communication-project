#AWGN = Additive White Gaussian Noise

#In a real wireless channel, the transmitted signal is affected by noise.

#Mathematically:

#Received Signal = Transmitted Signal + Noise

import numpy as np

def add_awgn_noise(signal,snr_db):
    snr_linear = 10**(snr_db/10)
    signal_power=np.mean(signal**2)
    noise_power= signal_power/signal_power
    noise_std= np.sqrt(noise_power)
    noise= np.random.normal (0,noise_std,len(signal))
    received_siganl=signal+noise

    return received_siganl
