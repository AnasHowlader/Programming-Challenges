import csv

from pathlib import Path


def read_csv(path):
    with open(path) as csvfile:
        csv_contents = []
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            csv_contents += row
    return csv_contents


def read_html(path):
    html_file = open(path, "r", "utf-8")
    html_contents = html_file.read()
    return html_contents



def process(csv, html):
    i = 0
    v = 0
    s = 0

    counter = 0
    while counter < 6:

        lookingfor = 'url("'
        url_start = html.find(lookingfor, i)
        url_end = html.find('");', url_start)
        link = csv[counter*3]
        newhtml = html.replace[html[url_start:url_end], link]

        initials_start = html.find('"el__heading">', v)
        initials_end = html.find("<", initials_start)
        initials = csv[counter *3 + 1]
        newhtml = html.replace(html[initials_start:initials_end], initials)

        name_start = html.find('el__text">', s)
        name_end = html.find("<", name_start)
        name = csv[counter *3 + 2]
        newhtml = html.replace(html[name_start:name_end], name)

        i = url_end

        v = initials_end

        s = name_end
        counter += 1



def write_html(path, html):
    html_write = open(path, "w")
    html_write.write(html)
    html_write.close()




if __name__ == "__main__":
    csv = read_csv(path="south.csv")
    html = read_html(path="south.html")
    html = process(csv=csv, html=html)
    write_html(path="south_final.html", html=html)