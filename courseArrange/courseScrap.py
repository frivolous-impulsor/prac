from urllib.request import urlopen
import re
from bs4 import BeautifulSoup

courseInstance = urlopen("https://kurser.ku.dk/course/ndak23003u/2024-2025")
courseByte = courseInstance.read()
courseCode = courseByte.decode('utf-8')

soup = BeautifulSoup(courseCode, "html.parser")
title = soup.find("h1").string
print(title)

pattern = "<dd>Block .</dd>"
searchResult = re.search(pattern, courseCode)
result = searchResult.group()
result = re.sub("<dd>Block ", "", result)
result = re.sub("</dd>", "", result)
print(result)
