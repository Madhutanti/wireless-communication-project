from src.modulation import generate_bits,bpsk_modulation
from src.modulation import bpsk_demodulation

from src.channel import add_awgn_noise
from src.metrics import calculate_ber
from src.visualization import plot_ber__vs_snr

# numbers of bits to generate
num_bits =  int (input("Enter the value : "))
bits= generate_bits(num_bits)
# perform BPSK modulation

bpsk_signal= bpsk_modulation(bits)
snr_values = [0, 2, 4, 6, 8, 10]
ber_values = []
for snr in snr_values:

    received_signal = add_awgn_noise(bpsk_signal, snr)

    received_bits = bpsk_demodulation(received_signal)

    errors, ber = calculate_ber(bits, received_bits)

    ber_values.append(ber)





print("========WIRELESS COMMUNICATION SIMULATION ========")

print("\n Number of Bits :",num_bits)
print("SNR :",snr_values,"dB")

print("\n Original Bits : ")
print(bits[:20])

print("\n Original Bits : ")
print (received_bits[:20])

print("\n Number of bit errors : ",errors)
print("Bit Error Rate (BER): ",ber)
import matplotlib.pyplot as plt


def plot_ber__vs_snr(snr_db,ber):
    plt.figure(figsize=(8,5))

    plt.semilogy(
        snr_db,
        ber,
        marker='o'
    )

    plt.title("BPSK BER vs SNR")
    plt.xlabel("SNR(dB)")
    plt.ylabel("Bit Error Rte(BER)")
    plt.grid(True,which="both")

    plt.show()


plot_ber__vs_snr(snr_values,ber_values)




