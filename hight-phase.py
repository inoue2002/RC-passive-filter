
import matplotlib.pyplot as plt
import numpy as np
import math
import logging

def calculate_phase_difference(R, C, f):
    """
    Calculate the phase difference of an RC high-pass filter.
    
    Parameters:
    R (float): Resistance in ohms
    C (float): Capacitance in farads
    f (float): Frequency in hertz

    Returns:
    float: Phase difference in degrees
    """
    omega = 2 * math.pi * f
    # Calculate phase difference
    phase_diff = math.atan(1 / (omega * R * C))
    # Convert to degrees
    phase_diff = math.degrees(phase_diff)
    return phase_diff

if __name__ == "__main__":
    R = 10000  # Resistance in ohms
    C = 0.00000001 # Capacitance in farads
    frequencies = [200, 500, 1250, 1592, 20000]  # Frequencies in hertz
    phase_differences = [calculate_phase_difference(R, C, f) for f in frequencies]
    
    # Log the data used for the plot
    logging.basicConfig(level=logging.INFO)
    logging.info("Frequencies: %s", frequencies)
    logging.info("Phase differences: %s", phase_differences)
    
    # Plot the frequency response
    plt.figure()
    plt.semilogx(frequencies, phase_differences)
    plt.title('Phase difference of RC high-pass filter')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Phase difference [degrees]')
    plt.grid(True)
    plt.show()


