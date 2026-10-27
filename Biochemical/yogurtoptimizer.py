# =====================================================
# Ferment me, Bobteria!
#
# yogurtoptimizer.py
#
# Automatic optimization engine
#
# Uses the current two-species co-culture model.
# =====================================================

import numpy as np

from scipy.optimize import minimize_scalar

from yogurtcoculture import yogurt_coculture


# =====================================================
# Find Fermentation Time
# =====================================================

def find_target_time(
        hours,
        pH,
        target=4.5
):
    """
    Find the first time at which the modeled pH
    reaches or falls below the target pH.

    Parameters
    ----------
    hours : array
        Simulation time in hours.

    pH : array
        Modeled pH values.

    target : float
        Target pH.

    Returns
    -------
    float
        Time required to reach target pH.
        Returns np.inf if target is not reached.
    """

    for i in range(len(pH)):

        if pH[i] <= target:

            return hours[i]

    return np.inf


# =====================================================
# Run Current Model
# =====================================================

def run_model(parameters, Xs0=None, Xl0=None, temperature=None):
    """
    Run the current yogurt co-culture model.

    Optional Xs0, Xl0, and temperature values can be
    supplied for optimization experiments.
    """

    if Xs0 is None:
        Xs0 = parameters["Xs0"]

    if Xl0 is None:
        Xl0 = parameters["Xl0"]

    if temperature is None:
        temperature = parameters["temperature"]

    return yogurt_coculture(

        Xs0,
        Xl0,

        parameters["S0"],
        parameters["P0"],

        parameters["fermentation_time"],

        parameters["mumax_s"],
        parameters["Ks_s"],

        parameters["mumax_l"],
        parameters["Ks_l"],

        parameters["Ys"],
        parameters["Yl"],

        parameters["Yps"],
        parameters["Ypl"],

        temperature,

        parameters["Topt_s"],
        parameters["Topt_l"],

        parameters["sigma"],

        parameters["sigma_pH"],

        parameters["pH0"],

        parameters["pHopt_s"],
        parameters["pHopt_l"],

        parameters["Ki"],

        parameters["BETA"],

        parameters["alpha_s"],
        parameters["alpha_l"],

        parameters["pH_min"]
    )


# =====================================================
# Temperature Optimization
# =====================================================

def optimize_temperature(parameters):

    def objective(T):

        result = run_model(
            parameters,
            temperature=T
        )

        acid = result.y[3]

        # Current model calculates pH internally.
        pH = result.y[4]

        hours = result.t

        return find_target_time(
            hours,
            pH
        )

    result = minimize_scalar(

        objective,

        bounds=(30, 50),

        method="bounded"

    )

    return result.x, result.fun


# =====================================================
# Starter Ratio Optimization
# =====================================================

def optimize_ratio(
        parameters,
        total_biomass
):
    """
    Optimize the initial S. thermophilus /
    L. bulgaricus biomass ratio.

    total_biomass is kept constant.
    """

    def objective(ratio):

        Xs = (
            total_biomass
            *
            ratio
            /
            (ratio + 1)
        )

        Xl = (
            total_biomass
            /
            (ratio + 1)
        )

        result = run_model(

            parameters,

            Xs0=Xs,

            Xl0=Xl

        )

        pH = result.y[4]

        hours = result.t

        return find_target_time(
            hours,
            pH
        )

    result = minimize_scalar(

        objective,

        bounds=(0.1, 10),

        method="bounded"

    )

    return result.x, result.fun