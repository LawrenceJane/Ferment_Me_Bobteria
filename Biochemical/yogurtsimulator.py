# =====================================================
# Ferment me, Bobteria!
#
# yogurtsimulator.py
#
# Simulation engine for yogurt fermentation.
#
# Runs the mathematical model and packages the
# simulation results.
#
# Author: LawrenceJane
# =====================================================

import numpy as np

from yogurtcoculture import yogurt_coculture

# =====================================================
# Run Simulation
# =====================================================

def run_simulation(params):
    """
    Runs the yogurt fermentation simulation.

    Parameters
    ----------
    params : dict
        Dictionary containing all model parameters.

    Returns
    -------
    dict
        Simulation results.
    """

    # -------------------------------------------------
    # Run model
    # -------------------------------------------------

    solution = yogurt_coculture(

    params["Xs0"],
    params["Xl0"],

    params["S0"],
    params["P0"],

    params["fermentation_time"],

    params["mumax_s"],
    params["Ks_s"],

    params["mumax_l"],
    params["Ks_l"],

    params["Ys"],
    params["Yl"],

    params["Yps"],
    params["Ypl"],

    params["temperature"],

    params["Topt_s"],
    params["Topt_l"],

    params["sigma"],
    params["sigma_pH"],

    params["pH0"],

    params["pHopt_s"],
    params["pHopt_l"],

    params["Ki"],

    params["BETA"],

    params["alpha_s"],
    params["alpha_l"],

    params["symbiosis_st"],
    params["symbiosis_lb"]
    
    )

    # -------------------------------------------------
    # Extract Results
    # -------------------------------------------------

    time = solution.t

    Xs = solution.y[0]

    Xl = solution.y[1]

    lactose = solution.y[2]

    lactose = np.maximum(
    solution.y[2],
    0
    )

    acid = solution.y[3]

    acid = np.maximum(
    solution.y[3],
    0
    )

    # -------------------------------------------------
    # Estimate pH
    # -------------------------------------------------

    pH = params["pH0"] - 0.15 * acid

    pH = np.maximum(
        pH,
        params["pH_min"]
    )
    # -------------------------------------------------
    # Package Results
    # -------------------------------------------------

    results = {

        "time": time,

        "Xs": Xs,

        "Xl": Xl,

        "lactose": lactose,

        "acid": acid,

        "pH": pH,

        "solution": solution,

        "params": params

    }

    return results