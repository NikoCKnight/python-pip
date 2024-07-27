import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data

def get_top_3_countries_by_population(data):
  # Ordenar los datos por la población en 2022
  data_sorted = sorted(data, key=lambda x: int(x['2022 Population']), reverse=True)
  # Seleccionar los tres primeros
  top_3 = data_sorted[:3]
  # Mostrar nombre, continente y población en 2022
  for country in top_3:
      population = int(country['2022 Population'])
      formatted_population = format(population, ",")
      print(f"Country: {country['Country/Territory']}, Continent: {country['Continent']}, Population in 2022: {formatted_population}")

if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[0])
  get_top_3_countries_by_population(data)