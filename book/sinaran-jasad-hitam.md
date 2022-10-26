---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

<!-- TODO nak pindah ke quarto ke? -->

<!-- Quarto lebih mudah dan dependency-nya tak saling bercanggah -->

# Sinaran Jasad Hitam

Jasad hitam ialah suatu jasad yang akan menyerap kesemua panjang gelombang cahaya dengan sempurna tanpa pantulan dan memancarkan juga kesemua panjang gelombang apabila berada dalam keseimbangan haba.
Bintang-bintang memiliki sifat ini.

Rumus terbaik yang memerihalkan taburan cahaya yang dipancarkan oleh bintang ialah [hukum Planck](./sinaran-jasad-hitam/Planck.md).
Ada pun begitu, pelajar Fizik lazimnya diajar tentang dua cubaan lampau ialah [hukum taburan Wien](./sinaran-jasad-hitam/taburan-Wien.md) dan [hukum Rayleigh--Jean](./sinaran-jasad-hitam/Rayleigh-Jeans.md) bagi mengetengahkan kepentingan hukum Planck.
Perkembangan tersebut boleh didapati dalam bahagian [sejarah](./sinaran-jasad-hitam/sejarah.md).
Selain itu, [hukum sesaran Wien](./sinaran-jasad-hitam/) yang memerihalkan puncak graf serta [hukum Stefan--Boltzmann](./sinaran-jasad-hitam/Stefan-Boltzmann.md) yang memerihalkan luas bawah graf juga adalah dua hukum yang penting berkaitan sinaran jasad hitam.

```{code-cell} ipython3
---
tags: [remove-input]
---
import numpy as np
import matplotlib.pyplot as plt

def Planck(wavelength: np.ndarray, temperature: float, h: float = 6.62e-34, boltzmann: float = 1.38e-23, speed_of_light: float = 3e8) -> np.ndarray:
    wavelength_five: np.ndarray = wavelength**5
    exponent_component: np.ndarray = wavelength*temperature*boltzmann
    exponent_minus_one: np.ndarray = np.exp(h*speed_of_light/exponent_component) - 1
    return (8*np.pi*h*speed_of_light/wavelength_five) * (1/exponent_minus_one)

def Wien(wavelength: np.ndarray, temperature: float, h: float = 6.62e-34, boltzmann: float = 1.38e-23, speed_of_light: float=3e8) -> np.ndarray:
    wavelength_five: np.ndarray = wavelength**5
    exponent_component: np.ndarray = wavelength*temperature*boltzmann
    exponent_minus_one: np.ndarray = np.exp(h*speed_of_light/exponent_component)
    return (2*h*speed_of_light**2/wavelength_five) * (1/exponent_minus_one) * 1e-7

def RayleighJeans(wavelength: np.ndarray, temperature: float, h: float=6.62e-34, boltzmann: float = 1.38e-23, speed_of_light: float = 3e8) -> np.ndarray:
    wavelength_four: np.ndarray = wavelength**4
    numerator: float = boltzmann*temperature
    return 8*np.pi * numerator / wavelength_four / 10

wavelength: np.ndarray = np.arange(0.000_000_2, 0.000_002_5, step=0.2e-7)
temperature: float = 3_000

plt.plot(wavelength, Planck(wavelength, temperature), label='Planck')
plt.plot(wavelength, Wien(wavelength, temperature), label='Wien')
plt.plot(wavelength, RayleighJeans(wavelength, temperature), label='Rayleigh--Jeans')


wavelength_random: np.ndarray = np.arange(0.000_000_2, 0.000_002_5, step=0.8e-7)

x_rand = Planck(wavelength_random, temperature) + np.random.default_rng(200).integers(low=-100, high=100)

plt.scatter(wavelength_random, x_rand, label='mock', marker='+', color='red')

plt.ylim(0, 60_000)

plt.title('Perbandingan model Planck, Wien dan Rayleigh--Jeans')
plt.legend()
plt.show()

# TODO How to Caption?
```

```{tableofcontents}

```
