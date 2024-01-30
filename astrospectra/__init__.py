# __init__.py for the AstroSpectra package

# Import classes and functions from modules for easier access
from .spectrum import Spectrum
from .gaussian_fit import gaussian, fit_spectrum

# Define what should be available at the package level
__all__ = ['Spectrum', 'gaussian', 'fit_spectrum']
