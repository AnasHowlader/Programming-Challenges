import csv

from pathlib import Path

csv_file = Path("south.csv")
html_file = Path("south.html.pdf")

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

def read_html(html_file):
    html_contents = []
    html_contents = open(html_file, "r")
    return html_contents

def process(file_contents, html_contents):

    lookingfor = 'url("'
    url_start = html_contents.find(lookingfor)
    url_end = html_contents.find('");', url_start)
    url = html_contents[url_start:url_end]
    






print(file_contents)



















