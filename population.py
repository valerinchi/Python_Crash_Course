def get_formatted_country(city, country, population=''):
    if not isinstance(population, (int, float)):
        raise TypeError("Population must be a number.")
    if population:
        the_country = f"{city}, {country}, {population}"
    else:
        the_country = f"{city}, {country}"
    return the_country.title()