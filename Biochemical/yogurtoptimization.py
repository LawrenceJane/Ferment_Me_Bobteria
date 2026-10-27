# =====================================================
# Ferment me, Bobteria!
#
# yogurtoptimization.py
#
# Experiment Laboratory
#
# Version 1.0
# =====================================================

import copy
import time

import numpy as np
import matplotlib.pyplot as plt

from yogurtsimulator import run_simulation
from yogurtparameters import get_parameters


# =====================================================
# Progress Bar
# =====================================================

def show_progress(
    current,
    total,
    experiment,
    current_value=""
):
    """
    Display experiment progress.
    """

    percent = int(
        current / total * 100
    )

    bar_length = 30

    filled = int(
        bar_length * current / total
    )

    bar = (
        "█" * filled
        +
        "░" * (
            bar_length
            -
            filled
        )
    )

    print("\033c", end="")

    print("=" * 55)
    print("        Ferment me, Bobteria!")
    print("         Experiment Laboratory")
    print("=" * 55)

    print()

    print(
        f"Experiment : {experiment}"
    )

    if current_value != "":
        print(
            f"Current    : {current_value}"
        )

    print()

    print(
        f"Simulation : {current}/{total}"
    )

    print()

    print(
        f"[{bar}] {percent}%"
    )

    print()

    if current == total:
        print(
            "Experiment Complete!"
        )


# =====================================================
# Optimization Objective
# =====================================================

def choose_objective():
    """
    Ask the user which quantity
    should be optimized.
    """

    print()
    print("=" * 55)
    print("Optimization Objective")
    print("=" * 55)

    print("1. Maximum Biomass")
    print("2. Maximum Lactic Acid")
    print("3. Lowest Final pH")
    print("4. Minimum Remaining Lactose")
    print("5. Balanced Performance")

    print()

    choice = input(
        "Choice: "
    )

    return choice


# =====================================================
# Balanced Performance Score
# =====================================================

def balanced_score(
    biomass,
    acid,
    pH,
    lactose
):
    """
    Calculate a balanced
    performance score.
    """

    biomass = biomass / np.max(
        biomass
    )

    acid = acid / np.max(
        acid
    )

    pH = 1 - (
        pH / np.max(pH)
    )

    lactose = 1 - (
        lactose
        /
        np.max(lactose)
    )

    score = (
        0.35 * biomass
        +
        0.35 * acid
        +
        0.15 * pH
        +
        0.15 * lactose
    )

    return score


# =====================================================
# Best Experiment Finder
# =====================================================

def find_best_index(
    results,
    objective
):
    """
    Return the index of the best
    experiment according to the
    selected objective.
    """

    if objective == "1":

        return np.argmax(
            results["biomass"]
        )

    elif objective == "2":

        return np.argmax(
            results["acid"]
        )

    elif objective == "3":

        return np.argmin(
            results["pH"]
        )

    elif objective == "4":

        return np.argmin(
            results["remaining_lactose"]
        )

    elif objective == "5":

        score = balanced_score(
            results["biomass"],
            results["acid"],
            results["pH"],
            results["remaining_lactose"]
        )

        return np.argmax(
            score
        )

    else:

        raise ValueError(
            "Invalid optimization objective."
        )


# =====================================================
# Laboratory Plot
# =====================================================

def laboratory_plot(
    x,
    y,
    xlabel,
    ylabel,
    title,
    marker="o"
):
    """
    Standard laboratory plot.
    """

    plt.figure(
        figsize=(9, 5)
    )

    plt.plot(
        x,
        y,
        marker=marker,
        linewidth=2
    )

    plt.title(
        title
    )

    plt.xlabel(
        xlabel
    )

    plt.ylabel(
        ylabel
    )

    plt.grid(True)

    plt.tight_layout()

    plt.show()


# =====================================================
# Experiment Dashboard
# =====================================================

