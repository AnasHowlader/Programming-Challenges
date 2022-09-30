import csv

from pathlib import Path

csv_file = Path("south.csv")
html_file = Path("south.html.pdf")

def check_file_exists(path):
    return csv_file.is_file()

def read_csv(path):
    csv_contents = []
    if check_file_exists(csv_file):
        with open(csv_file) as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            next(reader)
            for row in reader:
                csv_contents.append(row)
    return csv_contents


file_contents = read_csv(csv_file)


def read_html(path):
    html_contents = []
    html_contents = open(html_file, "r")
    return html_contents

html_contents = read_html(html_file)

def process(csv, html):

    lookingfor = 'url("'
    url_start = html.find(lookingfor)
    url_end = html.find('");', url_start)
    url = html[url_start:url_end]
    url.append(csv())



def write_html(path, html):
    html = open(html_file, "w")
    html.write(process(path))





print(file_contents)





















