def normalize_adc_level(raw_value):
    # 1. Defensive Clamping
    if raw_value > 1023:
        raw_value = 1023
    elif raw_value < 0:
        raw_value = 0

    # 2. Catch the math inside a variable
    normalized_val = raw_value / 1023.0

    # 3. Catch the rounding in a new value
    final_val = round(normalized_val, 3)

    # 4. Push the payload out the port
    return final_val


# -- GLOBAL SCOPE --
# Call the tool and catch the returned payload in vew variables
test_1 = normalize_adc_level(850)
test_2 = normalize_adc_level(1050)
test_3 = normalize_adc_level(-15)

# Print the captured payloads
print(f"Test 1: {test_1}")
print(f"Test 2: {test_2}")
print(f"Test 3: {test_3}")
