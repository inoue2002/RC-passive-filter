
import matplotlib.pyplot as plt
import numpy as np
import math
import logging

def calculate_theoretical_amplitude(R, C, f):
    """
    Calculate the theoretical amplitude of an RC high-pass filter.
    
    Parameters:
    R (float): Resistance in ohms
    C (float): Capacitance in farads
    f (float): Frequency in hertz

    Returns:
    float: Theoretical amplitude
    """
    omega = 2 * math.pi * f
    # Convert to decibels
    omega = 20 * math.log10(math.sqrt(1 + (omega * R * C) ** 2))
    return omega

if __name__ == "__main__":
    R = 10000  # Resistance in ohms
    C = 0.00000001 # Capacitance in farads
    frequencies = [200, 1250, 1592, 5000, 20000]  # Frequencies in hertz
    amplitudes = [calculate_theoretical_amplitude(R, C, f) for f in frequencies]
    
    # Log the data used for the plot
    logging.basicConfig(level=logging.INFO)
    logging.info("Frequencies: %s", frequencies)
    logging.info("Amplitudes: %s", amplitudes)
    
    # Plot the frequency response
    plt.figure()
    plt.semilogx(frequencies, amplitudes)
    plt.title('Frequency response of RC high-pass filter')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Amplitude [dB]')
    plt.grid(True)
    plt.show()

