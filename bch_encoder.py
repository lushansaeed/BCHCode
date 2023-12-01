# bch_encoder.py
import utils


def encode():
    input_number = input("\nPlease enter a six digit number:\n")
    if utils.is_valid_input(input_number, 6):
        encoded_array = [int(digit) for digit in input_number]
        if utils.calculate_and_set_padding(encoded_array):
            print("Encoded Number:", utils.format_array(encoded_array))
        else:
            print("Unusable Number.")
    else:
        print("Invalid Input.")
