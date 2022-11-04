import csv

with open('students.csv', 'w') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['First name', 'Last namw', 'Age'])
    csv_writer.writerow(['Jack', 'White', 24])
    csv_writer.writerow(['Jane', 'Black', 21])

# Read and write
with open('cars.csv') as file:
    csv_reader = csv.reader(file)
    make_model_list = []
    for car in csv_reader:
        make_model = [car[1], car[2]]
        make_model_list.append(make_model)
with open('cars_make_model.csv', 'w') as file:
    csv_writer = csv.writer(file)
    for row in make_model_list:
        csv_writer.writerow(row)

# Fast read and write
with open('cars.csv') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    with open('cars_make_model_fast.csv', 'w') as file:
        csv_writer = csv.writer(file)
        for row in csv_reader:
            csv_writer.writerow([row[1], row[2]])

# Dict writer
with open('students1.csv', 'w') as file:
    headers_list = ['First name', 'Last name', 'Age']
    csv_writer = csv.DictWriter(file, fieldnames=headers_list)
    csv_writer.writeheader()
    csv_writer.writerow({
        'First name': 'Ivan',
        'Last name': 'White',
        'Age': 28
    })
    csv_writer.writerow({
        'First name': 'Alice',
        'Last name': 'Black',
        'Age': 26
    })

with open('cars.csv') as file:
    csv_reader = csv.DictReader(file)
    car_list = list(csv_reader)

with open('make_model', 'w') as file:
    headers_list = ['Make', 'Model']
    csv_writer = csv.DictWriter(file, fieldnames=headers_list)
    csv_writer.writeheader()
    for car in car_list:
        csv_writer.writerow({
            'Make': car['Make'],
            'Model': car['Model']
        })
