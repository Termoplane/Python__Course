import csv

with open ("Crimes.csv", "r") as f:
    reader = csv.reader(f)

    crime_type_value = {}

    for row in reader:
        if '2015' in row[2]:
            if row[5] not in crime_type_value:
                crime_type_value[row[5]] = 1
            else:
                crime_type_value[row[5]] += 1

ctv_rev = {v:k for k, v in crime_type_value.items()}

print(ctv_rev[max(ctv_rev)])