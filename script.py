#pdf2txt.py -t html Profile.pdf > Profile.html

from pyquery import PyQuery as pq

with open("Profile.html", "r") as f:
    contents = f.read()
    # print contents
    doc = pq(contents)
    text = doc('span[style="font-family: EAAAAA+ArialUnicodeMS; font-size:36px"]').text()
    print text

