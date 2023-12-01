# bch_decoder.py
import utils

def decode(input_number):
    result = {
        'corrected_number': '',
        'error_info': {
            'error_position_1': None,
            'error_position_2': None,
            'error_magnitude_1': None,
            'error_magnitude_2': None
        }
    }

    if utils.is_valid_input(input_number, 10):
        encoded_array = [int(digit) for digit in input_number]
        try:
            # Ensure 'correct_errors' returns a dictionary with error positions and magnitudes
            error_info = utils.correct_errors(encoded_array) or {
                'error_position_1': None,
                'error_position_2': None,
                'error_magnitude_1': None,
                'error_magnitude_2': None
            }
            result['corrected_number'] = utils.format_array(encoded_array)
            result['error_info'] = error_info
        except Exception as e:
            raise e
    else:
        raise ValueError("Invalid Input")

    return result
