'''
Using the PokéAPI https://pokeapi.co/docs/v2.html#pokemon
fetch the name and height of all 151 Pokémon of the main series.

Create a text document that describes each Pokémon using the information
available in the JSON response.
NOTE: only using 'height' is enough, but if you want more, go crazy.

BONUS: Using your script, create a folder and download the main 'front_default'
       sprites for each Pokémon using requests into that folder.
       Name the files appropriately using the name data from your response.

'''
import requests
import os

url = "https://pokeapi.co/api/v2/pokemon/"
char = "height"
lower = 1
upper = 152
pokemon_info = ""

# for i in range(lower, upper):
#     url = f"{url}{i}/"
#     pokemon = requests.get(url).json()
#     id, name, height, weight = pokemon["id"],pokemon["name"], pokemon["height"], pokemon["weight"]
#     pokemon_info += f"{id}: {name} is {height} decimetres tall and weigh {weight} hectograms, with BMI of{weight/height**2:.2f}.\n"
#     url = "https://pokeapi.co/api/v2/pokemon/"
#
# with open("plokemon.txt", "w") as f:
#     f.write(pokemon_info)

# create a folder
# # detect the current working directory and print it
path = os.getcwd()
# print ("The current working directory is %s" % path)
#
# # define the name of the directory to be created
path += "/pokemon"
#
# try:
#     os.mkdir(path)
# except OSError:
#     print("Creation of the directory %s failed" % path)
# else:
#     print("Successfully created the directory %s " % path)

# download name and front default of sprites for each pokemon
for i in range(lower, upper):
    url = f"{url}{i}/"
    pokemon = requests.get(url).json()
    sprites = pokemon["sprites"]["front_default"]
    file_name = pokemon["name"] + ".png"
    url = "https://pokeapi.co/api/v2/pokemon/"
    file_name = os.path.join(path, file_name)
    response = requests.get(sprites)
# save files to the folder
    with open(os.path.join(path, file_name), "wb") as f:
        f.write(response.content)



