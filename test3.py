#!/usr/bin/python3
import json, sys, getopt

# print('Number of arguments:', len(sys.argv), 'arguments.')
# print('Argument List:', str(sys.argv))
# print(sys.argv[2])

data = {
    "Host name": "Billy",
    "expansions": {"Expansioncheck": "Y",
    "The Forgotten": "Y",
    "African Kingdoms": "Y",
    "Rise of the Rajas": "Y",
    "DE Civs": "N",
    "Lords of the West": "Y",
    "Dawn of the Dukes": "N"},
    "Number of players": "4",
    "PlayerNames":{"ProvidePlayerNames": "Y",
    "Player2": "Joe",
    "Player3": "Nic",
    "Player4": "Tom"}
}

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)


# inputfile = str(sys.argv[2])
#
# with open(inputfile, "r") as read_file:
#     data = json.load(read_file)
#
# if __name__ == "__main__":
#    print(data)

