#WEB SCRAPPER
import requests as rst
from selenium import webdriver
import chromedriver_binary
import time
import bs4

class WebScrapper:
    def __init__(self,url='',selector=''):
        self.url = url
        self.selector = selector
        self.scrap_page = None
        self.scrap_objs = None
        self.html= None
    
    def __str__(self):
        return f"url = {self.url}\n selector = {self.selector}"
    
    def get_from_selenumum(self,url):
        if url == self.url:
            return self.html
        else:
            driver = webdriver.Chrome()
            driver.get(url)
            html = driver.page_source
            self.html = html
            self.url = url
            driver.close()
            return html

    def get_page(self,url):
        selector = self.selector
        page = rst.get(url)
        if page.status_code == 200:
            html = self.get_from_selenumum(url)
            self.scrap_page = bs4.BeautifulSoup(html,'html.parser')
            self.scrap_objs = self.scrap_page.select(selector)
            return 1
        else:
            return 0
    def get_items_html(self,url,selector):
        self.selector = selector
        objs = ['Erro ao aceder a pagina ,por favor confirme a url']
        if self.get_page(url) == 1:
            objs = []
            for obj in self.scrap_objs:
                objs.append(str(obj))
        return objs

    def get_items_text(self,url,selector):
        self.selector = selector
        objs = ['Erro ao aceder a pagina ,por favor confirme a url']
        if self.get_page(url) == 1:
            objs = []
            for obj in self.scrap_objs:
                objs.append(obj.getText())
        return objs
    
