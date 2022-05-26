from bs4 import BeautifulSoup
import requests
import lxml


def parse_xml():
    url = "http://upload.itcollege.ee/~aleksei/test.xml"
    xml_content = requests.get(url).content
    soup = BeautifulSoup(xml_content, 'xml')

    find_data = soup.find_all('data')
    for data in find_data:
        text = data.get_text().strip()
        return text

print(parse_xml())
