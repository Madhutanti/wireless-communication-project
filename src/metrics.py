def calculate_ber (original_bits,received_bits):
    errors=(original_bits!=received_bits).sum()
    ber= errors/len(original_bits)
    return errors,ber

#BER = Number of Incorrect Bits / Total Number of Bits