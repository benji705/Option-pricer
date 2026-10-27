from math import *
import numpy as np
import random as rd
import matplotlib.pyplot as plt
from scipy.stats import norm


def Black_scholes(S,K,T,r,sigma,option_type="call"):
    # S: Prix de l'actif sous-jacent
    # K: Prix d'exercice (Strike)
    # T: Temps jusqu'à l'échéance (en années)
    # r: Taux d'intérêt sans risque
    # sigma: Volatilité de l'actif'
    d1= (np.log(S/K)+ (r+sigma**2/2)*T)/(sigma*sqrt(T))
    d2=d1-sigma*sqrt(T)
    if option_type=="call":
        price=S*norm.cdf(d1)-K*exp(-r*T)*norm.cdf(d2)
    elif option_type=="put":
        price=-S*norm.cdf(-d1)+K*exp(-r*T)*norm.cdf(-d2)
    return (price)

# Exemple d'utilisation
S = 100    # L'action vaut 100€
r = 0.05   # Taux à 5%
T = 1      # Échéance dans 1 an
sigma = 0.2 # Volatilité de 20%

# On teste différents Strikes pour voir l'évolution
strikes = [80, 90, 100, 110, 120]

print(f"{'Strike':<10} | {'Call Price':<12} | {'Put Price':<12}")
print("-" * 40)

for K in strikes:
    c = Black_scholes(S, K, T, r, sigma, 'call')
    p = Black_scholes(S, K, T, r, sigma, 'put')
    print(f"{K:<10} | {c:<12.2f} | {p:<12.2f}")
