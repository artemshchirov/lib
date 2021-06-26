import csv

with open('cars.csv') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for car in csv_reader:
        print(f'{car[1]} {car[2]} costs: {car[4]}')

with open('cars.csv') as file:
    csv_reader = csv.reader(file)
    data_list = list(csv_reader)
    print(data_list)

# Ordered dict
with open('cars.csv') as file:
    csv_reader = csv.DictReader(file)
    for car in csv_reader:
        print(f'{car["Make"]} {car["Model"]} costs {car["Price"]}')

# Dict reader
with open('cars;.csv') as file:
    csv_reader = csv.DictReader(file, delimiter=";")  # ordered dict
    for car in csv_reader:
        print(f'{car["Make"]} {car["Model"]} is {car["Length"]} m')

with open('cars;.csv') as file:
    csv_reader = csv.reader(file, delimiter=";")
    next(csv_reader)
    for car in csv_reader:
        print(f'{car[1]} {car[2]} is {car[3]} m')
