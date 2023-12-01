from flask import Flask, render_template, request, jsonify
import utils
import bch_decoder

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/encode', methods=['POST'])
def encode():
    data = request.get_json()  # Getting data from the JSON body of the request
    input_number = data['number']  # Extracting the input number from the data

    if utils.is_valid_input(input_number, 6):
        encoded_array = [int(digit) for digit in input_number]
        if utils.calculate_and_set_padding(encoded_array):
            return 'Encoded Number: ' + utils.format_array(encoded_array)
        else:
            return 'Please input 6 digit binary number.', 400
    else:
        return 'Invalid Input.', 400


@app.route('/decode', methods=['POST'])
def decode():
    data = request.get_json()
    encoded_number = data['number']

    try:
        decode_result = bch_decoder.decode(encoded_number)
        error_info = decode_result['error_info']

        response_message = ''
        if error_info['error_position_1'] is not None:
            response_message += f"Error Position 1: {error_info['error_position_1']}, Magnitude: {error_info.get('error_magnitude_1', 'N/A')}\n"
        if error_info['error_position_2'] is not None:
            response_message += f"Error Position 2: {error_info['error_position_2']}, Magnitude: {error_info.get('error_magnitude_2', 'N/A')}\n"

        response_message += f"User Input: {encoded_number}\n"
        response_message += f"Corrected Number: {decode_result['corrected_number']}"

        return response_message
    except Exception as e:
        return str(e), 400



if __name__ == '__main__':
    app.run(debug=True)
