conversions = {
    'Temperature': {
        'C to F': lambda c: (c * 9/5) + 32,
        'F to C': lambda f: (f - 32) * 5/9,
        'C to K': lambda c: c + 273.15,
        'K to C': lambda k: k - 273.15,
        'F to K': lambda f: (f - 32) * 5/9 + 273.15
    },
    'Distance': {
        'km to miles': lambda km: km * 0.621371,
        'miles to km': lambda miles: miles / 0.621371,
        'meters to feet': lambda m: m * 3.28084,
        'feet to meters': lambda ft: ft / 3.28084,
        'meters to inches': lambda m: m * 39.3701,
        'inches to meters': lambda in_: in_ / 39.3701,
        'km to meters': lambda km: km * 1000,
        'meters to km': lambda m: m / 1000,
        'cm to inches': lambda cm: cm / 2.54,
        'inches to cm': lambda in_: in_ * 2.54
    },
    'Volume': {
        'liters to gallons': lambda l: l * 0.264172,
        'gallons to liters': lambda gal: gal / 0.264172,
        'ml to fl oz': lambda ml: ml * 0.033814,
        'fl oz to ml': lambda oz: oz / 0.033814,
        'liters to ml': lambda l: l * 1000,
        'ml to liters': lambda ml: ml / 1000,
        'cups to ml': lambda cups: cups * 236.588,
        'ml to cups': lambda ml: ml / 236.588,
        'tablespoons to ml': lambda tbsp: tbsp * 14.787,
        'ml to tablespoons': lambda ml: ml / 14.787
    },
    'Mass': {
        'kg to lbs': lambda kg: kg * 2.20462,
        'lbs to kg': lambda lbs: lbs / 2.20462,
        'grams to oz': lambda g: g * 0.035274,
        'oz to grams': lambda oz: oz / 0.035274,
        'kg to grams': lambda kg: kg * 1000,
        'grams to kg': lambda g: g / 1000,
        'kg to stone': lambda kg: kg / 6.35029,
        'stone to kg': lambda st: st * 6.35029,
        'pounds to ounces': lambda lbs: lbs * 16,
        'ounces to pounds': lambda oz: oz / 16
    }
}

def main():
    while True:
        print("\n===Unit Converter===")
        print("Select a conversion type:")
        
        # Show conversion types
        types = list(conversions.keys())
        for i, conv_type in enumerate(types, 1):
            print(f"{i}. {conv_type}")
        print(f"{len(types) + 1}. Quit\n")
        
        type_choice = input("Choose: ").strip()
        
        if type_choice == str(len(types) + 1):
            print("Goodbye!")
            break
        
        # Validate choice and get conversion type
        try:
            type_index = int(type_choice) - 1
            if type_index < 0 or type_index >= len(types):
                print("Invalid choice. Try again.")
                continue
            selected_type = types[type_index]
        except Exception:
            print("Invalid input. Try again.")
            continue
        
        available_conversions = conversions[selected_type]
        conv_list = list(available_conversions.keys())
        
        print(f"\n{selected_type} Conversions:")
        for i, conv in enumerate(conv_list, 1):
            print(f"{i}. {conv}")
        print(f"{len(conv_list) + 1}. Back to menu\n")
        
        conv_choice = input("Choose: ").strip()
        
        if conv_choice == str(len(conv_list) + 1):
            continue
        
        # Validate choice and get conversion function
        try:
            conv_index = int(conv_choice) - 1
            if conv_index < 0 or conv_index >= len(conv_list):
                print("Invalid choice. Try again.")
                continue
            selected_conv = conv_list[conv_index]
        except Exception:
            print("Invalid input. Try again.")
            continue
        
        # Get value and perform conversion
        try:
            value = float(input(f"\nEnter value: "))
            result = available_conversions[selected_conv](value)
            print(f"Result: {result:.4f}\n")
        except ValueError:
            print("Invalid number. Try again.")

if __name__ == "__main__":
    main()