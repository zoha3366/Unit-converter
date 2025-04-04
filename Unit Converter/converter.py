import json
import os

# Load conversion rates from JSON file
def load_units():
    file_path = os.path.join(os.path.dirname(__file__), "unit.json")
    with open(file_path, "r") as file:
        return json.load(file)

units = load_units()

def convert(value, from_unit, to_unit, category):
    """Convert value from one unit to another within the same category."""
    if category in units and from_unit in units[category] and to_unit in units[category]:
        from_rate = units[category][from_unit]
        to_rate = units[category][to_unit]
        
        if from_rate is None or to_rate is None:
            raise ValueError(f"Conversion rates not found for {from_unit} or {to_unit} in category {category}")
        
        return value * (to_rate / from_rate)
    
    elif category == "temperature":
        return convert_temperature(value, from_unit, to_unit)  
    
    else:
        raise ValueError(f"Invalid unit conversion: {from_unit} to {to_unit} in {category}")

def convert_temperature(value, from_unit, to_unit):
    """Convert between Celsius and Fahrenheit."""
    if from_unit == "celsius" and to_unit == "fahrenheit":
        return value * 9/5 + 32
    elif from_unit == "fahrenheit" and to_unit == "celsius":
        return (value - 32) * 5/9
    else:
        raise ValueError("Invalid temperature conversion")
