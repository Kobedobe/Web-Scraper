from website import Website
from crawler import Crawler
from data import *

crawler = Crawler()
siteData = [['STEAM', 'https://store.steampowered.com/', 'https://store.steampowered.com/search/?term=', '#search_resultsRows>a', '.title', '', 
                None, 'div.discount_final_price', False, ['PC', 'PlayStation 5']]]
# ['Amazon', 'https://www.amazon.co.uk/', 'https://www.amazon.co.uk/s?k=', 'span[data-component-type="s-search-results"] div[data-component-type="s-search-result"]', 
#              'div[data-cy="title-recipe"]>h2 span', 'div[data-cy="title-recipe"] div.a-row span.a-size-base', lambda tag: True if tag and 'PEGI Rating:' in tag.text else False,
#              'div[data-cy="price-recipe"] span.a-price span.a-offscreen', False, ['Nintendo Switch', 'PC', 'PlayStation 5']],
#             ['Argos', 'https://www.argos.co.uk/', 'https://www.argos.co.uk/search/', 'div[data-test="product-list"] div[data-test="component-product-card"]',
#              'div[data-test="component-product-card-title"]', 'div[data-test="component-product-card-title"]', lambda tag: True if tag and 'Game' in tag.text else False,
#              'div[data-test="component-product-card-price"] strong', False, ['Nintendo Switch', 'PC', 'PlayStation 5']],
# ['CEX', 'https://uk.webuy.com/', 'https://uk.webuy.com/search?stext=', 'div.search-result-grid>div', 'div.card-title>a', 'div.card-subtitle', 
# lambda tag: True if tag and 'Games' in tag.text else False, 'p.product-main-price',True, ['Nintendo Switch', 'PC', 'PlayStation 5']],
# ['Currys', 'https://www.currys.co.uk/', 'https://www.currys.co.uk/search?q=', 'div.product-item-element', 'h2.pdp-grid-product-name', 'div.ratings', 
#                  lambda tag: True if tag else False, 'div.price-info span.value',False],
# ['Very', 'https://www.very.co.uk/', 'https://www.very.co.uk/e/q/', 'div[id=product-listing-root] div[data-testid=gallery-product-card]', 'div.productInfo h3[data-testid="fuse-complex-product-card__title"]', '', 
#                  None, 'div.productInfo div[data-testid="fuse-complex-product-card__price"]>h4', True],
# ['Smyths Toys', 'https://www.smythstoys.com/uk/en-gb', 'https://www.smythstoys.com/uk/en-gb/search/?text=', 'div.item-panel div.details', 'h5 span.name', 
#                  '', None, 'div.price span', True, ['Nintendo Switch', 'PC', 'PlayStation 5']],
sites = []
for row in siteData:
    sites.append(Website(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))

for filename in dataframes:
    prices = []
    df =dataframes[filename]
    for index, game in df.iterrows():
        for site in sites:
            if console in site.consoles:
                price = crawler.search(game['Game'], site)
                if price is not None: 
                    prices.append(price)
                    print(price)
                else: prices.append(game['Price'])
    df['Price'] = prices
    df.to_csv(filename, index=False)
    

# for site in sites:
#     prices = []
#     for console in console_data:
#         for game in console_data[console]:
#             price = crawler.search(game['Game'], site)
#             if price is not None:
#                 prices.append(price)
#             else: prices.append(game['Price'])
