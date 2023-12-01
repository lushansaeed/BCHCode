# main.py
import bch_encoder
import bch_decoder


def main():
    while True:
        try:
            print("\nEnter:\n'1' to encode\n'2' to error correct\n'3' to exit.")
            mode = input()
            if mode == '1':
                bch_encoder.perform_encoding()
            elif mode == '2':
                bch_decoder.perform_error_correction()
            elif mode == '3':
                break
            else:
                print("Invalid mode selection.")
        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting...")
            break


if __name__ == "__main__":
    main()
