from  web_scrapper import WebScrapper


wb = WebScrapper()

#Busca Artigos no Jornal de Angola
url = 'http://jornaldeangola.sapo.ao/'
selector = 'article>a'
#Resultado em HTML
#result = wb.get_items_html(url,selector)
#print(result)
#print('\n')
#Resultado em Texto
#result = wb.get_items_text(url,selector)
#print(result)

#Busca Cambios Bna
url = 'http://www.bpc.ao/bpc/pt/'
selector = '.cambio'
#Resultado em HTML
result = wb.get_items_html(url,selector)
print(result)
#Resultado em Texto
result = wb.get_items_text(url,selector)
print('\n')
print(result)
