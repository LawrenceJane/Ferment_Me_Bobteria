import numpy as np
import matplotlib.pyplot as plt


# =====================================================
# pH Response Function
# =====================================================

def pH_factor(pH, pHopt, sigma_pH):

    return np.exp(
        -((pH - pHopt) ** 2)
        /
        (2 * sigma_pH ** 2)
    )
# =====================================================
# Parameters
# =====================================================

PHOPT_S = 7.44
PHOPT_L = 4.91

SIGMA_PH = 1.2


# =====================================================
# pH Range
# =====================================================

pH_values = np.linspace(3, 8, 300)


# =====================================================
# Calculate Response
# =====================================================

pH_response_s = pH_factor(
    pH_values,
    PHOPT_S,
    SIGMA_PH
)

pH_response_l = pH_factor(
    pH_values,
    PHOPT_L,
    SIGMA_PH
)


# =====================================================
# Plot
# =====================================================

plt.figure(figsize=(9, 6))

plt.plot(
    pH_values,
    pH_response_s,
    linewidth=2,
    label="S. thermophilus"
)

plt.plot(
    pH_values,
    pH_response_l,
    linewidth=2,
    label="L. bulgaricus"
)

plt.xlabel("pH")
plt.ylabel("Relative Growth Rate")

plt.title("pH Response of Yogurt Starter Cultures")

plt.legend()

plt.grid(True)

plt.xlim(3, 8)
plt.ylim(0, 1.05)

plt.tight_layout()

plt.show()