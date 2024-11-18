import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

tid = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76])  # Tid i minutter
temperatur_malt = np.array([98, 90, 83, 73, 66, 65, 60, 54, 56, 50, 48, 43, 43, 36, 36, 35, 32, 32, 30, 30, 28, 27, 26, 27, 26, ])  # Målte temperaturer i °C

Tk = 22  # °C

def temperatur_model(t, T0, alpha):
    return Tk + (T0 - Tk) * np.exp(-alpha * t)

T0 = temperatur_malt[0]

popt, _ = curve_fit(lambda t, alpha: temperatur_model(t, T0, alpha), tid, temperatur_malt)
alpha = popt[0]

teoretisk_temperatur = temperatur_model(tid, T0, alpha)


plt.plot(tid, temperatur_malt, 'o-', label='Målt data', color='blue')
plt.plot(tid, teoretisk_temperatur, '-', label=f'Teoretisk modell (alpha={alpha:.4f})', color='orange')
plt.xlabel('Tid (minutter)')
plt.ylabel('Temperatur (°C)')
plt.title('Sammenligning av målt og teoretisk temperatur')
plt.legend()
plt.grid(True)
plt.show()
print(f"Estimert verdi for alpha: {alpha:.4f}")


