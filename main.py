import csv
from random import shuffle
from faker import Faker
from faker.providers import barcode, person, job, date_time, phone_number,color, company, geo
import timeit

start = timeit.default_timer()

fake = Faker('ar_SA')
fake.add_provider(barcode)
fake.add_provider(person)
fake.add_provider(job)
fake.add_provider(date_time)
fake.add_provider(phone_number)
fake.add_provider(color)
fake.add_provider(company)
fake.add_provider(geo)

NUBMER_OF_ENTIRES = 1000

with open('output-1.csv', 'w') as output_1_file:
    data_file_1 = csv.writer(output_1_file, delimiter=',')
    data_file_1.writerow(['ID', 'first name الإسم الأول', 'last name اللقب', 'job المهنة', 'birth date تاريخ الإزدياد'])
    for i in range(NUBMER_OF_ENTIRES):
        data_file_1.writerow([fake.ean8(), fake.first_name(), fake.first_name(), fake.job(), fake.date_of_birth()])


with open('output-2.csv', 'w') as output_2_file:
    data_file_2 = csv.writer(output_2_file)
    data_file_2.writerow(['ID', 'Phone Number رقم الهاتف', 'Company الشركة', 'latitutde', 'longitude'])
    
    with open('output-1.csv') as input_file:
        data_file = csv.reader(input_file)
    
        next(data_file)
        ids = list()
        for line in data_file:
            ids.append(line[0])
        shuffle(ids)
    
    for i in range(NUBMER_OF_ENTIRES):
        data_file_2.writerow([ids[i], fake.phone_number(), fake.color_name(), fake.company(), fake.latitude(), fake.longitude()])

stop = timeit.default_timer()

execution_time = stop - start
print(execution_time)