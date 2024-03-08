import requests
def get_superhero_info(hero_name):
    url = f"https://superheroapi.com/api/2619421814940190/search/{hero_name}"
    response = requests.get(url)
    data = response.json()
    if "results" in data:
        results = data["results"]
        if results:
            hero = results[0]
            name = hero["name"]
            intelligence = hero["powerstats"]["intelligence"]
            return f"{name} has an intelligence of {intelligence} ."
        else:
            return "No results found."
    else:
        return "Error: Unable to retrieve data."
Hulk = get_superhero_info("Hulk")
Captain_America = get_superhero_info("Captain America")
Thanos = get_superhero_info("Thanos")
print(Hulk)
print(Captain_America)
print(Thanos)
if int(Hulk.split()[-2]) > int(Captain_America.split()[-2]) and int(Hulk.split()[-2]) > int(Thanos.split()[-2]):
  print("Hulk is the smartest superhero")
elif int(Captain_America.split()[-2]) > int(Hulk.split()[-2]) and int(Captain_America.split()[-2]) > int(Thanos.split()[-2]):
  print("Captain America is the smartest superhero")
elif int(Thanos.split()[-2]) > int(Hulk.split()[-2]) and int(Thanos.split()[-2]) > int(Captain_America.split()[-2]):
  print("Thanos is the smartest superhero")