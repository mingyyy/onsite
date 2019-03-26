from requests_html import HTMLSession
from pprint import pprint
import sqlalchemy as db
import json

# http://climatedataapi.worldbank.org/climateweb/rest//v1/country/mavg/bccr_bcm2_0/a2/pr/2020/2039/bra
# http://climatedataapi.worldbank.org/climateweb/rest/v1/country/type/var/start/end/ISO3[.ext]

type = ["mavg", "annualavg", "manom", "annualanom"]
# type:
# mavg - monthly avg
# annualavg - annual avg
# manom - avg monthly change 1961-1999
# annualanom - avg annual change 1961-1999
var = ["pr", "tas"]
# var:
# pr - Precipitation (rainfall and assumed water equivalent), in millimeters
# tas - Temperature, in degrees Celsius
start = [1920, 1940, 1960, 1980, 2020, 2040, 2060, 2080]
end = [1939, 1959, 1979, 1999, 2039, 2059, 2079, 2099]
# past:
# start end
# 1920 1939
# 1940 1959
# 1960 1979
# 1980 1999

# past:
# start end
# 2020 2039
# 2040 2059
# 2060 2079
# 2080 2099
iso = []
with open("wb_country_code.json", "r") as f:
    file = json.load(f)
for i in file:

    for k in i.keys():
        if k == "id" and i["incomeLevel"] != "Aggregates":
            iso.append(i["id"])
print(len(iso), iso)
for i in iso:
    path = f"http://climatedataapi.worldbank.org/climateweb/rest/v1/country/{type[0]}/{var[0]}/{start[0]}/{end[0]}/{iso[0]}[.ext]"