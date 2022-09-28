import urllib.request

url = "https://www.officialcharts.com/charts/singles-chart"


def scrape(url):
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    return mystr


def pos_finder(newstring):
    lookingfor = '"position">'
    pos_start = newstring.find(lookingfor)
    pos_end = newstring.find('</', pos_start)
    position = (newstring[pos_start + len(lookingfor):pos_end])

    return position



def name_finder(newstring):
    lookingforname = newstring.find('<a href')
    name_start = newstring.find('/">', lookingforname)
    name_end = newstring.find('</a>', name_start)
    name = (newstring[name_start + 3:name_end])
    return name

def artist_finder(newstring):
    lookingforartist = newstring.find('<div class="artist">')
    artist_start = newstring.find('/">', lookingforartist)
    artist_end = newstring.find('</a>', artist_start)
    artist = (newstring[artist_start + 3:artist_end])
    return artist

def table():
    i = 0
    num = 0
    while num != 10:
        open_tr = html.find('<tr>', i)
        close_tr = html.find("</tr>", open_tr)

        newstring = html[open_tr:close_tr]


        position = pos_finder(newstring)
        name = name_finder(newstring)
        artist = artist_finder(newstring)

        print(f'{position}  {name}  {artist}')

        i = close_tr
        num +=1

if __name__ == "__main__":
    html = scrape(url)
    table()

