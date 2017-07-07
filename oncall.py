import sys
import urllib3
from html.parser import HTMLParser
import os
import codecs

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_h3 = False
        self.in_a = False
        self.urls = []

    def handle_starttag(self, tag, attrs):
        if tag == "h3":
            self.in_h3 = True
        if tag == "a" and self.in_h3:
            self.in_a = True
            self.urls.append(attrs[0][1])

    def handle_endtag(self, tag):
        if tag == "h3":
            self.in_h3 = False
        elif tag == "a":
            self.in_a = False

    def get_urls(self):
        return self.urls

class StoryParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_body = False
        self.body = ""

    def handle_starttag(self, tag, attrs):
        if tag == "div" and attrs[0][1] == "body":
            self.in_body = True
            self.body += self.get_starttag_text()
        elif tag == "div" and attrs[0][1] == "article_body_btm":
            self.in_body = False
        elif self.in_body:
            self.body += self.get_starttag_text()

    def handle_endtag(self, tag):
        if self.in_body:
            self.body += "</" + tag + ">"

    def handle_data(self, data):
        if self.in_body:
            self.body += data

    def get_body(self):
        return self.body

if len(sys.argv) > 1:
    pages = int(sys.argv[1]) + 1
else:
    pages = 8

http = urllib3.PoolManager()
page = "http://www.theregister.co.uk/Tag/on-call?page={0}"

urls = []
for i in range(1, pages):
    print("Checking out page", i)
    r = http.request("GET", page.format(i))
    parser = PageParser()
    parser.feed(str(r.data))
    urls.extend(parser.get_urls())

beginning = """<!DOCTYPE html>
<html>
  <head>
    <title>On call</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
            """
end = """</body>
</html>
"""
if not os.path.exists("html"):
    os.makedirs("html")
lname = len(str(len(urls)))
for i, url in enumerate(reversed(urls)):
    print("Downloading {0}/{1}: {2}".format(i + 1, len(urls), url))
    r = http.request("GET", "http://www.theregister.co.uk" + url)
    parser = StoryParser()
    parser.feed(r.data.decode("utf-8"))
    body = beginning + parser.get_body() + end
    filename = "html/{0}.html".format(str(i + 1).zfill(lname))
    with codecs.open(filename, 'w', "utf-8-sig") as f:
        f.write(body)
