# =====================================================
# Ferment me, Bobteria!
#
# yogurtplot.py
#
# Visualization tools for yogurt fermentation.
#
# Author: LawrenceJane
# =====================================================

import numpy as np 
import matplotlib.pyplot as plt

# =====================================================
# Experimental Validation Data
# =====================================================

experimental_time = np.array([0, 2, 4, 6, 8])

experimental_pH = np.array([
    6.51,
    6.50,
    5.30,
    4.50,
    4.45
])

# =====================================================
# pH Validation
# =====================================================

def calculate_pH_RMSE(time, pH):

    model_pH = np.interp(
        experimental_time,
        time,
        pH
    )

    errors = model_pH - experimental_pH

    rmse = np.sqrt(
        np.mean(
            errors ** 2
        )
    )

    print("\n========== pH Validation ==========")

    for t, exp, model, error in zip(
        experimental_time,
        experimental_pH,
        model_pH,
        errors
    ):
        print(
            f"{t:.0f} h | "
            f"Experimental: {exp:.2f} | "
            f"Model: {model:.2f} | "
            f"Error: {error:+.2f}"
        )

    print(f"\nRMSE: {rmse:.3f} pH units")

    return rmse

# =====================================================
# Fermentation Dashboard
# =====================================================

def plot_results(results):
    """
    Display fermentation dashboard.
    """

    time = results["time"]

    Xs = results["Xs"]

    Xl = results["Xl"]

    lactose = results["lactose"]

    acid = results["acid"]

    pH = results["pH"]

    pH_RMSE = calculate_pH_RMSE(
        time,
        pH
    )


    fig = plt.figure(
        figsize=(14,9)
    )

    gs = fig.add_gridspec(
        3,
        2,
        height_ratios=[1,1,0.55]
    )

    fig.suptitle(
        "Ferment me, Bobteria! Dashboard",
        fontsize=18,
        fontweight="bold"
    )


    # =================================================
    # Growth
    # =================================================

    ax1 = fig.add_subplot(gs[0,0])

    ax1.plot(
        time,
        Xs,
        linewidth=2,
        label="S. thermophilus"
    )

    ax1.plot(
        time,
        Xl,
        linewidth=2,
        label="L. bulgaricus"
    )

    ax1.set_title("Starter Culture Growth")

    ax1.set_xlabel("Time (hours)")

    ax1.set_ylabel("Biomass (g/L)")

    ax1.legend()

    ax1.grid(True)


    # =================================================
    # Lactose
    # =================================================

    ax2 = fig.add_subplot(gs[0,1])

    ax2.plot(
        time,
        lactose,
        linewidth=2,
        color="orange"
    )

    ax2.set_title("Lactose Consumption")

    ax2.set_xlabel("Time (hours)")

    ax2.set_ylabel("Lactose (g/L)")

    ax2.grid(True)


    # =================================================
    # Acid
    # =================================================

    ax3 = fig.add_subplot(gs[1,0])

    ax3.plot(
        time,
        acid,
        linewidth=2,
        color="red"
    )

    ax3.set_title("Lactic Acid Production")

    ax3.set_xlabel("Time (hours)")

    ax3.set_ylabel("Lactic Acid (g/L)")

    ax3.grid(True)


    # =================================================
    # pH
    # =================================================

    ax4 = fig.add_subplot(gs[1,1])

    # Model
    ax4.plot(
        time,
        pH,
        linewidth=2,
        color="green",
        label="Model"
    )

    # Experimental data
    ax4.scatter(
        experimental_time,
        experimental_pH,
        color="black",
        s=45,
        zorder=5,
        label="Experimental"
    )

    ax4.set_title("pH Evolution")

    ax4.set_xlabel("Time (hours)")

    ax4.set_ylabel("pH")

    ax4.invert_yaxis()

    ax4.legend()

    ax4.grid(True)



    # =================================================
    # Summary Panel
    # =================================================

    ax5 = fig.add_subplot(gs[2,:])

    ax5.axis("off")

    summary = f"""
Simulation Summary

Final S. thermophilus : {Xs[-1]:.3f} g/L
Final L. bulgaricus   : {Xl[-1]:.3f} g/L
Remaining Lactose     : {lactose[-1]:.3f} g/L
Lactic Acid Produced  : {acid[-1]:.3f} g/L
Final pH              : {pH[-1]:.2f}
Fermentation Time     : {time[-1]:.2f} hours
pH RMSE               : {pH_RMSE:.3f}
"""

    ax5.text(
        0.02,
        0.95,
        summary,
        fontsize=11,
        family="monospace",
        verticalalignment="top",
        bbox=dict(
            facecolor="whitesmoke",
            edgecolor="black",
            boxstyle="round,pad=0.7"
        )
    )


    plt.tight_layout()

    plt.show()
