# =====================================================
# Ferment me, Bobteria!
#
# yogurtparameters.py
#
# Parameter Input
#
# Provides a complete parameter dictionary for the
# current two-species co-culture model.
# =====================================================

import yogurtconstant


# =====================================================
# Get Parameters
# =====================================================

def get_parameters():

    print("\n========== Initial Conditions ==========")

    params = {}

    # -------------------------------------------------
    # Initial Conditions
    # -------------------------------------------------

    params["Xs0"] = float(
        input(
            "Initial S. thermophilus biomass (g/L): "
        )
    )

    params["Xl0"] = float(
        input(
            "Initial L. bulgaricus biomass (g/L): "
        )
    )

    params["S0"] = float(
        input(
            "Initial lactose concentration (g/L): "
        )
    )

    params["P0"] = float(
        input(
            "Initial lactic acid concentration (g/L): "
        )
    )

    params["fermentation_time"] = float(
        input(
            "Fermentation time (hours): "
        )
    )


    # =================================================
    # Parameter Source
    # =================================================

    print("\n========== Parameter Source ==========")

    print("1. Use literature parameters")
    print("2. Enter custom parameters")

    parameter_choice = input(
        "\nChoice: "
    )


    # =================================================
    # Literature Parameters
    # =================================================

    if parameter_choice == "1":

        print("\nLoading literature parameters...")

        # ---------------------------------------------
        # S. thermophilus
        # ---------------------------------------------

        params["mumax_s"] = yogurtconstant.MU_MAX_S

        params["Ks_s"] = yogurtconstant.KS_S

        params["Ys"] = yogurtconstant.YS

        params["Yps"] = yogurtconstant.ACID_YIELD_S

        params["Topt_s"] = yogurtconstant.TOPT_S

        params["pHopt_s"] = yogurtconstant.PHOPT_S

        # ---------------------------------------------
        # L. bulgaricus
        # ---------------------------------------------

        params["mumax_l"] = yogurtconstant.MU_MAX_L

        params["Ks_l"] = yogurtconstant.KS_L

        params["Yl"] = yogurtconstant.YL

        params["Ypl"] = yogurtconstant.ACID_YIELD_L

        params["Topt_l"] = yogurtconstant.TOPT_L

        params["pHopt_l"] = yogurtconstant.PHOPT_L


        # ---------------------------------------------
        # Model Parameters
        # ---------------------------------------------

        params["BETA"] = yogurtconstant.BETA

        print(
            "\nLiterature parameters loaded."
        )


    # =================================================
    # Custom Parameters
    # =================================================

    elif parameter_choice == "2":

        print(
            "\n========== S. thermophilus =========="
        )

        params["mumax_s"] = float(
            input("Maximum growth rate (h^-1): ")
        )

        params["Ks_s"] = float(
            input("Monod constant Ks (g/L): ")
        )

        params["Ys"] = float(
            input("Biomass yield (g/g): ")
        )

        params["Yps"] = float(
            input("Acid yield: ")
        )

        params["Topt_s"] = float(
            input("Optimal temperature (°C): ")
        )

        params["pHopt_s"] = float(
            input("Optimal pH: ")
        )


        print(
            "\n========== L. bulgaricus =========="
        )

        params["mumax_l"] = float(
            input("Maximum growth rate (h^-1): ")
        )

        params["Ks_l"] = float(
            input("Monod constant Ks (g/L): ")
        )

        params["Yl"] = float(
            input("Biomass yield (g/g): ")
        )

        params["Ypl"] = float(
            input("Acid yield: ")
        )

        params["Topt_l"] = float(
            input("Optimal temperature (°C): ")
        )

        params["pHopt_l"] = float(
            input("Optimal pH: ")
        )


        print(
            "\n========== pH Model =========="
        )

        params["BETA"] = float(
            input(
                "Buffering capacity BETA "
                "(g/L/pH): "
            )
        )


    else:

        print(
            "\nInvalid choice."
        )

        return None


    # =================================================
    # Environment
    # =================================================

    print(
        "\n========== Environment =========="
    )

    params["temperature"] = float(
        input(
            "Temperature (°C): "
        )
    )

    params["sigma"] = float(
        input(
            "Temperature tolerance (°C): "
        )
    )

    # Fixed model parameter
    params["sigma_pH"] = 1.2

    params["pH0"] = float(
        input(
            "Initial pH: "
        )
    )


    # =================================================
    # Interaction Parameters
    # =================================================

    print(
        "\n========== Interaction Parameters =========="
    )

    params["Ki"] = float(
        input(
            "Lactic acid inhibition constant (g/L): "
        )
    )

    params["alpha_s"] = float(
        input(
            "Symbiosis coefficient for S. thermophilus: "
        )
    )

    params["alpha_l"] = float(
        input(
            "Symbiosis coefficient for L. bulgaricus: "
        )
    )


    # =================================================
    # pH Floor
    # =================================================

    params["pH_min"] = 3.5


    # =================================================
    # Validation
    # =================================================

    print(
        "\nParameters successfully loaded."
    )

    return params
