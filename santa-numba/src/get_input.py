from countryinfo import CountryInfo
import pycountry
import numpy as np
from haversine import Unit
import haversine


def _get_all_capital_geocodes() -> list[dict]:
    results = []
    for country in pycountry.countries:
        try:
            info = CountryInfo(country.name)
            capital = info.capital()
            latlng = info.latlng()
            results.append(
                {
                    "country": country.name,
                    "capital": capital,
                    "lat": latlng[0] if latlng else None,
                    "lon": latlng[1] if latlng else None,
                }
            )
        except (KeyError, AttributeError):
            pass

    return results


def get_distance_matrix() -> np.array:
    capitals = _get_all_capital_geocodes()
    geocodes_vector = np.array([(c1["lat"], c1["lon"]) for c1 in capitals])
    return np.array(
        haversine.haversine_vector(
            geocodes_vector, geocodes_vector, Unit.KILOMETERS, comb=True
        )
    )
