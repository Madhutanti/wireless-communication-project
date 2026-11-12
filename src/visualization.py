import matplotlib.pyplot as plt


def plot_ber__vs_snr(snr_value ,ber_values):
    plt.figure(figsize=(8,5))

    plt.semilogy(
        snr_value,
        ber_values,
        marker='o'
    )

    plt.title("BPSK BER vs SNR")
    plt.xlabel("SNR(dB)")
    plt.ylabel("Bit Error Rte(BER)")
    plt.grid(True,which="both")

    plt.show()
