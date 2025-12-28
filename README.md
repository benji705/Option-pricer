# Black-Scholes Option Pricer 📈

Ce projet est un outil d'analyse financière permettant de calculer le prix théorique des options européennes (Call et Put) en utilisant le modèle de **Black-Scholes-Merton**. 

Il combine des concepts d'**analyse fonctionnelle** (espaces de Hilbert, continuité) et de **finance quantitative**.

## 1. Concepts Théoriques

### Le Modèle de Black-Scholes
Le prix d'une option dépend de la probabilité que l'actif sous-jacent dépasse (pour un Call) ou tombe en dessous (pour un Put) du prix d'exercice (**Strike**) à l'échéance.

Les formules utilisées sont :
$$d_1 = \frac{\ln(S/K) + (r + \frac{\sigma^2}{2})T}{\sigma\sqrt{T}}$$
$$d_2 = d_1 - \sigma\sqrt{T}$$

Le prix du **Call ($C$)** et du **Put ($P$)** :
- **Call** : $C = S \cdot N(d_1) - K e^{-rT} \cdot N(d_2)$
- **Put** : $P = K e^{-rT} \cdot N(-d_2) - S \cdot N(-d_1)$

Où :
- $S$ : Prix actuel de l'actif (Spot)
- $K$ : Prix d'exercice (Strike)
- $T$ : Temps jusqu'à l'échéance (Maturité)
- $r$ : Taux d'intérêt sans risque
- $\sigma$ : Volatilité de l'actif
- $N(\cdot)$ : Fonction de répartition de la loi normale centrée réduite.





## 2. Fonctionnalités

- ✅ **Calcul du prix** : Support des options Call et Put.
- ✅ **Analyse de la Valeur Temps** : Décomposition entre valeur intrinsèque et valeur extrinsèque.
- ✅ **Parité Put-Call** : Vérification de la cohérence mathématique ($C - P = S - Ke^{-rT}$).
- ✅ **Visualisation** : Graphiques d'impact du Strike et de la Volatilité (à venir).

## 3. Installation et Utilisation

### Prérequis
- Python 3.8+
- `numpy`, `scipy`

```bash
pip install numpy scipy
