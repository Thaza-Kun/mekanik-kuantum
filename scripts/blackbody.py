import numpy as np
from . import consts

_8pi: float = 8 * np.pi
_8pihc: float = _8pi * consts.h * consts.speed_of_light


def Planck(
    wavelength: np.ndarray,
    temperature: float,
) -> np.ndarray:
    wavelength_five: np.ndarray = wavelength**5
    exponent_component: np.ndarray = wavelength * temperature * consts.Boltzmann
    exponent_minus_one: np.ndarray = (
        np.exp(consts.h * consts.speed_of_light / exponent_component) - 1
    )
    return (_8pihc / wavelength_five) * (1 / exponent_minus_one)


def Wien(
    wavelength: np.ndarray,
    temperature: float,
) -> np.ndarray:
    wavelength_five: np.ndarray = wavelength**5
    exponent_component: np.ndarray = wavelength * temperature * consts.Boltzmann
    exponent_minus_one: np.ndarray = np.exp(
        consts.h * consts.speed_of_light / exponent_component
    )
    return (_8pihc / wavelength_five) * (1 / exponent_minus_one)


def RayleighJeans(
    wavelength: np.ndarray,
    temperature: float,
) -> np.ndarray:
    wavelength_four: np.ndarray = wavelength**4
    numerator: float = consts.Boltzmann * temperature
    return _8pi * numerator / wavelength_four
