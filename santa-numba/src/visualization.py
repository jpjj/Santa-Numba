import folium
import numpy as np


def get_map(route: np.array, locations: list[dict]):
    """
    Create a folium map showing the route through capital cities.

    Args:
        route: numpy array of indices representing the order of locations to visit
        locations: list of dicts with keys 'country', 'capital', 'lat', 'lon'

    Returns:
        folium.Map object
    """
    # Create a map centered on the world
    m = folium.Map(location=[20, 0], zoom_start=2)

    # Add markers for each capital in the route
    for idx in route:
        loc = locations[idx]
        folium.Marker(
            location=[loc["lat"], loc["lon"]],
            popup=f"{loc['capital']}, {loc['country']}",
            tooltip=loc["capital"],
            icon=folium.Icon(color="red", icon="gift"),
        ).add_to(m)

    # Add lines showing the route
    route_coords = [[locations[idx]["lat"], locations[idx]["lon"]] for idx in route]
    # Close the loop by returning to the start
    route_coords.append(route_coords[0])

    folium.PolyLine(
        route_coords, color="blue", weight=2.5, opacity=0.7, tooltip="Route"
    ).add_to(m)

    return m
