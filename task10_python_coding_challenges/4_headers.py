import requests as req
import re

if __name__ == '__main__':
    url = 'https://en.wikipedia.org/wiki/Main_Page'
    response = req.get(url)
    headers = response.headers
    html = response.text

    pattern1 = "mw-headline.*span"
    pattern2 = ">.*<"
    raw_header_html = re.findall(pattern1, response.text)
    headers = [ re.findall(pattern2, header)[0][1:][:-1] for header in raw_header_html]
    print("Wikipedia website headers:")
    for h in headers:
        print(" ",h)
    
    