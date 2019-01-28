import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
con = 0
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')# Solicitud de la direccion web
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser') # El analizador de beautiful inicia a procesar
# Retrieve all of the anchor tags
tags = soup('a')
busqueda(url,tags)

for tag in tags:
    con = con + 1
    

def busqueda(url, tags):
    for tag in tags: 
    con = con + 1
    c = con / 3
    if con == 1:
        url = tag.get('href', None)
        name = tag.contents[0]
        