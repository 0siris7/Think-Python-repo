def get_formatted_city(city, country, population = ''):
    if population:
        formatted_place = f"{city}, {country} - {population}"

    else:
        formatted_place = f"{city}, {country}"
    return formatted_place.title()
