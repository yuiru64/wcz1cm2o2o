from data import sealevel_data, country_info, landbelow5
from Island import Island

countries = landbelow5.getData()
countryInfos = country_info.fromCountries(list(countries.keys()))

islands = []
for key in countries.keys():
    islands.append(Island(
        countryInfos[key]["population"],
        countries[key] / 100 * countryInfos[key]["area"],
        countryInfos[key]["area"]
    ))

Island.bind(lambda t: sealevel_data.getLevel(t + 2010))
for y in range(2011, 2020):
    for island in islands:
        print(island.deltaN(y - 2010))


