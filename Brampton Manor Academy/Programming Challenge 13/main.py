import urllib.request

url = "https://www.officialcharts.com/charts/singles-chart"


def scrape(url):
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    return mystr


def pos_finder(html):
    k= 0
    while k != 10:
        open_tr = html.find('<tr>', k)
        close_tr: object = html.find("</tr>", open_tr)

        newstring = html[open_tr:close_tr]
        lookingfor = '"position">'
        pos_start = newstring.find(lookingfor)
        pos_end = newstring.find('</', pos_start)
        position = (newstring[pos_start + len(lookingfor):pos_end])

        return position
        k += 1



def name_finder(html):
    v = 0
    open_tr_2 = html.find('<tr>', v)
    close_tr_2 : object = html.find("</tr>", open_tr_2)

    namestring = html[open_tr_2:close_tr_2]
    lookingforname = '<a'
    name_start = namestring.find(lookingforname)
    name_end = namestring.find('</a>', name_start)
    name = (namestring[name_start + 47:name_end])
    return name

def artist_finder(html):
    s = 0
    open_tr_3 = html.find('class="artist"', s)
    close_tr_3: object = html.find("</tr>", open_tr_3)

    artiststring = html[open_tr_3:close_tr_3]
    lookingforartist = '<a'
    artist_start = artiststring.find(lookingforartist)
    artist_end = artiststring.find('</a>', artist_start)
    artist = (artiststring[artist_start + 52:artist_end])
    return artist

if __name__ == "__main__":
    html = scrape(url)
    print(pos_finder(html), end =' ')
    print(name_finder(html), end =' ')
    print(artist_finder(html),)

