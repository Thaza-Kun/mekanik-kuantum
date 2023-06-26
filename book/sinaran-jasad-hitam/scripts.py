#!/bin/python3.11

import numpy as np
import matplotlib.pyplot as plt
from typing import Callable

h: float = 6.62e-34
Boltzmann: float = 1.38e-23
speed_of_light: float = 3e8

_8pi: float = 8 * np.pi
_8pihc: float = _8pi * h * speed_of_light


def Planck(
    wavelength: np.ndarray,
    temperature: float,
) -> np.ndarray:
    wavelength_five: np.ndarray = wavelength**5
    exponent_component: np.ndarray = wavelength * temperature * Boltzmann
    exponent_minus_one: np.ndarray = (
        np.exp(h * speed_of_light / exponent_component) - 1
    )
    return (_8pihc / wavelength_five) * (1 / exponent_minus_one)

def Wien(
    wavelength: np.ndarray,
    temperature: float,
) -> np.ndarray:
    wavelength_five: np.ndarray = wavelength**5
    exponent_component: np.ndarray = wavelength * temperature * Boltzmann
    exponent_minus_one: np.ndarray = np.exp(
        h * speed_of_light / exponent_component
    )
    return (_8pihc / wavelength_five) * (1 / exponent_minus_one)


def RayleighJeans(
    wavelength: np.ndarray,
    temperature: float,
) -> np.ndarray:
    wavelength_four: np.ndarray = wavelength**4
    numerator: float = Boltzmann * temperature
    return _8pi * numerator / wavelength_four

def plot_blackbody_by_wavelength(
    models: [(Callable[[np.ndarray, float], np.ndarray], str), ...],
    title: str,
    wavelength: (float, float) = (0.000_000_2, 0.000_004),
    temperature: float = 3_000,
    mock_data: str | None = None,
) -> None:
    """Plots a blackbody radiation model(s)

    Args:
        models (Iterable[(model, label)]): A list of tuple of models and labels
        title (str): Title of the graph
        wavelength (Tuple[float, float], optional): Range of wavelengths to plot. Defaults to (0.000_000_2, 0.000_004).
        temperature (float, optional): The temperature of blackbody. Defaults to 3_000.
        mock_data (str | None, optional): Label of mock_data. None means no mock data. (Mock data will always follow Planck's Law). Defaults to None.
    """
    wavelengths: np.ndarray = np.arange(wavelength[0], wavelength[1], step=0.2e-7)

    for model, label in models:
        plt.plot(wavelengths, model(wavelengths, temperature), label=label)

    if mock_data:
        wavelength_random: np.ndarray = np.arange(
            wavelength[0], wavelength[1], step=0.8e-7
        )
        x_rand: np.ndarray = Planck(
            wavelength_random, temperature
        ) + np.random.default_rng(200).integers(low=-100, high=100)
        plt.scatter(wavelength_random, x_rand, label=mock_data, color="red", marker="x")  # type: ignore

    plt.ylim(0, 60_000)

    plt.title(title)
    plt.xlabel("panjang gelombang")
    plt.ylabel("keamatan")
    plt.legend()
    plt.show()