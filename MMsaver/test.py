from BeautifulSoup import BeautifulSoup as B
from BeautifulSoup import BeautifulStoneSoup as S
soup = S(open("temp.xml",'r').read())
f = open("new.xml",'w')
f.write(soup.prettify())
f.close()
