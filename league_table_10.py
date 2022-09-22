import csv



from pathlib import Path

csv_file = Path("Premier 16-17.csv")

def check_file_exists(csv_file): 
    return csv_file.is_file()
        
def read_csv(csv_file):
    csv_contents = []
    if check_file_exists(csv_file):
        with open(csv_file) as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            next(reader)
            for row in reader:
                csv_contents.append(row)
    return csv_contents


file_contents = read_csv(csv_file)






def process_results(rows):
    dictionary = {}
    goals = 0
    for row in rows:
        home, away, homegoals, awaygoals, winner = row[1], row[2], row[3], row[4], row[5]

        if home not in dictionary:
            dictionary[home] = [0,0]
        if away not in dictionary:
            dictionary[away] = [0,0]



        if winner == "D":
            dictionary[home][0] += 1
            dictionary[away][0] += 1
        if winner == "H":
            dictionary[home][0] += 3
            dictionary[away][0] += 0
        if winner == "A":
            dictionary[home][0] += 0
            dictionary[away][0] += 3

            dictionary[home][1] = dictionary[home][1] + int(homegoals) - int(awaygoals)

    dictionary = sorted(dictionary.items(), key=lambda e: e[1][0], reverse = True)
    data = dictionary
    return dictionary




if __name__ == "__main__":
    file_contents = read_csv(csv_file)
    results = process_results(file_contents)
    print(results)












