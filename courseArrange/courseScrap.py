from urllib.request import urlopen
import re
from bs4 import BeautifulSoup


def searchCourse():
    "todo"

def fetchCourse(url: str):
    courseInstance = urlopen(url)
    courseByte = courseInstance.read()
    courseCode = courseByte.decode('utf-8')
    #title
    soup = BeautifulSoup(courseCode, "html.parser")
    title = soup.find("h1").string
    print(title)

    #content
    courseContent = ""
    contentSoup = soup.find("div", id="course-content")
    contents = contentSoup.findAll('p')
    for content in contents:
        courseContent += content.string
    print(courseContent)

    #block number
    pattern = "<dd>Block .</dd>"
    searchResult = re.search(pattern, courseCode)
    result = searchResult.group()
    result = re.sub("<dd>Block ", "", result)
    result = re.sub("</dd>", "", result)
    print(result)


 