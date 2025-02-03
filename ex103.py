import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com')
except urllib.error.URLError:
    print('O site youtube não pode ser conectado')
else:
    print('ok')
