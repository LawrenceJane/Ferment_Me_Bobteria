# Ferment me, Bobteria!

*A Python-based mathematical simulator of two-species yogurt fermentation.* 
**Author:** Tjiu We Shen
**Language:** Python  
**Core libraries:** NumPy, SciPy, Matplotlib

---

## Overview

**Ferment me, Bobteria!** is a personal scientific modelling project that simulates yogurt fermentation through the interactions of two lactic acid bacteria: *Streptococcus thermophilus* and *Lactobacillus delbrueckii* subsp. *bulgaricus*.

The project combines mathematical modelling, ordinary differential equations (ODEs), and numerical integration to investigate how bacterial growth, substrate consumption, lactic acid production, temperature, and pH interact during fermentation.

Users can explore fermentation under different initial conditions and parameter configurations. The simulator also provides a framework for investigating how changes in operating conditions affect the predicted fermentation process.

The project was developed as an exploration of biochemical engineering, particularly the application of mathematical models to biological processes.

> 100% organic. 0% FDA approval.

*This is an educational simulation, not a validated industrial process model or a tool for food safety assessment.*

## Table of Contents

- [Features](#features)
- [Scientific Background](#scientific-background)
- [Mathematical Model](#mathematical-model)
- [Model Parameters](#model-parameters)
- [Parameter Configuration](#parameter-configuration)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Calibration and Validation](#calibration-and-validation)
- [Assumptions and Limitations](#assumptions-and-limitations)
- [Future Development](#future-development)
- [References](#references)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Features

### Two-species fermentation model

Models the growth of *S. thermophilus* and *L. bulgaricus* within the same fermentation system, allowing their interactions to influence predicted growth.

### Substrate consumption

Tracks lactose consumption associated with bacterial growth through species-specific biomass yields.

### Lactic acid production

Estimates lactic acid accumulation using substrate-consumption rates and species-specific product yields.

### Environmental effects

Incorporates temperature and pH response functions to represent the effects of environmental conditions on bacterial growth.

### Acid inhibition

Includes an inhibition function that reduces the predicted growth rate as lactic acid concentration increases.

### Adjustable fermentation conditions

Allows users to investigate the effects of different initial bacterial populations, lactose and lactic acid concentrations, initial pH, fermentation duration, and model parameters.

### Numerical integration

Uses SciPy's `solve_ivp` to solve the system of ordinary differential equations over the selected fermentation period.

### Parameter calibration and optimisation

Supports exploration of model parameters and operating conditions to investigate their influence on the simulated fermentation process.

---

## Scientific Background

Yogurt fermentation involves the metabolic activity of lactic acid bacteria, which convert fermentable sugars into organic acids and other metabolic products.

Two bacteria commonly associated with yogurt fermentation are:

- ***Streptococcus thermophilus*** — a thermophilic lactic acid bacterium involved in acidification and the early stages of yogurt fermentation.
- ***Lactobacillus delbrueckii* subsp. *bulgaricus*** — a lactic acid bacterium that contributes to acidification and can participate in reciprocal interactions with *S. thermophilus*.

Their interaction is often described as protocooperation or mutualistic cooperation under suitable conditions. Metabolites and growth factors produced or released by one organism can support the growth of the other.

The resulting fermentation process depends on multiple interacting factors, including temperature, nutrient availability, acidity, strain characteristics, and inoculum composition.

*Ferment me, Bobteria!* represents selected aspects of this complex process using a simplified mathematical framework. It is intended to explore relationships between model variables rather than reproduce every biochemical mechanism involved in actual yogurt production.

---

## Mathematical Model

The model represents fermentation using five state variables:

| Symbol | Description |
|---|---|
| \(X_s\) | Biomass concentration of *S. thermophilus* |
| \(X_l\) | Biomass concentration of *L. bulgaricus* |
| \(S\) | Remaining lactose concentration |
| \(P\) | Lactic acid concentration |
| \(pH\) | Modelled pH |

The state variables evolve over time according to a system of ordinary differential equations.

### 1. Substrate-dependent growth

The model uses Monod kinetics to represent the effect of lactose availability on bacterial growth:

\[
\mu(S)=\mu_{\max}\frac{S}{K_s+S}
\]

where:

- \(\mu\) is the substrate-dependent specific growth rate.
- \(\mu_{\max}\) is the maximum specific growth rate.
- \(S\) is the available lactose concentration.
- \(K_s\) is the half-saturation constant.

The growth rate approaches zero as the substrate becomes depleted and approaches its maximum as substrate availability becomes sufficiently high, assuming other factors remain constant.

### 2. Temperature response

Temperature dependence is represented using a Gaussian response function:

\[
f_T=\exp\left[-\frac{(T-T_{\mathrm{opt}})^2}{2\sigma_T^2}\right]
\]

where:

- \(T\) is the fermentation temperature.
- \(T_{\mathrm{opt}}\) is the organism-specific optimum temperature used by the model.
- \(\sigma_T\) controls the width of the response curve.

The function reaches its maximum at the specified optimum temperature and decreases as the temperature moves away from that optimum.

This is a simplified representation of temperature dependence. It does not explicitly model thermal death, heat shock, or changes in cellular physiology.

### 3. pH response

The effect of pH on growth is represented by another Gaussian function:

\[
f_{pH}=\exp\left[-\frac{(pH-pH_{\mathrm{opt}})^2}{2\sigma_{pH}^2}\right]
\]

where:

- \(pH_{\mathrm{opt}}\) is the organism-specific optimum pH.
- \(\sigma_{pH}\) controls the width of the pH response curve.

This function reduces the predicted growth rate as pH deviates from the selected optimum.

### 4. Acid inhibition

The model incorporates lactic acid inhibition through:

\[
f_P=\frac{1}{1+P/K_i}
\]

where \(K_i\) is an inhibition parameter.

As the acid concentration increases, the inhibition factor decreases. This represents the general effect of accumulated acidity on bacterial growth in a simplified form.

The equation does not distinguish between the effects of undissociated lactic acid, lactate ions, and other aspects of the fermentation medium.

### 5. Species interaction

The model includes a linear interaction function:

\[
f_{\mathrm{sym}}=1+\alpha X_{\mathrm{other}}
\]

where:

- \(\alpha\) is the interaction coefficient used in the growth-rate calculation.
- \(X_{\mathrm{other}}\) is the biomass concentration of the other bacterial species.

The function allows the predicted growth rate of one species to depend on the population of the other.

This formulation is a phenomenological approximation. It does not explicitly represent the exchange of specific metabolites, growth factors, or other mechanisms responsible for bacterial cooperation.

### 6. Overall growth rates

The specific growth rates combine the substrate, temperature, pH, acid-inhibition, and species-interaction terms:

\[
\mu_s=
\mu_{\mathrm{Monod},s}
f_{T,s}f_{pH,s}f_Pf_{\mathrm{sym},s}
\]

\[
\mu_l=
\mu_{\mathrm{Monod},l}
f_{T,l}f_{pH,l}f_Pf_{\mathrm{sym},l}
\]

The model uses species-specific growth parameters and optimum conditions.

Any additional species-specific symbiosis multipliers must be interpreted according to their actual implementation in the code; they should not be confused with experimentally established biological constants.

### 7. Biomass growth

The biomass balances are:

\[
\frac{dX_s}{dt}=\mu_sX_s
\]

\[
\frac{dX_l}{dt}=\mu_lX_l
\]

These equations describe biomass growth as a function of the specific growth rate and the current biomass concentration.

### 8. Lactose consumption

Lactose consumption is related to bacterial growth through biomass yields:

\[
r_{S,s}=\frac{\mu_sX_s}{Y_s}
\]

\[
r_{S,l}=\frac{\mu_lX_l}{Y_l}
\]

The total lactose balance is:

\[
\frac{dS}{dt}=-(r_{S,s}+r_{S,l})
\]

where \(Y_s\) and \(Y_l\) represent species-specific biomass yields on the substrate.

### 9. Lactic acid production

Lactic acid production is estimated using product yields:

\[
\frac{dP}{dt}=Y_{ps}r_{S,s}+Y_{pl}r_{S,l}
\]

where \(Y_{ps}\) and \(Y_{pl}\) represent the respective lactic acid production yields associated with lactose consumption.

This assumes a simplified relationship between substrate consumption and acid production. Other metabolic products and competing pathways are not explicitly represented.

### 10. pH evolution

The model uses a simplified relationship between acid production and pH change:

\[
\frac{dpH}{dt}=-\frac{1}{\beta}\frac{dP}{dt}
\]

where \(\beta\) is a model parameter representing the effective resistance of the medium to pH change.

This equation is an approximation. Real pH depends on acid dissociation, buffer composition, protein content, mineral equilibria, and other properties of the fermentation medium.

**Important:** the equation above describes the pH state within the ODE system. Any separate pH calculation used for plotting or validation must be documented independently and checked for consistency with the pH values used to calculate bacterial growth.

---

## Model Parameters

The model uses the following parameter groups.

| Parameter | Description |
|---|---|
| `Xs0`, `Xl0` | Initial biomass concentrations |
| `S0` | Initial lactose concentration |
| `P0` | Initial lactic acid concentration |
| `pH0` | Initial pH |
| `fermentation_time` | Total simulation duration |
| `mumax_s`, `mumax_l` | Maximum specific growth rates |
| `Ks_s`, `Ks_l` | Monod half-saturation constants |
| `Ys`, `Yl` | Biomass yields on lactose |
| `Yps`, `Ypl` | Lactic acid production yields |
| `temperature` | Fermentation temperature |
| `Topt_s`, `Topt_l` | Optimum temperatures |
| `sigma` | Temperature-response width parameter |
| `pHopt_s`, `pHopt_l` | Optimum pH values |
| `sigma_pH` | pH-response width parameter |
| `Ki` | Acid-inhibition parameter |
| `BETA` | Effective pH-response or buffering parameter |
| `alpha_s`, `alpha_l` | Species-interaction coefficients |
| `symbiosis_st`, `symbiosis_lb` | Additional species-specific coefficients, where implemented |

The numerical values, units, sources, and roles of these parameters should be documented alongside the constants or parameter definitions in the source code.

### Parameter provenance

The project distinguishes between three kinds of parameter values:

1. **Literature-derived parameters:** values taken from published research, with citations and any necessary conversions.
2. **Calibrated parameters:** values selected by comparing model predictions against reference observations.
3. **Modelling assumptions:** values used when a directly applicable literature value or measurement is unavailable.

These categories are not interchangeable. A parameter selected to minimise prediction error is not automatically a measured biological constant.

For example, the currently investigated symbiosis coefficients are:

| Parameter | Current calibrated value |
|---|---:|
| `symbiosis_st` | 0.25 |
| `symbiosis_lb` | 0.30 |

These values were selected based on RMSE comparisons among the parameter combinations tested. They should be treated as provisional calibration values, not universal biological constants.

The interpretation of these coefficients depends on how they enter the growth-rate equations. Their units, mathematical role, and effect on growth should be confirmed against the implementation before they are used in scientific comparisons.

---

## Parameter Configuration

The simulator supports two approaches to parameter configuration.

### Literature-based configuration

The simulator supplies its predefined model parameters, allowing users to specify the initial conditions and simulation settings without manually entering every kinetic parameter.

This configuration is intended to make the model easier to use.

Parameters that are not directly supported by applicable literature must still be identified as assumptions or calibrated values. The term *literature-based* does not imply that every number in the model has been independently measured or published.

### Custom configuration

Users can supply their own model parameters to explore alternative assumptions, experimental conditions, or calibration results.

This approach is useful for sensitivity analysis, investigating different kinetic behaviours, and testing how uncertainty in model parameters influences the predicted fermentation process.

When using custom values, users should ensure that units are consistent and that the selected values are appropriate for the equations being evaluated.

---

## Installation

### Requirements

The project uses Python and scientific computing libraries.

- Python 3
- NumPy
- SciPy
- Matplotlib, if using the plotting modules

The model file `yogurtcoculture.py` imports NumPy and SciPy directly.

### 1. Clone the repository

Replace the placeholder below with the actual GitHub repository URL:

```bash
git clone <YOUR_REPOSITORY_URL>
cd ferment-me-bobteria
```

Alternatively, download the repository as a ZIP file from GitHub and extract it.

### 2. Create a virtual environment (recommended)

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install numpy scipy matplotlib
```

If a `requirements.txt` file is provided, install the listed dependencies using:

```bash
python -m pip install -r requirements.txt
```

---

## Usage

### Running the simulator

The project includes `yogurtferment.py` as its command-line interface. If that remains the main entry point in the current version, run:

```bash
python yogurtferment.py
```

Follow the prompts to select the parameter configuration and provide the requested initial conditions.

The exact interface and available options depend on the current implementation.

### Running the co-culture model programmatically

The core model can be imported into another Python script:

```python
from yogurtcoculture import yogurt_coculture
```

The function accepts initial conditions, kinetic parameters, environmental conditions, interaction coefficients, and the simulation duration.

A schematic example of its structure is:

```python
solution = yogurt_coculture(
    Xs0=initial_st_biomass,
    Xl0=initial_lb_biomass,
    S0=initial_lactose,
    P0=initial_lactic_acid,
    fermentation_time=8.0,
    # Supply the remaining required parameters.
)
```

The names above illustrate the concept; the variables are placeholders, not predefined project constants. The actual function signature and required argument names must be followed when calling the model.

### Accessing simulation results

The model returns a SciPy `OdeResult` object.

Its numerical solution contains the time points and state variables:

```python
solution.t
solution.y
```

The state variables are ordered as follows:

```python
Xs, Xl, S, P, pH = solution.y
```

Here, each row contains the simulated values of one state variable across the returned time points.

For example, the final simulated state can be inspected with:

```python
final_state = solution.y[:, -1]

print("Final S. thermophilus biomass:", final_state[0])
print("Final L. bulgaricus biomass:", final_state[1])
print("Final lactose:", final_state[2])
print("Final lactic acid:", final_state[3])
print("Final model pH:", final_state[4])
```

The final values are predictions from the model, not measurements from an actual fermentation experiment.

---

## Project Structure

The project is organised into modules that separate the mathematical model, parameter definitions, simulation workflow, visualisation, and optimisation.

```text
ferment-me-bobteria/
│
├── yogurtferment.py       # Command-line interface
├── yogurtconstant.py      # Literature-based constants
├── yogurtparameters.py    # Parameter configuration
├── yogurtcoculture.py     # Two-species ODE model
├── yogurtplot.py          # Plotting and visualisation
├── yogurtsimulator.py     # Simulation workflow
├── yogurtoptimization.py  # Parameter and condition sweeps
│
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
└── LICENSE                # Optional licence
```

This is an illustrative structure based on the project's modules. Retain the actual filenames and include only files present in the published repository.

---

## Calibration and Validation

Mathematical models are useful only when their predictions are compared with observations and their limitations are understood.

The project has explored comparison of simulated pH values with a set of reference observations.

An example reference series previously used in the project is:

| Fermentation time (h) | Reference pH |
|---:|---:|
| 0 | 6.51 |
| 2 | 6.50 |
| 4 | 5.30 |
| 6 | 4.50 |
| 8 | 4.45 |

These observations should be accompanied by a complete citation identifying the original experimental source and the conditions under which the measurements were obtained.

The series should not be interpreted as a universal yogurt fermentation profile. Results depend on the bacterial strains, substrate, medium composition, temperature, and experimental conditions.

### Root Mean Square Error

The root mean square error (RMSE) can be used to quantify the difference between model predictions and reference observations:

\[
\operatorname{RMSE}=
\sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat y_i)^2}
\]

where:

- \(y_i\) is an observed value.
- \(\hat y_i\) is the corresponding model prediction.
- \(n\) is the number of observations.

Lower RMSE indicates closer agreement with the selected observations.

However, a lower RMSE does not prove that the selected parameters are biologically correct. Different parameter combinations can produce similar predictions, especially when calibration is based on a small number of observations.

If the same observations are used both to optimise parameters and to report model accuracy, the resulting RMSE describes the fit to those observations rather than independent predictive performance.

### Current validation scope

The available reference series provides a limited basis for assessing the model's pH trajectory.

It does not independently establish the accuracy of the predicted bacterial populations, lactose consumption, or lactic acid production. Those variables would require suitable independent experimental data for meaningful validation.

The relationship between the model's internal pH state and any separate pH calculation used during plotting or evaluation should also be checked before reporting validation results.

---

## Assumptions and Limitations

*Ferment me, Bobteria!* is an educational model of selected fermentation dynamics. Its predictions are conditional on the mathematical assumptions and parameter values used.

### Simplified bacterial physiology

The model uses empirical growth-response functions rather than detailed intracellular metabolic pathways. It does not explicitly simulate gene regulation, enzyme kinetics, or all the metabolic exchanges between the two organisms.

### Simplified species interaction

The interaction function is a mathematical approximation. It cannot fully capture the complex, strain-dependent mechanisms underlying cooperation between *S. thermophilus* and *L. bulgaricus*.

### Simplified pH dynamics

The model represents pH evolution through a relationship between acid production and an effective buffering parameter. It does not solve a full acid-base equilibrium model for yogurt.

### Parameter uncertainty

Literature-derived values may come from different strains, experimental conditions, or measurement conventions. Their applicability to the simulated system must be evaluated rather than assumed.

Calibrated values are conditional on the observations, objective function, and parameter ranges used during optimisation.

### Limited validation data

A small set of pH observations is insufficient to establish predictive accuracy across all state variables and operating conditions.

### Numerical and physical constraints

Numerical integration approximates the solution of the model equations. Solver success does not establish biological validity.

The implementation also needs to be checked for physical consistency, including nonnegative concentrations, appropriate units, realistic parameter ranges, and whether the equations behave sensibly outside the calibration conditions.

### No direct industrial or food-safety application

The simulator has not been established as a substitute for experimental validation, industrial process control, or food-safety assessment.

Its purpose is educational exploration and the study of simplified mathematical relationships.

---

## Future Development

Potential areas for further development include:

- Improving the consistency between the internal pH state and the pH calculation used for validation.
- Incorporating additional experimental observations for calibration and independent validation.
- Investigating parameter sensitivity and identifiability.
- Examining uncertainty in literature-derived and calibrated parameters.
- Refining the representation of bacterial interactions.
- Improving the documentation of parameter sources, units, and assumptions.
- Expanding the analysis and visualisation of biomass, lactose, lactic acid, and pH trajectories.
- Comparing simulated results with additional fermentation datasets.

These are possible future directions, not claims about features already implemented.

---

## References

Salmazo, G. C., Dal Molin Filho, R. G., Robazza, W. S., Schmidt, F. C., & Longhi, D. A. (2023). Modeling the growth dependence of *Streptococcus thermophilus* and *Lactobacillus bulgaricus* as a function of temperature and pH. *Brazilian Journal of Microbiology, 54*(1), 323–334. https://doi.org/10.1007/s42770-023-00907-5

Degeest, B., & De Vuyst, L. (1999). Indication that the nitrogen source influences both amount and size of exopolysaccharides produced by *Streptococcus thermophilus* LY03 and modelling of the bacterial growth and exopolysaccharide production in a complex medium. *Applied and Environmental Microbiology, 65*(7), 2863–2870. https://doi.org/10.1128/AEM.65.7.2863-2870.1999

Rezvani, F., Ardestani, F., & Najafpour, G. (2017). Growth kinetic models of five species of *Lactobacilli* and lactose consumption in batch submerged culture. *Brazilian Journal of Microbiology, 48*(2), 251–258. https://doi.org/10.1016/j.bjm.2016.12.007

Mistry, V. V., & Kosikowski, F. V. (1985). Growth of lactic acid bacteria in highly concentrated ultrafiltered skim milk retentates. *Journal of Dairy Science, 68*(10), 2536–2543. https://doi.org/10.3168/jds.S0022-0302(85)81134-6

Burgos-Rubio, C. N., Okos, M. R., & Wankat, P. C. (2000). Kinetic study of the conversion of different substrates to lactic acid using *Lactobacillus bulgaricus*. *Biotechnology Progress, 16*(3), 305–314. https://doi.org/10.1021/bp000022p





*Ferment me, Bobteria!* is an ongoing learning project. Its purpose is not to provide a perfect representation of yogurt fermentation, but to explore how mathematical models can help us understand a complex biological process—and where those models fall short.
