# Ohm's Law Calculator

## What it does
A Python program that calculates voltage, current, resistance or power from any two known values. It keeps asking if you enter something invalid, so it doesn't crash.

## How to run it
Install Python 3, then run: python Ohms_law.py


## Sample output
```
=== Ohm's Law & Power Calculator ===

What do you want to find?
  V - Voltage
  I - Current
  R - Resistance
  P - Power
Choice (V/I/R/P): v
Known values: pick two of I, R, P
  First known ['I', 'R', 'P']: 1
  Please enter one of: I, P, R
  First known ['I', 'R', 'P']: i
  Second known ['R', 'P']: r
  Enter current (A): 0.01
  Enter resistance (ohm): 100

  Voltage = 1 V

Calculate again? (y/n): y

What do you want to find?
  V - Voltage
  I - Current
  R - Resistance
  P - Power
Choice (V/I/R/P): v
Known values: pick two of I, R, P
  First known ['I', 'R', 'P']: i
  Second known ['R', 'P']: r
  Enter current (A): 1
  Enter resistance (ohm): 100

  Voltage = 100 V
  WARNING: 100 W exceeds 0.25 W - a typical 1/4 W resistor could overheat!

Calculate again? (y/n): n

=== Calculation History ===
  1. Voltage = 1 V  (from I=0.01 A, R=100 ohm)
  2. Voltage = 100 V  (from I=1 A, R=100 ohm)

Goodbye!
```
 

## My own twist
 I added an overheat warning that alerts the user when the power goes above a typical 1/4 W resistor limit, and a history log that lists all the calculations done in that session.

## What I learned
I learned how to store formulas in a dictionary so one program can calculate voltage, current, resistance or power without writing many if statements.

## Author
Brian, ND1 Mechatronics Engineering, YabaTech.