def experiment_dashboard(
    results,
    objective
):
    """
    Display experiment results
    in a dashboard.
    """

    best = find_best_index(
        results,
        objective
    )

    x = results["x"]

    xlabel = results["xlabel"]

    biomass = results["biomass"]

    acid = results["acid"]

    pH = results["pH"]

    lactose = results["remaining_lactose"]

    fig, ax = plt.subplots(
        2,
        2,
        figsize=(12, 8)
    )

    # ------------------------------------------
    # Biomass
    # ------------------------------------------

    ax[0, 0].plot(
        x,
        biomass,
        marker="o"
    )

    ax[0, 0].set_title(
        "Final Biomass"
    )

    ax[0, 0].set_xlabel(
        xlabel
    )

    ax[0, 0].set_ylabel(
        "g/L"
    )

    ax[0, 0].grid(True)

    ax[0, 0].scatter(
        x[best],
        biomass[best],
        s=80
    )

    # ------------------------------------------
    # Acid
    # ------------------------------------------

    ax[0, 1].plot(
        x,
        acid,
        marker="s"
    )

    ax[0, 1].set_title(
        "Lactic Acid"
    )

    ax[0, 1].set_xlabel(
        xlabel
    )

    ax[0, 1].set_ylabel(
        "g/L"
    )

    ax[0, 1].grid(True)

    ax[0, 1].scatter(
        x[best],
        acid[best],
        s=80
    )

    # ------------------------------------------
    # Final pH
    # ------------------------------------------

    ax[1, 0].plot(
        x,
        pH,
        marker="^"
    )

    ax[1, 0].set_title(
        "Final pH"
    )

    ax[1, 0].set_xlabel(
        xlabel
    )

    ax[1, 0].set_ylabel(
        "pH"
    )

    ax[1, 0].grid(True)

    ax[1, 0].scatter(
        x[best],
        pH[best],
        s=80
    )

    # ------------------------------------------
    # Summary
    # ------------------------------------------

    ax[1, 1].axis("off")

    summary = (
        "Recommended Condition\n\n"

        f"{xlabel}: "
        f"{x[best]}\n\n"

        f"Biomass\n"
        f"{biomass[best]:.3f} g/L\n\n"

        f"Lactic Acid\n"
        f"{acid[best]:.3f} g/L\n\n"

        f"Remaining Lactose\n"
        f"{lactose[best]:.3f} g/L\n\n"

        f"Final pH\n"
        f"{pH[best]:.2f}"
    )

    ax[1, 1].text(
        0,
        1,
        summary,
        fontsize=11,
        va="top"
    )

    fig.suptitle(
        "Experiment Dashboard",
        fontsize=16
    )

    plt.tight_layout()

    plt.show()


# =====================================================
# Temperature Sweep
# =====================================================

def temperature_sweep(
    params,
    objective
):
    """
    Perform a temperature sweep.
    """

    Tmin = float(
        input(
            "\nMinimum Temperature (°C): "
        )
    )

    Tmax = float(
        input(
            "Maximum Temperature (°C): "
        )
    )

    step = float(
        input(
            "Temperature Step (°C): "
        )
    )

    temperatures = np.arange(
        Tmin,
        Tmax + step,
        step
    )

    biomass = []

    acid = []

    pH = []

    remaining_lactose = []

    total = len(
        temperatures
    )

    for i, T in enumerate(
        temperatures
    ):

        experiment = copy.deepcopy(
            params
        )

        experiment["temperature"] = T

        results = run_simulation(
            experiment
        )

        biomass.append(
            results["Xs"][-1]
            +
            results["Xl"][-1]
        )

        acid.append(
            results["acid"][-1]
        )

        pH.append(
            results["pH"][-1]
        )

        remaining_lactose.append(
            results["lactose"][-1]
        )

        show_progress(
            i + 1,
            total,
            "Temperature Sweep",
            f"{T:.1f} °C"
        )

        time.sleep(
            0.03
        )

    sweep_results = {
        "x": temperatures,

        "xlabel": "Temperature (°C)",

        "biomass": np.array(
            biomass
        ),

        "acid": np.array(
            acid
        ),

        "pH": np.array(
            pH
        ),

        "remaining_lactose": np.array(
            remaining_lactose
        )
    }

    experiment_dashboard(
        sweep_results,
        objective
    )

    return sweep_results


# =====================================================
# Starter Ratio Sweep
# =====================================================

