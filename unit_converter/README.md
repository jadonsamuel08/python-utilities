**Unit Converter**

A small interactive command-line unit converter supporting temperature, distance, volume, and mass conversions.

**Overview**
- Interactive menu-driven converter implemented in `unit_converter/unit_converter.py`.
- Lightweight and easy to extend: conversion functions are stored in the `conversions` dictionary.

**Features**
- Temperature: Celsius, Fahrenheit, Kelvin conversions.
- Distance: kilometers, miles, meters, feet, inches, centimeters.
- Volume: liters, milliliters, gallons, fluid ounces, cups, tablespoons.
- Mass: kilograms, pounds, grams, ounces, stone.

**Usage**
Run the converter from the project root:

```bash
python3 unit_converter/unit_converter.py
```

Follow the interactive prompts:
1. Pick a conversion type (Temperature, Distance, Volume, Mass).
2. Pick a specific conversion (e.g., `km to miles`).
3. Enter the numeric value to convert.

**Examples**
- Convert 10 km to miles: choose `Distance` → `km to miles` → enter `10`.
- Convert 100 F to K: choose `Temperature` → `F to K` → enter `100`.

**Extending**
To add a new conversion, edit `unit_converter/unit_converter.py` and add a new key/value to the appropriate category in the `conversions` dictionary. Each conversion is a small function (lambda or def) that accepts a numeric input and returns the converted numeric value.

**Notes**
- Results are printed with 4 decimal places.
- The program expects numeric input for conversion values; non-numeric input will be rejected.

**License**
See the repository LICENSE for usage terms.
