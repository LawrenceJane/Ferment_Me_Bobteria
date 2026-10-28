# =====================================================
# Ferment me, Bobteria!
#
# yogurtferment.py
#
# Main program for yogurt fermentation simulation.
#
# Author: LawrenceJane
# =====================================================

from yogurtsimulator import run_simulation
from yogurtplot import plot_results
from yogurtsave import save_results
from yogurtoptimization import optimization_menu
from yogurtparameters import get_parameters

print("START")

# =====================================================
# Header
# =====================================================

def title():

    print("=" * 60)
    print("          Ferment me, Bobteria! 🧫")
    print("      'Where tiny bacteria make big yogurt.'")
    print("=" * 60)


# =====================================================
# New Experiment
# =====================================================

def new_experiment():

    params = get_parameters()

    print("\nRunning fermentation...\n")

    results = run_simulation(params)

    print("=" * 50)
    print("Simulation Complete")
    print("=" * 50)

    print(
        f"Final S. thermophilus : "
        f"{results['Xs'][-1]:.3f} g/L"
    )

    print(
        f"Final L. bulgaricus  : "
        f"{results['Xl'][-1]:.3f} g/L"
    )

    print(
        f"Remaining Lactose    : "
        f"{results['lactose'][-1]:.3f} g/L"
    )

    print(
        f"Lactic Acid          : "
        f"{results['acid'][-1]:.3f} g/L"
    )

    print(
        f"Final pH             : "
        f"{results['pH'][-1]:.2f}"
    )

    plot_results(results)

    print()

    print("=" * 40)
    print("Save Results?")
    print("=" * 40)

    print("1. Yes")
    print("2. No")

    save_choice = input("\nChoice: ")

    if save_choice == "1":

        save_results(results)

    elif save_choice == "2":

        print("\nResults not saved.")

    else:

        print("\nInvalid choice.")
        print("Results not saved.")

    input("\nPress Enter to continue...")

# =====================================================
# Menu
# =====================================================

def menu():

    print("          Ferment me, Bobteria! 🧫")
    print("      '100% organic. 0% FDA approval.'")

    print("1. New Fermentation")
    print("2. Optimization")
    print("3. Exit")

    return input("\nChoice: ")


# =====================================================
# Goodbye
# =====================================================

def goodbye():

    print()

    print("Bob wishes you safety.")

    print("For the next 24 hours.")

    print("After that, you're on your own.")

    print()


# =====================================================
# Main
# =====================================================

# =====================================================
# Main
# =====================================================

def main():

    while True:

        choice = menu()

        if choice == "1":

            new_experiment()

        elif choice == "2":

            optimization_menu()

        elif choice == "3":

            goodbye()
            break

        else:

            print("\nInvalid choice.")


# =====================================================
# Program Entry
# =====================================================

if __name__ == "__main__":
    
    main()
