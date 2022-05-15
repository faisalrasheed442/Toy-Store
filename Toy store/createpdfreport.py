import csv
def create_file(text,title):
    with open(str(title)+'.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(text)
        file.close()