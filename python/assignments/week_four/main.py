def read_and_modify_file():
    # this will ask the user to enter the filename
    filename = input('Enter the name of the file to read: ')

    try: 
        # this will try to open the file 
        infile = open(filename, 'r')
        content = infile.read()
        infile.close()

        # this will modify content of the file 
        modified_content = content.upper()

        # this will open the output file manually 
        outfile = open('modified_output.txt', 'w')
        outfile.write(modified_content)
        outfile.close()

        print("File read successfully and modified content written to 'modified_output.txt'.")


        # this will modify the content to make it uppercase
        modified_content = content.upper()
    except FileNotFoundError: 
        print("There is an error, The file not found. Please check the filename and try again")
    except PermissionError: 
        print("There is an error, You don't have the permission to read this file")
    except Exception as e:
        print(f"An error occured: {e}")
    

read_and_modify_file()
