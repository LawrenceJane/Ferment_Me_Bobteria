# =====================================================
# Ferment me, Bobteria!
#
# yogurtconstant.py
#
# Biological constants from literature.
#
# Author: LawrenceJane
# =====================================================

BETA = 2.4               # g lactic acid / L / pH unit
# Estimated from Mistry & Kosikowski (1985):

# =====================================================
# Streptococcus thermophilus
# =====================================================

MU_MAX_S = 1.23          # h^-1     Rosso et al. (2023)

TMIN_S = 15.1            # °C       Rosso et al. (2023)
TOPT_S = 41.0            # °C       Rosso et al. (2023)
TMAX_S = 55.2            # °C       Rosso et al. (2023)

PHMIN_S = 2.98           #          Rosso et al. (2023)
PHOPT_S = 7.44           #          Rosso et al. (2023)
PHMAX_S = 8.60           #          Rosso et al. (2023)

YS = 0.095               # g/g      Degeest et al. (2001)

KS_S = 3.36              # g/L
    # Assumed equal to KS_L due to lack of
    # an identified published KS value for S. thermophilus.
    # This is a model assumption, not a literature-derived value.

ACID_YIELD_S = 0.556     #          Degeest & De Vuyst (1999)

SYMBIOSIS_ST = 0.25
    # Empirically calibrated parameters.
    # Selected based on the lowest RMSE among the
    # parameter combinations tested; not literature-derived.

# =====================================================
# Lactobacillus delbrueckii subsp. bulgaricus
# =====================================================

MU_MAX_L = 1.25          # h^-1     Rosso et al. (2023)

TMIN_L = 20.4            # °C       Rosso et al. (2023)
TOPT_L = 43.5            # °C       Rosso et al. (2023)
TMAX_L = 53.4            # °C       Rosso et al. (2023)

PHMIN_L = 3.27           #          Rosso et al. (2023)
PHOPT_L = 4.91           #          Rosso et al. (2023)
PHMAX_L = 9.28           #          Rosso et al. (2023)

YL = 0.1                 # g/g      Burgos-Rubio et al. (2000)

KS_L = 3.36              # g/L      Burgos-Rubio et al. (2000)

ACID_YIELD_L = 0.602     #          Rezvani, Ardestani & Najafpour (2017)

SYMBIOSIS_LB = 0.30
    # Empirically calibrated parameters.
    # Selected based on the lowest RMSE among the
    # parameter combinations tested; not literature-derived.