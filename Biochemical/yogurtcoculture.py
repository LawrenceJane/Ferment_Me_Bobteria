import numpy as np
from scipy.integrate import solve_ivp


# =====================================================
# Ferment me, Bobteria!
#
# yogurtcoculture.py
#
# Version 2.2
#
# Two-species yogurt fermentation model
#
# Author: LawrenceJane
# =====================================================

# =====================================================
# Monod Growth
# =====================================================

def monod(S, mumax, Ks):

    if S <= 0:
        return 0

    return mumax * S / (Ks + S)


# =====================================================
# Temperature Factor
# =====================================================

def temperature_factor(T, Topt, sigma):

    return np.exp(
        -((T - Topt) ** 2)
        /
        (2 * sigma ** 2)
    )


# =====================================================
# pH Factor
# =====================================================

def pH_factor(pH, pHopt, sigma_pH):

    return np.exp(
        -((pH - pHopt) ** 2)
        /
        (2 * sigma_pH ** 2)
    )

# =====================================================
# Acid Inhibition
# =====================================================

def acid_factor(P, Ki):

    return 1 / (1 + P / Ki)


# =====================================================
# Symbiosis
# =====================================================

def symbiosis_factor(other_species, alpha):

    return 1 + alpha * other_species


# =====================================================
# Overall Growth Rate
# =====================================================

def growth_rate(
    S,
    mumax,
    Ks,
    temperature,
    Topt,
    sigma,
    pH,
    pHopt,
    sigma_pH,
    P,
    Ki,
    other_species,
    alpha,
    symbiosis_coefficient,
):

    return (
        monod(S, mumax, Ks)
        *
        temperature_factor(temperature, Topt, sigma)
        *
        pH_factor(pH, pHopt, sigma_pH)
        *
        acid_factor(P, Ki)
        *
        symbiosis_factor(other_species, alpha)
        *
        symbiosis_coefficient
    )

# =====================================================
# Co-culture Simulation
# =====================================================

def yogurt_coculture(
    Xs0,
    Xl0,

    S0,
    P0,

    fermentation_time,

    mumax_s,
    Ks_s,

    mumax_l,
    Ks_l,

    Ys,
    Yl,

    Yps,
    Ypl,

    temperature,

    Topt_s,
    Topt_l,

    sigma,

    sigma_pH,

    pH0,

    pHopt_s,
    pHopt_l,

    Ki,

    BETA,

    alpha_s,
    alpha_l,

    symbiosis_st,
    symbiosis_lb,

    pH_min=3.5
):

    def model(t, y):

        Xs, Xl, S, P, pH = y


        # -----------------------------------------
        # Prevent negative values
        # -----------------------------------------

        Xs = max(Xs, 0)
        Xl = max(Xl, 0)
        S = max(S, 0)
        P = max(P, 0)


        # -----------------------------------------
        # Growth rates
        # -----------------------------------------

        mu_s = growth_rate(
            S,
            mumax_s,
            Ks_s,
            temperature,
            Topt_s,
            sigma,
            pH,
            pHopt_s,
            sigma_pH,
            P,
            Ki,
            Xl,
            alpha_s,
            symbiosis_st,
            
        )


        mu_l = growth_rate(
            S,
            mumax_l,
            Ks_l,
            temperature,
            Topt_l,
            sigma,
            pH,
            pHopt_l,
            sigma_pH,
            P,
            Ki,
            Xs,
            alpha_l,
            symbiosis_lb,
            
        )


        # -----------------------------------------
        # Biomass growth
        # -----------------------------------------

        dXsdt = mu_s * Xs

        dXldt = mu_l * Xl


        # -----------------------------------------
        # Lactose consumption
        # -----------------------------------------

        lactose_s = mu_s * Xs / Ys

        lactose_l = mu_l * Xl / Yl

        dSdt = -(lactose_s + lactose_l)


        # -----------------------------------------
        # Lactic acid production
        # -----------------------------------------

        dPdt = (
            Yps * lactose_s
            +
            Ypl * lactose_l
        )


        # -----------------------------------------
        # pH change
        # -----------------------------------------

        dpHdt = -dPdt / BETA


        return [

            dXsdt,

            dXldt,

            dSdt,

            dPdt,

            dpHdt

        ]


    # =================================================
    # Solve ODE
    # =================================================

    solution = solve_ivp(

        model,

        (
            0,
            fermentation_time
        ),

        [

            Xs0,
            Xl0,
            S0,
            P0,
            pH0

        ],

        t_eval=np.linspace(

            0,
            fermentation_time,
            300

        )

    )


    return solution