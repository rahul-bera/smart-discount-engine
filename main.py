import json
from allocator import allocate_discounts_featurewise
from utils import read_input, write_output

def select_input_file():
    print("Choose an input file to run:")
    print("1. sample_input_normal.json")
    print("2. sample_input_same.json")
    print("3. sample_input_rounding.json")
    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        return "sample_input_normal.json"
    elif choice == "2":
        return "sample_input_same.json"
    elif choice == "3":
        return "sample_input_rounding.json"
    else:
        print("Invalid choice. Defaulting to sample_input_normal.json")
        return "sample_input_normal.json"

if __name__ == "__main__":
    filename = select_input_file()
    data = read_input(filename)
    site_kitty = data["siteKitty"]
    agents = data["salesAgents"]

    result = allocate_discounts_featurewise(site_kitty, agents)
    write_output(result)