def starter_ratio_sweep(
    params,
    objective
):
    """
    Perform a starter ratio sweep.
    """

    # Keep total initial starter biomass constant
    total_biomass = (
        params["Xs0"]
        +
        params["Xl0"]
    )

    ratios = [
        (1, 1),
        (2, 1),
        (3, 1),
        (4, 1),
        (1, 2),
        (1, 3),
        (1, 4)
    ]

    biomass = []

    acid = []

    pH = []

    remaining_lactose = []

    labels = []

    total = len(
        ratios
    )

    for i, (s_ratio, l_ratio) in enumerate(
        ratios
    ):

        experiment = copy.deepcopy(
            params
        )

        ratio_total = (
            s_ratio
            +
            l_ratio
        )

        experiment["Xs0"] = (
            total_biomass
            *
            s_ratio
            /
            ratio_total
        )

        experiment["Xl0"] = (
            total_biomass
            *
            l_ratio
            /
            ratio_total
        )

        results = run_simulation(
            experiment
        )

        labels.append(
            f"{s_ratio}:{l_ratio}"
        )

        biomass.append(
            results["Xs"][-1]
            +
            results["Xl"][-1]
        )

        acid.append(
            results["acid"][-1]
        )

        pH.append(
            results["pH"][-1]
        )

        remaining_lactose.append(
            results["lactose"][-1]
        )

        show_progress(
            i + 1,
            total,
            "Starter Ratio Sweep",
            f"{s_ratio}:{l_ratio}"
        )

        time.sleep(
            0.03
        )

    sweep_results = {
        "x": labels,

        "xlabel": "Starter Ratio",

        "biomass": np.array(
            biomass
        ),

        "acid": np.array(
            acid
        ),

        "pH": np.array(
            pH
        ),

        "remaining_lactose": np.array(
            remaining_lactose
        )
    }

    experiment_dashboard(
        sweep_results,
        objective
    )

    return sweep_results


# =====================================================
# Lactose Sweep
# =====================================================

def lactose_sweep(
    params,
    objective
):
    """
    Perform a lactose sweep.
    """

    minimum = float(
        input(
            "\nMinimum Lactose (g/L): "
        )
    )

    maximum = float(
        input(
            "Maximum Lactose (g/L): "
        )
    )

    step = float(
        input(
            "Step (g/L): "
        )
    )

    lactose_levels = np.arange(
        minimum,
        maximum + step,
        step
    )

    biomass = []

    acid = []

    pH = []

    remaining_lactose = []

    total = len(
        lactose_levels
    )

    for i, value in enumerate(
        lactose_levels
    ):

        experiment = copy.deepcopy(
            params
        )

        experiment["S0"] = value

        results = run_simulation(
            experiment
        )

        biomass.append(
            results["Xs"][-1]
            +
            results["Xl"][-1]
        )

        acid.append(
            results["acid"][-1]
        )

        pH.append(
            results["pH"][-1]
        )

        remaining_lactose.append(
            results["lactose"][-1]
        )

        show_progress(
            i + 1,
            total,
            "Lactose Sweep",
            f"{value:.1f} g/L"
        )

        time.sleep(
            0.03
        )

    sweep_results = {
        "x": lactose_levels,

        "xlabel": "Initial Lactose (g/L)",

        "biomass": np.array(
            biomass
        ),

        "acid": np.array(
            acid
        ),

        "pH": np.array(
            pH
        ),

        "remaining_lactose": np.array(
            remaining_lactose
        )
    }

    experiment_dashboard(
        sweep_results,
        objective
    )

    return sweep_results


# =====================================================
# Initial pH Sweep
# =====================================================

def pH_sweep(
    params,
    objective
):
    """
    Perform an initial pH sweep.
    """

    minimum = float(
        input(
            "\nMinimum Initial pH: "
        )
    )

    maximum = float(
        input(
            "Maximum Initial pH: "
        )
    )

    step = float(
        input(
            "Step: "
        )
    )

    pH_values = np.arange(
        minimum,
        maximum + step,
        step
    )

    biomass = []

    acid = []

    final_pH = []

    remaining_lactose = []

    total = len(
        pH_values
    )

    for i, value in enumerate(
        pH_values
    ):

        experiment = copy.deepcopy(
            params
        )

        experiment["pH0"] = value

        results = run_simulation(
            experiment
        )

        biomass.append(
            results["Xs"][-1]
            +
            results["Xl"][-1]
        )

        acid.append(
            results["acid"][-1]
        )

        final_pH.append(
            results["pH"][-1]
        )

        remaining_lactose.append(
            results["lactose"][-1]
        )

        show_progress(
            i + 1,
            total,
            "Initial pH Sweep",
            f"{value:.2f}"
        )

        time.sleep(
            0.03
        )

    sweep_results = {
        "x": pH_values,

        "xlabel": "Initial pH",

        "biomass": np.array(
            biomass
        ),

        "acid": np.array(
            acid
        ),

        "pH": np.array(
            final_pH
        ),

        "remaining_lactose": np.array(
            remaining_lactose
        )
    }

    experiment_dashboard(
        sweep_results,
        objective
    )

    return sweep_results


