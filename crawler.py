import requests
from bs4 import BeautifulSoup
import time
import random
# from selenium import webdriver
import re

class Crawler:
    
    # def __init__(self):
    #     # self.__headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    #     # self.__driver = webdriver.Chrome()


    def __get_page(self, url, dynamically_generated):
        # if dynamically_generated:
        #     self.__driver.get(url)
        #     time.sleep(10)
        #     html = self.__driver.page_source
        # else:
        try:
            req = requests.get(url)
            if req.status_code != 200:
                return None
            else:
                html = req.text
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(html, 'html.parser')

    def __safe_get(self, page_obj, selector):
        child_obj = page_obj.select(selector)
        if len(child_obj) > 0:
            return child_obj[0]
        return None
    
    def __perform_random_delay(self, delay = 3, random_offset = .5):
        time.sleep(delay + random.uniform(0,random_offset))

    def __match(self, game_name, product_name):
        modified_game_name = re.sub('[-()!.:,\'’]', '', game_name)
        game_name_words = modified_game_name.split(' ')
        game_name_words = list(map(lambda word: word.strip().lower(), game_name_words))
        modified_product_name = re.sub('[-()!.:,\']', '', product_name)
        product_name_words = modified_product_name.split(' ')
        product_name_words = list(map(lambda word: word.strip().lower(), product_name_words))
        return set(game_name_words).issubset(product_name_words)
        
    
    def __find_game(self, search_results, game_name, site):
        i=0
        while i<len(search_results):
            result = search_results[i]
            product_name = self.__get_text(result,site.name_selector)
            valid_game = self.__valid_game(game_name, product_name, site, result)
            if valid_game:
                return result
            i+=1
        return None

    def __valid_game(self, game_name, product_name, site, result):
        if self.__match(game_name, product_name):
            if site.check_game_selector:
                check_game_value = self.__safe_get(result, site.check_game_selector)
                if site.check_game_function(check_game_value):
                    return True
            else:
                return True
        else:
            return False
    
    def __get_text(self, result, selector):
        tag = self.__safe_get(result, selector)
        if tag: return tag.text
        else: return ''


    def search(self, game_name, site):
        url = site.search_url + game_name

        bs = self.__get_page(url, site.dynamically_generated)
        if bs is not None:
            search_results = bs.select(site.results_selector)
            game = self.__find_game(search_results, game_name, site)
            if game:
                price = self.__get_text(game, site.price_selector)
            else:
                price = None
            self.__perform_random_delay()
            return price
        else:
            self.__perform_random_delay()
            return None
