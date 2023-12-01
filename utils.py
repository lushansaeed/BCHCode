# utils.py

def is_valid_input(input_str, expected_length):
    return len(input_str) == expected_length and input_str.isdigit()


def format_array(array):
    return ''.join(str(num) for num in array)


def calculate_and_set_padding(encoded_array):
    encoded_array.extend([0] * 4)
    encoded_array[6] = (4 * encoded_array[0] + 10 * encoded_array[1] + 9 * encoded_array[2] +
                        2 * encoded_array[3] + encoded_array[4] + 7 * encoded_array[5]) % 11
    encoded_array[7] = (7 * encoded_array[0] + 8 * encoded_array[1] + 7 * encoded_array[2] +
                        encoded_array[3] + 9 * encoded_array[4] + 6 * encoded_array[5]) % 11
    encoded_array[8] = (9 * encoded_array[0] + encoded_array[1] + 7 * encoded_array[2] +
                        8 * encoded_array[3] + 7 * encoded_array[4] + 7 * encoded_array[5]) % 11
    encoded_array[9] = (encoded_array[0] + 2 * encoded_array[1] + 9 * encoded_array[2] +
                        10 * encoded_array[3] + 4 * encoded_array[4] + encoded_array[5]) % 11

    return all(num != 10 for num in encoded_array[6:10])


def correct_errors(encoded_array):
    s1 = sum(encoded_array[i] for i in range(10)) % 11
    s2 = sum((i + 1) * encoded_array[i] for i in range(10)) % 11
    s3 = sum(pow(i + 1, 2) * encoded_array[i] for i in range(10)) % 11
    s4 = sum(pow(i + 1, 3) * encoded_array[i] for i in range(10)) % 11

    error_positions = {
        'error_position_1': None,
        'error_position_2': None,
        'error_magnitude_1': None,  # Consider updating this key as well
        'error_magnitude_2': None   # Consider updating this key as well
    }

    if s1 == 0 and s2 == 0 and s3 == 0 and s4 == 0:
        return error_positions  # No errors

    p = mod11(s2 * s2 - s1 * s3)
    q = mod11(s1 * s4 - s2 * s3)
    r = mod11(s3 * s3 - s2 * s4)

    if p == 0 and q == 0 and r == 0:
        error_position = mod11(s2 * inverse(s1))
        error_magnitude = s1
        encoded_array[error_position - 1] = mod11(encoded_array[error_position - 1] - error_magnitude)
        error_positions['error_position_1'] = error_position
        error_positions['error_magnitude_1'] = error_magnitude
        return error_positions

    else:
        discriminant = mod11(q * q - 4 * p * r)
        if discriminant >= 0:
            sqrt_discriminant = sqrt_mod11(discriminant)
            error_position1 = mod11((mod11(-q + sqrt_discriminant) * inverse(2 * p)) % 11)
            error_position2 = mod11((mod11(-q - sqrt_discriminant) * inverse(2 * p)) % 11)

            # Recalculating error magnitudes
            # m1 = mod11(s1 - error_position2 * s2 + error_position1 * error_position2 * s3)
            # m2 = mod11(s2 - error_position2 * s3 + error_position1 * error_position2 * s4)

            error_magnitude2 = mod11(mod11(error_position1 * s1 - s2) * inverse(error_position1 - error_position2));
            error_magnitude1 = mod11(s1 - error_magnitude2);

            # Apply corrections
            encoded_array[error_position1 - 1] = mod11(encoded_array[error_position1 - 1] - error_magnitude1)
            encoded_array[error_position2 - 1] = mod11(encoded_array[error_position2 - 1] - error_magnitude2)

            error_positions['error_position_1'] = error_position1
            error_positions['error_position_2'] = error_position2
            error_positions['error_magnitude_1'] = error_magnitude1
            error_positions['error_magnitude_2'] = error_magnitude2
            return error_positions

        else:
            raise Exception("Error correction failed. More than two errors detected")

    return error_positions



def mod11(value):
    return (value % 11 + 11) % 11


def inverse(i):
    inverses = {1: 1, 2: 6, 3: 4, 4: 3, 5: 9, 6: 2, 7: 8, 8: 7, 9: 5, 10: 10}
    return inverses.get(mod11(i), 0)


def sqrt_mod11(i):
    sqrt_values = {1: 1, 3: 5, 4: 2, 5: 4, 9: 3}
    if i in sqrt_values:
        return sqrt_values[i]
    else:
        raise ValueError("Error correction failed. More than two errors detected.")
