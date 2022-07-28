from urllib import response
import urllib.request
url = 'http://www.blog.pythonlibrary.org/wp-content/uploads/2012/06/wxDbViewer.zip'
response = urllib.request.urlopen(url)
data = response.read()
with open('test.zip', 'wb') as fobj:
    fobj.write(data)