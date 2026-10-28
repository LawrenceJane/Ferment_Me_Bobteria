# =====================================================
# yogurt_model.py
#
# Improved yogurt fermentation model
#
# Includes:
# - Monod substrate limitation
# - Temperature effect
# - pH inhibition
# - Biomass growth
# - Lactose consumption
# - Acid production
# =====================================================


import numpy as np

from scipy.integrate import solve_ivp



# =====================================================
# Temperature Effect
# =====================================================

def temperature_factor(
        T,
        Topt,
        sigma
):

    """
    Gaussian temperature response.

    T in Celsius
    """


    return np.exp(
        -(
            (T-Topt)**2
        )
        /
        (2*sigma**2)
    )



# =====================================================
# pH Effect
# =====================================================

def pH_factor(
        pH,
        pHopt
):

    """
    Growth inhibition by acidity.
    """


    return (
        1
        /
        (
            1
            +
            10**(pHopt-pH)
        )
    )



# =====================================================
# Growth Rate
# =====================================================

def growth_rate(
        S,
        pH,
        T,
        mumax,
        Ks,
        Topt,
        sigma,
        pHopt
):


    substrate_factor = (
        S
        /
        (Ks+S)
    )


    temp_factor = temperature_factor(
        T,
        Topt,
        sigma
    )


    acid_factor = pH_factor(
        pH,
        pHopt
    )


    return (
        mumax
        *
        substrate_factor
        *
        temp_factor
        *
        acid_factor
    )



# =====================================================
# Yogurt Fermentation
# =====================================================

def yogurt_fermentation(

        X0,
        S0,
        P0,

        fermentation_time,

        mumax,
        Ks,

        Yxs,
        Ypx,

        temperature,

        Topt,
        sigma,

        pH0,
        pHopt

):


    """
    Differential equations:

    dX/dt = μX

    dS/dt = -(1/Yxs)μX

    dP/dt = Ypx μX

    """



    def model(t,y):


        X = y[0]

        S = y[1]

        P = y[2]



        # pH calculation

        pH = (
            pH0
            -
            0.15*P
        )


        mu = growth_rate(

            S,

            pH,

            temperature,

            mumax,

            Ks,

            Topt,

            sigma,

            pHopt

        )



        dXdt = mu*X


        dSdt = (
            -1/Yxs
            *
            mu
            *
            X
        )


        dPdt = (
            Ypx
            *
            mu
            *
            X
        )


        return [

            dXdt,

            dSdt,

            dPdt

        ]



    solution = solve_ivp(

        model,

        (0, fermentation_time),

        [
            X0,
            S0,
            P0
        ],

        t_eval=np.linspace(
            0,
            fermentation_time,
            300
        )

    )


    return solution
