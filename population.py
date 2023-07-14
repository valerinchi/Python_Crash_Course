def get_formatted_country(city, country, population=None):
    full_country = f"{city}, {country}"
    if population is not None:
        full_country += f" - population {population}"
    return full_country.title()
