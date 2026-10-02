import urllib.request, re

url = 'https://potudo-ff-ob54.netlify.app/'
html = urllib.request.urlopen(url).read().decode('utf-8')
print('Downloaded HTML, length:', len(html))
