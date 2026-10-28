# =====================================================
# Ferment me, Bobteria!
#
# yogurtsave.py
#
# Save fermentation results to CSV.
#
# Author: LawrenceJane
# =====================================================

import csv
from datetime import datetime


# =====================================================
# Save Results
# =====================================================

def save_results(results):
    """
    Save fermentation results to CSV.
    """

    params = results["params"]

    time = results["time"]

    Xs = results["Xs"]

    Xl = results["Xl"]

    lactose = results["lactose"]

    acid = results["acid"]

    pH = results["pH"]


    filename = (
        "Fermentation_"
        +
        datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )
        +
        ".csv"
    )


    with open(

        filename,

        "w",

        newline=""

    ) as file:

        writer = csv.writer(file)

        # =============================================
        # Header
        # =============================================

        writer.writerow([
            "Ferment me, Bobteria!"
        ])

        writer.writerow([
            "Simulation Results"
        ])

        writer.writerow([])


        # =============================================
        # Parameters
        # =============================================

        writer.writerow([
            "Simulation Parameters"
        ])

        writer.writerow([
            "Parameter",
            "Value"
        ])

        writer.writerow([
            "Initial S. thermophilus (g/L)",
            params["Xs0"]
        ])

        writer.writerow([
            "Initial L. bulgaricus (g/L)",
            params["Xl0"]
        ])

        writer.writerow([
            "Initial Lactose (g/L)",
            params["S0"]
        ])

        writer.writerow([
            "Initial Lactic Acid (g/L)",
            params["P0"]
        ])

        writer.writerow([
            "Temperature (°C)",
            params["temperature"]
        ])

        writer.writerow([
            "Initial pH",
            params["pH0"]
        ])

        writer.writerow([
            "Fermentation Time (hours)",
            params["fermentation_time"] / 3600
        ])

        writer.writerow([])


        # =============================================
        # Summary
        # =============================================

        writer.writerow([
            "Final Results"
        ])

        writer.writerow([
            "Quantity",
            "Value"
        ])

        writer.writerow([
            "Final S. thermophilus (g/L)",
            Xs[-1]
        ])

        writer.writerow([
            "Final L. bulgaricus (g/L)",
            Xl[-1]
        ])

        writer.writerow([
            "Remaining Lactose (g/L)",
            lactose[-1]
        ])

        writer.writerow([
            "Lactic Acid Produced (g/L)",
            acid[-1]
        ])

        writer.writerow([
            "Final pH",
            pH[-1]
        ])

        writer.writerow([])


        # =============================================
        # Time Series
        # =============================================

        writer.writerow([
            "Time (hours)",
            "S. thermophilus (g/L)",
            "L. bulgaricus (g/L)",
            "Lactose (g/L)",
            "Lactic Acid (g/L)",
            "pH"
        ])


        for i in range(len(time)):

            writer.writerow([

                time[i],

                Xs[i],

                Xl[i],

                lactose[i],

                acid[i],

                pH[i]

            ])


    print()

    print("=" * 45)

    print("Results successfully saved!")

    print(f"File: {filename}")

    print("=" * 45)

    print()
