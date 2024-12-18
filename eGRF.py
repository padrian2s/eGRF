import matplotlib.pyplot as plt

def calculate_egfr(creatinine, age, sex, race="non-african-american"):
    """
    Calculate eGFR using the CKD-EPI formula.

    :param creatinine: Serum creatinine in mg/dL
    :param age: Age in years
    :param sex: "male" or "female"
    :param race: "african-american" or "non-african-american"
    :return: eGFR in mL/min/1.73m²
    """
    if sex.lower() == "male":
        k = 0.9  # reference for males
        alpha = -0.411 if creatinine <= k else -1.209
        coeff = 141
    elif sex.lower() == "female":
        k = 0.7  # reference for females
        alpha = -0.329 if creatinine <= k else -1.209
        coeff = 144
    else:
        raise ValueError("Sex must be 'male' or 'female'.")

    race_factor = 1.159 if race.lower() == "african-american" else 1.0

    egfr = coeff * (creatinine / k) ** alpha * (0.993 ** age) * race_factor

    return egfr

def plot_kidney_disease_stages_with_correct_format(egfr, creatinine, age, sex, race="non-african-american"):
    """
    Plot a bar chart showing eGFR value and the kidney disease stages, with the format matching the provided example.

    :param egfr: eGFR value in mL/min/1.73m²
    :param creatinine: Serum creatinine in mg/dL
    :param age: Age in years
    :param sex: "male" or "female"
    :param race: "african-american" or "non-african-american"
    """
    stages = [
        "Stage 5: Kidney Failure",
        "Stage 4: Severe Reduction",
        "Stage 3b: Moderate-to-Severe Reduction",
        "Stage 3a: Mild-to-Moderate Reduction",
        "Stage 2: Mild Reduction",
        "Stage 1: Normal or High Function"
    ]
    thresholds = [0, 15, 30, 45, 60, 90, 120]  # eGFR thresholds for each stage (including upper limit)
    colors = ['darkred', 'red', 'orange', 'yellow', 'lime', 'green']

    # Create the bar graph for thresholds
    for i in range(len(thresholds) - 1):
        plt.barh(
            stages[i],
            thresholds[i + 1] - thresholds[i],
            left=thresholds[i],
            color=colors[i],
            edgecolor='black',
            alpha=0.7
        )

    # Add the user's eGFR as a vertical line
    plt.axvline(x=egfr, color='blue', linestyle='--', label=f'eGFR = {egfr:.2f} mL/min/1.73m²')

    # Add annotation for the eGFR value
    plt.text(
        egfr + 1, len(stages) - 1,  # Position near the top of the bar
        f'{egfr:.2f}', color='blue', fontsize=10, va='center'
    )

    # Label the values used in the formula
    if sex.lower() == "male":
        k = 0.9
        coeff = 141
        alpha = -0.411 if creatinine <= k else -1.209
    elif sex.lower() == "female":
        k = 0.7
        coeff = 144
        alpha = -0.329 if creatinine <= k else -1.209
    else:
        raise ValueError("Sex must be 'male' or 'female'.")

    race_factor = 1.159 if race.lower() == "african-american" else 1.0

    constants_info = (
        f"Constants:\n"
        f"- {coeff}: Scaling factor\n"
        f"- {creatinine:.2f}: Serum creatinine (mg/dL)\n"
        f"- {k:.2f}: Reference creatinine for {sex}\n"
        f"- {alpha:.3f}: Exponent (based on creatinine)\n"
        f"- 0.993: Age adjustment factor\n"
        f"- {age}: Age in years\n"
        f"- {race_factor:.3f}: Race adjustment factor\n"
    )

    # Formula used in the calculation
    formula = f"eGFR = {coeff} × ({creatinine:.2f}/{k:.2f})^({alpha:.3f}) × (0.993^{age}) × {race_factor:.3f}"

    # Add formula and constants to the plot
    plt.figtext(0.5, 0.001, formula, wrap=True, horizontalalignment='center', fontsize=10)
    plt.figtext(0.02, -0.00, constants_info, wrap=True, horizontalalignment='left', fontsize=9)

    # Chart details
    plt.title("Kidney Disease Stages Based on eGFR")
    plt.xlabel("eGFR (mL/min/1.73m²)")
    plt.ylabel("Kidney Disease Stages")
    plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.35), fontsize=9, ncol=2, frameon=True)
    plt.grid(axis='x', linestyle='--', alpha=0.5)
    plt.tight_layout()

    # Show the plot
    plt.show()

# Exemplu de utilizare
creatinine = 1.45  # în mg/dL
age = 45           # în ani
sex = "male"       # "male" sau "female"
race = "non-african-american"  # "african-american" sau "non-african-american"

# Calculați eGFR
egfr = calculate_egfr(creatinine, age, sex, race)

# Plotați graficul cu formula și constantele actualizate
plot_kidney_disease_stages_with_correct_format(egfr, creatinine, age, sex, race)
