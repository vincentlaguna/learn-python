# Sample use of csv library to open a csv file as a list and output certain content
import csv

print("Retrieving data from 100-contacts.csv >>>\n")

email_list = []

with open('100-contacts.csv') as contacts:
    contact_reader = csv.DictReader(contacts)
    #contact_reader = csv.DictReader(contacts, delimiter = '@') # With delimiter option
    for row in contact_reader:
        email_list.append(row["email"])
print(email_list)