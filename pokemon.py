# A program made to learn about APIs and integrate them into code!

import sys
import requests

base_url = "https://pokeapi.co/api/v2"

def getInfo(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pkmnData = response.json()
        print(f"\nSuccessfully retrieved Data from {base_url}!")
        print("\n" + "-"*40 + "\n")
        return pkmnData
    else:
        print(f"Failed to retrieve data {response.status_code}")
        return None
    
while True:
    pokemon_name = input("Please enter a pokemon's name: ").lower()
    pkmnInfo = getInfo(pokemon_name)

    try:
        print(f"Name: {pkmnInfo['name']}")
        print(f"ID: {pkmnInfo['id']}")
        print(f"Height {pkmnInfo['height']}")
        print(f"Weight: {pkmnInfo['weight']}")
    except (TypeError, KeyError):
        print("Please enter a valid pokemon name\n")
    
    if pkmnInfo:
        while True:
            userIN = input("\nWould you like to search for another pokemon? (yes/no) ")
            
            if userIN == "yes":
                print("\n" + "-"*40 + "\n")
                break
            elif userIN == "no":
                print("\nThanks for using the PokeAPI!")
                sys.exit()
            else:
                print("Please enter a valid response")