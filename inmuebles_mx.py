import requests
import csv
from bs4 import BeautifulSoup

#salida del archivo
f = csv.writer(open('inmuebles_mx.csv', 'w'))
f.writerow(['Categoria', 'Localidad', 'Colonia', 'Precio'])

paginas=[]

for i in range(1,10):
    url = "https://www.avisosdeocasion.com/reforma/venta/casas/casas.aspx?ntext=venta-casas-casas-Distrito-Federal&PlazaBusqueda=1&Plaza=1&pagina=" +str(i)
    paginas.append(url)

    for pagina in paginas:
        
        page = requests.get(pagina)
        soup = BeautifulSoup(page.content, 'html.parser')

        lista_anuncios = soup.find_all('td', class_="tituloresultchico")

        for anuncios_items in lista_anuncios:
            titulos = anuncios_items.contents[0]
            categoria = anuncios_items.find('h3').get_text()
            localidad=anuncios_items.find('h4').get_text()
            colonia = anuncios_items.find('h5').get_text()
            detalle = anuncios_items.find('tr')
            precio = detalle.find('td').get_text()
            nprecio = precio.replace ("|", "")

            # Agrega cada información del anuncio de inmuebles a un registro del archivo de salida

            f.writerow([categoria, localidad, colonia, nprecio])

            #print(titulos)
            #print(localidad)
            #print(colonia)
            #print (nprecio)

