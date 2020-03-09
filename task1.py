from data import sealevel_data, country_info, landbelow5
from Island import Island
import bokeh.plotting as plotting
import bokeh.palettes as palettes
import numpy as np
from pandas import DataFrame

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
result = []
level = []
_max = 0
step = 10
for island in islands:
    tmp = []
    result.append(tmp)
    for y in range(2011, 2100, step):
        num = 0
        for i in range(step):
            num += island.deltaN(y + i - 2010)
            # num += island.deltaS(y + i - 2010)
            # num += island.leftN(y + i - 2010)
        _max = max(_max, num)
        tmp.append(num)

plotting.output_file("docs/pic1.html")

names = list(countries.keys())
fig = plotting.figure(x_range=(0, len(names) + 1), y_range=(0, _max * 1.2))
df = DataFrame(np.array(result).T).add_prefix("y")
fig.varea_stack(["y" + str(i) for i in range(len(names))], x="index", color=palettes.brewer["Spectral"][len(names)], legend_label=names, source=df)

# fig = plotting.figure()
# def draw(_result, color):
#     fig.line(np.arange(2011, 2100, step), _result, line_width=5, color=color, alpha=.5)
#     fig.circle(np.arange(2011, 2100, step), _result, size=20, alpha=.5, color=color)

# _len = len(result)
# colors = palettes.brewer["Spectral"][_len]
# for i in range(_len):
#     draw(result[i], colors[i])
plotting.show(fig, "windows-default")
