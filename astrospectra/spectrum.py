# spectrum.py

import pandas as pd
import matplotlib.pyplot as plt

class Spectrum:
    """Class representing an astronomical spectrum."""

    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)

    def plot(self):
        """Plot the spectrum."""
        plt.plot(self.data['wavelength'], self.data['intensity'])
        plt.xlabel('Wavelength')
        plt.ylabel('Intensity')
        plt.title('Astronomical Spectrum')
        plt.show()
