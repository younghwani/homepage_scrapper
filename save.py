import csv

def save_to_file(companies):
    file = open('company.csv', mode='w')
    writer = csv.writer(file)
    writer.writerow(['company, homepage'])
    for company in companies:
        writer.writerow(list(company))
    return 