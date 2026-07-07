# List of trips
trips = [['france', 'germany', 'italy', 'spain', 'netherlands', 'sweden', 'norway', 'switzerland', 'austria', 'portugal', 'belgium'],
         ['japan', 'china', 'thailand', 'vietnam', 'indonesia', 'india', 'malaysia', 'philippines', 'singapore', 'mongolia'],
         ['usa', 'canada', 'mexico', 'brazil', 'argentina', 'colombia', 'peru', 'chile', 'ecuador'],
         ['egypt', 'morocco', 'south africa', 'tunisia', 'algeria', 'kenya', 'nigeria', 'ethiopia'],
         ['australia', 'new zealand', 'fiji', 'papua new guinea', 'samoa']]

# List of all countries 
countries = []
for trip in trips:
    for country in trip:
        countries.append(country.capitalize())
   

# Testing
print('List of Countries:', countries)