# =====================================================
# Experiment Report
# =====================================================

def experiment_report(
    name,
    results,
    objective
):
    """
    Print experiment summary.
    """

    best = find_best_index(
        results,
        objective
    )

    print()

    print("=" * 55)

    print("Experiment Summary")

    print("=" * 55)

    print()

    print(
        f"Experiment : {name}"
    )

    print()

    print(
        f"Recommended {results['xlabel']}: "
        f"{results['x'][best]}"
    )

    print()

    print(
        f"Final Biomass : "
        f"{results['biomass'][best]:.3f} g/L"
    )

    print(
        f"Lactic Acid   : "
        f"{results['acid'][best]:.3f} g/L"
    )

    print(
        f"Remaining Lactose : "
        f"{results['remaining_lactose'][best]:.3f} g/L"
    )

    print(
        f"Final pH : "
        f"{results['pH'][best]:.2f}"
    )

    print()

    print("=" * 55)


# =====================================================
# Run All Experiments
# =====================================================

def run_all_experiments(
    params
):
    """
    Run every optimization experiment.
    """

    objective = choose_objective()

    print(
        "\nRunning Temperature Sweep..."
    )

    temperature = temperature_sweep(
        params,
        objective
    )

    experiment_report(
        "Temperature Sweep",
        temperature,
        objective
    )

    input(
        "\nPress Enter..."
    )

    print(
        "\nRunning Starter Ratio Sweep..."
    )

    starter = starter_ratio_sweep(
        params,
        objective
    )

    experiment_report(
        "Starter Ratio Sweep",
        starter,
        objective
    )

    input(
        "\nPress Enter..."
    )

    print(
        "\nRunning Lactose Sweep..."
    )

    lactose = lactose_sweep(
        params,
        objective
    )

    experiment_report(
        "Lactose Sweep",
        lactose,
        objective
    )

    input(
        "\nPress Enter..."
    )

    print(
        "\nRunning Initial pH Sweep..."
    )

    pH = pH_sweep(
        params,
        objective
    )

    experiment_report(
        "Initial pH Sweep",
        pH,
        objective
    )

    input(
        "\nPress Enter..."
    )

    return {
        "temperature": temperature,

        "starter": starter,

        "lactose": lactose,

        "pH": pH
    }


# =====================================================
# Optimization Laboratory
# =====================================================

def optimization_menu():
    """
    Experiment laboratory.
    """

    print(
        "\n========== Base Fermentation Parameters =========="
    )

    print(
        "These parameters will be used as the baseline"
    )

    print(
        "for every optimization experiment.\n"
    )

    params = get_parameters()

    while True:

        print()

        print("=" * 55)

        print("Optimization Laboratory")

        print("=" * 55)

        print("1. Temperature Sweep")

        print("2. Starter Ratio Sweep")

        print("3. Lactose Sweep")

        print("4. Initial pH Sweep")

        print("5. Run All Experiments")

        print("6. Return")

        choice = input(
            "\nChoice: "
        )

        if choice == "1":

            objective = choose_objective()

            results = temperature_sweep(
                params,
                objective
            )

            experiment_report(
                "Temperature Sweep",
                results,
                objective
            )

            input(
                "\nPress Enter to continue..."
            )

        elif choice == "2":

            objective = choose_objective()

            results = starter_ratio_sweep(
                params,
                objective
            )

            experiment_report(
                "Starter Ratio Sweep",
                results,
                objective
            )

            input(
                "\nPress Enter to continue..."
            )

        elif choice == "3":

            objective = choose_objective()

            results = lactose_sweep(
                params,
                objective
            )

            experiment_report(
                "Lactose Sweep",
                results,
                objective
            )

            input(
                "\nPress Enter to continue..."
            )

        elif choice == "4":

            objective = choose_objective()

            results = pH_sweep(
                params,
                objective
            )

            experiment_report(
                "Initial pH Sweep",
                results,
                objective
            )

            input(
                "\nPress Enter to continue..."
            )

        elif choice == "5":

            run_all_experiments(
                params
            )

            input(
                "\nPress Enter to continue..."
            )

        elif choice == "6":

            break

        else:

            print(
                "\nInvalid choice."
            )