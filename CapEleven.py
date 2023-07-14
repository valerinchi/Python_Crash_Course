print("Hello world")

# Try it yourself

def city_functions(city, country):
    full_name = f"{city}, {country}" 
    return full_name.title()

print("Enter 'q' at any time to quit.")
while True:
    city = input("Please, give me the name of a city: ")
    if city == 'q':
        break
    country = input("Please, giove me the name of a country: ")
    if country == 'q':
        break

    formatted_name = city_functions(city, country)
    print(f"\tNeatly formatted name: {formatted_name}.")