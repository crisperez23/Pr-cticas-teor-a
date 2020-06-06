import re

expresion = r'^([A-Za-z0-9]+)([@])([a-z]+)([.])([a-z]+)$'
resultado = re.compile(expresion)
prueba = raw_input("entrada: ")
busqueda=re.search(resultado,prueba)

if busqueda:
    print busqueda.group()
else:
    print"qr"
