import csv


name = input("Whats your name? ")
home = input("Where is yoyr home? ")


with open("names3.csv", "a") as file:
    # writer = csv.writer(file)
    # writer.writerow([name, home])
    writer = csv.DictWriter(file, fieldnames= ["name", "home"])
    writer.writerow({"name": name, "home": home})

