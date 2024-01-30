# gaussian_fit.py

import numpy as np
from scipy.optimize import curve_fit

def gaussian(x, amp, cen, wid):
    """Gaussian function."""
    return amp * np.exp(-(x-cen)**2 / (2*wid**2))

def fit_spectrum(spectrum):
    """Fit a Gaussian model to a spectrum."""
    popt, _ = curve_fit(gaussian, spectrum.data['wavelength'], spectrum.data['intensity'])
    return popt
