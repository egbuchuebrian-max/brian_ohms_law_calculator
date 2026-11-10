"""Ohm's Law and Power Calculator (with resistor overheat warning)."""

from math import sqrt

NAMES = {"V": "Voltage", "I": "Current", "R": "Resistance", "P": "Power"}
UNITS = {"V": "V", "I": "A", "R": "ohm", "P": "W"}
MAX_RESISTOR_WATTS = 0.25  # typical 1/4 W resistor

# FORMULAS[target][frozenset of the two known values] -> function(known dict)
FORMULAS = {
    "V": {
        frozenset("IR"): lambda k: k["I"] * k["R"],
        frozenset("PI"): lambda k: k["P"] / k["I"],
        frozenset("PR"): lambda k: sqrt(k["P"] * k["R"]),
    },
    "I": {
        frozenset("VR"): lambda k: k["V"] / k["R"],
        frozenset("PV"): lambda k: k["P"] / k["V"],
        frozenset("PR"): lambda k: sqrt(k["P"] / k["R"]),
    },
    "R": {
        frozenset("VI"): lambda k: k["V"] / k["I"],
        frozenset("VP"): lambda k: k["V"] ** 2 / k["P"],
        frozenset("PI"): lambda k: k["P"] / k["I"] ** 2,
    },
    "P": {
        frozenset("VI"): lambda k: k["V"] * k["I"],
        frozenset("IR"): lambda k: k["I"] ** 2 * k["R"],
        frozenset("VR"): lambda k: k["V"] ** 2 / k["R"],
    },
}


def ask_choice(prompt, valid):
    """Keep asking until the user types one of the valid options."""
    while True:
        choice = input(prompt).strip().upper()
        if choice in valid:
            return choice
        print(f"  Please enter one of: {', '.join(sorted(valid))}")


def ask_number(prompt):
    """Keep asking until the user enters a non-negative number."""
    while True:
        try:
            value = float(input(prompt).strip())
            if value < 0:
                print("  Value can't be negative.")
                continue
            return value
        except ValueError:
            print("  That's not a number, try again.")


def power_of(values):
    """Work out power from whichever of V, I, R we have."""
    if "P" in values:
        return values["P"]
    if "V" in values and "I" in values:
        return values["V"] * values["I"]
    if "I" in values and "R" in values:
        return values["I"] ** 2 * values["R"]
    return values["V"] ** 2 / values["R"]


def main():
    print("=== Ohm's Law & Power Calculator ===")
    history = []  # Twist: log of every successful calculation
    while True:
        print("\nWhat do you want to find?")
        for key, name in NAMES.items():
            print(f"  {key} - {name}")
        target = ask_choice("Choice (V/I/R/P): ", NAMES)

        others = [k for k in NAMES if k != target]
        print(f"Known values: pick two of {', '.join(others)}")
        first = ask_choice(f"  First known {others}: ", others)
        second = ask_choice(
            f"  Second known {[o for o in others if o != first]}: ",
            [o for o in others if o != first],
        )

        known = {}
        for key in (first, second):
            known[key] = ask_number(f"  Enter {NAMES[key].lower()} ({UNITS[key]}): ")

        try:
            result = FORMULAS[target][frozenset(known)](known)
        except ZeroDivisionError:
            print("\n  Can't divide by zero - check your inputs.")
        else:
            print(f"\n  {NAMES[target]} = {result:.4g} {UNITS[target]}")

            # Twist: save to history
            inputs = ", ".join(f"{k}={v:g} {UNITS[k]}" for k, v in known.items())
            history.append(f"{NAMES[target]} = {result:.4g} {UNITS[target]}  (from {inputs})")

            # Twist: overheat warning
            watts = power_of({**known, target: result})
            if watts > MAX_RESISTOR_WATTS:
                print(
                    f"  WARNING: {watts:.4g} W exceeds {MAX_RESISTOR_WATTS} W - "
                    "a typical 1/4 W resistor could overheat!"
                )

        again = ask_choice("\nCalculate again? (y/n): ", {"Y", "N"})
        if again == "N":
            if history:
                print("\n=== Calculation History ===")
                for number, entry in enumerate(history, start=1):
                    print(f"  {number}. {entry}")
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()
