#WEB SCRAPPER
import requests as rst
import bs4

class WebScrapper:
    def __init__(self,url='',selector=''):
        self.url = url
        self.selector = selector
        self.scrap_page = None
        self.scrap_objs = None
    
    def __str__(self):
        return f"url = {self.url}\n selector = {self.selector}"

    def get_page(self):
        url = self.url
        selector = self.selector
        page = rst.get(url)
        if page.status_code == 200:
            self.scrap_page = bs4.BeautifulSoup(page.text,'html.parser')
            self.scrap_objs = self.scrap_page.select(selector)
            return 1
        else:
            return 0
    def get_items_html(self,url,selector):
        self.url = url
        self.selector = selector
        objs = ['Erro ao aceder a pagina ,por favor confirme a url']
        if self.get_page() == 1:
            objs = []
            for obj in self.scrap_objs:
                objs.append(str(obj))
        return objs

    def get_items_text(self,url,selector):
        self.url = url
        self.selector = selector
        objs = ['Erro ao aceder a pagina ,por favor confirme a url']
        if self.get_page() == 1:
            objs = []
            for obj in self.scrap_objs:
                objs.append(obj.getText())
        return objs
    
