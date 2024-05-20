"""O módulo urllib.request permite requisitar e
receber recursos da Web, de modo similar a
um navegador.
A função urlopen():
-recebe como parâmetro uma URL
-formula uma requisição HTTP que será
enviada ao servidor especificado na URL
-obtém e retorna uma resposta HTTP
completa do servidor."""



"""from urllib.request import urlopen

def getSource(url):
    response = urlopen(url)
    html = response.read()
    return html.decode()

html = getSource('https://www.uol.com.br')
print(html)"""

from html.parser import HTMLParser
from urllib.request import urlopen, Request

class MyParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.n_polos = 0

    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            for attr in attrs:
                if attr[0] == 'class' and attr[1] == 'item-polos':
                    self.n_polos += 1

    def num_polos(self):
        return self.n_polos
    
    def getSource(url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
        reg_url = "https:XXXXOOOO"
        req = Request(url=url, headers=headers)
        html = urlopen(req).read()
        return html.decode()

html = 'https://univesp.br/cursos/engenharia-de-computacao'

parser = MyParser()
parser.feed(html)
parser.num_polos()