import requests
from bs4 import BeautifulSoup
import urllib


page = requests.get('http://hackbulgaria.com')
html_text = page.text

print(html_text)
print(page.json())


def scan_page(url):
    if url in scanned_urls:
        return

    scanned_urls.append(url)
    print(url)
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html)
    for link in soup.find_all('a'):
        if 'http' not in link.get('href') and '..' not in link.get('href'):
            scan_page(base_url + link.get('href'))


def is_outgoing(url):
    if base_url in url:
        return False
    return True


def prepare_link(url, href):
    return urllib.parse.urljoin(url, href)


scanned_urls = []
base_url = "http://hackbulgaria.com"
scan_page(base_url)
