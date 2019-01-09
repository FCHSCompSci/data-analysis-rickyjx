import csv

pop = []
arrests = []
filename = 'drug-arrests-in-the-us.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for row in reader:
        try:
            pop.append(row[1])
            arrests.append(row[5])
        except IndexError:
            print("Error")


    print(pop)
    print(arrests)

    percentages = []

    for pop in pop:
        for arrest in arrests:
            percentages.append(int(arrest) / int(pop))

    print(percentages)
