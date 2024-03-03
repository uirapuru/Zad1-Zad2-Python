def read_file_content():
    while True:
        file_name = input("Please enter the file name: ")
        try:
            with open(file_name, 'r') as file:
                return file.read()
        except FileNotFoundError:
            print(f"File '{file_name}' not found. Please try again.")
