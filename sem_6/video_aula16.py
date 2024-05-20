"""JSON:
JSON (JavaScript Object Notation) define um
formato padrão para descrever, em formato
texto, objetos como dicionários, listas,
números e strings.
A maioria das linguagens de programação
possui bibliotecas para produzir e processar
dados no formato JSON.
"""

import json

d = dict()
d['a'] = 1
d['b'] = 2
d['c'] = [3,4]
jd = json.dumps(d)
print(jd)

dd = json.loads(jd)
print(dd)

print(type(jd))
print(type(d))