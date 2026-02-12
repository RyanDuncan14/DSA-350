import pandas as pd
df = pd.read_csv("planet_data.csv", index_col="eName")
df = df[["isPlanet", "meanRadius", "orbit_type", "orbits"]]
print(df.head())

class planet:
    def __init__(self, eName, meanRadius, color="blue"):
        self.radius = float(meanRadius)
        self.color = color
        self.name = eName
        self.moon_list = []

    def set_color(self, new_color):
        self.color = new_color

    def append_moon_list(self, m):
        self.moon_list.append(m)


class moon:
    def __init__(self, eName, meanRadius, orbit_type="secondary", color="white", planet_companion=None):
        self.name = eName
        self.radius = float(meanRadius)
        self.color = color
        self.orbit_type = orbit_type          
        self.planet_companion = planet_companion  

    def update_planet(self):
        if self.planet_companion is None:
            return False
        if self not in self.planet_companion.moon_list:
            self.planet_companion.append_moon_list(self)
            return True
        return False


def print_largest(pl):
    largest = None
    for m in pl.moon_list:
        if largest is None:
            largest = m
        else:
            if largest.radius < m.radius:
                largest = m
    if largest is not None:
        print(f"The largest moon of {pl.name} is {largest.name}")



planet_d = dict()
moon_d = dict()

for index, row in df.iterrows():
    if row['isPlanet'] is True:
        planet_d[index] = planet(eName=index, meanRadius= row['meanRadius'] )

for index, row in df.iterrows():
    if row['isPlanet'] is False:
         moon_d[index] = moon (eName=index, meanRadius= row['meanRadius'],
                                planet_companion=planet_d[ row['orbits']])

for key, val in planet_d.items():
    print(key, val.radius)
         
for key, val in moon_d.items(): 
    val.update_planet()
    print(key, val.radius, val.planet_companion.name)

for key, val in planet_d.items():  
    print_largest(val) 
    print(key, [moon.name for moon in val.moon_list]) 