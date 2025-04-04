def read_and_write_file():
    input_filename = input("Enter the filename to read: ")
    
    try:
        with open(input_filename, 'r') as file:
            content = file.read()

        modified_content = content.upper()

        output_filename = input("Enter the filename to write the modified content: ")

        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)

        print(f"Content has been modified and written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{input_filename}' could not be read.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

read_and_write_file()

