def file_manager():
    while True:
        # This will ask the user which action to take
        print('''\nWelcome to Morris' file manager (CLI based) 
    
What action do you want to do?
1. Create a new file
2. Open an existing file 
3. Exit
''')

        choice = input("Enter 1, 2 or 3: ")

        if choice == "1": 
            filename = input("Enter the name of the new file (e.g. myfile.txt): ")
            try:
                content = input("Enter the content to write in the file:\n")
                file = open(filename, 'w')
                file.write(content)
                file.close()
                print(f"File '{filename}' created successfully!")
            except Exception as e: 
                print(f"Error creating the file: {e}")
        
        elif choice == "2": 
            filename = input("Enter the name of the file to open: ")
            try: 
                file = open(filename, 'r')
                content = file.read()
                file.close()
                print(f"""\nFile Content: 
====================
{content}
====================""")
            except FileNotFoundError:
                print("File not found. Please make sure the filename is correct.")
            except Exception as e: 
                print(f"Error reading the file: {e}")

        elif choice == "3":
            print("Exiting the file manager. Goodbye!")
            break  # Exit the loop

        else: 
            print("Invalid choice. Please enter 1, 2 or 3.")

file_manager()

