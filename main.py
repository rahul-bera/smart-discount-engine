import json
from allocator import allocate_discounts_featurewise
from utils import read_input, write_output

if __name__ == "__main__":
    data = read_input("sample_input.json")
    site_kitty = data["siteKitty"]
    agents = data["salesAgents"]

    result = allocate_discounts_featurewise(site_kitty, agents)
    write_output(result)
    