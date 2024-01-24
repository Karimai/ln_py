import csv
data = {}
data['name'] = ["Iran", "Iraq"]
data["iso"] = ["IR", "IQ"]
with open('eggs.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile)
    for i in range(2):
        spamwriter.writerow([data["name"][i], data["iso"][i]])
