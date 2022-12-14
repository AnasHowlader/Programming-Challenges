import csv


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
    x = 1
    y = 1
    while x < 6:
        while y < 6:
            html = html.replace(f"name{y}", csv[x-1][2])
            html = html.replace(f"initials{y}", csv[x-1][1])
            html = html.replace(f"link{y}", csv[x-1][0])
            x+=1
            y+=1

        return html




def write_html(path, html):
    html_write = open(path, "w")
    html_write.write(str(html))
    html_write.close()




if __name__ == "__main__":
    csv = read_csv(path="south.csv")
    html = read_html(path="south.html")
    html = process(csv=csv, html=html)
    write_html(path="south_final.html", html=html)




















