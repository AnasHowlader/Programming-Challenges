import csv

from pathlib import Path


def read_csv(path):
    with open(path) as csvfile:
        csv_contents = []
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            csv_contents.append(row)
    return csv_contents


def read_html(path):
    html_file = open(path, "r")
    html_contents = html_file.read()
    return html_contents



def process(csv, html):
    i = 0
    v = 0
    s = 0
    k= 0
    counter = 0
    while counter != 5:
        while k < 5:


            lookingfor = 'url("'
            url_start = html.find(lookingfor, i)
            url_end = html.find('");', url_start)
            dummy_link = html[url_start:url_end]
            print(dummy_link)
            k+=1




            initials_start = html.find('"el__heading">', v)
            initials_end = html.find("<", initials_start)




            name_start = html.find('el__text">', s)
            name_end = html.find("<", name_start)



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




















