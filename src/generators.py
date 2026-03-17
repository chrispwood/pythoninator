### This module explores how to use generators in Python.


import pathlib


def grocery_generator(file_path):
    """
    A generator that pulls grocery items from a file.
    """
    try:
        with open(file_path, "r") as file:
            for line in file:
                item = line.strip()
                if item:
                    yield item
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")


def main():
    print("Welcome to the Grocery List Generator (File Mode)!")
    
    # Calculate path relative to the script file
    script_path = pathlib.Path(__file__).resolve()
    # Assuming grocery_list.txt is in the project root, one level up from 'src'
    file_path = script_path.parent.parent / "grocery_list.txt"
    
    my_groceries = grocery_generator(file_path)

    print(f"\nStarting to iterate through your grocery list from '{file_path.name}':")
    for grocery in my_groceries:
        user_input = input("Would you like the next item? y/N: ").strip().lower()
        if user_input == 'y':
            print(f"Adding {grocery} to the cart...")
        else:
            print("Iteration halted by user.")
            break

    print("\nAll items have been processed or iteration was stopped.")


    if __name__ == "__main__":
        main()

