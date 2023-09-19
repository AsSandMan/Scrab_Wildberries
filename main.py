import pandas as pd
import requests


    
def get_category():

    url = 'https://catalog.wb.ru/catalog/bl_shirts/catalog?appType=1&cat=8126&curr=rub&dest=-1257786&page=1&regions=80,38,83,4,64,33,68,70,30,40,86,75,69,1,31,66,110,48,22,71,114&sort=priceup&spp=30'
        

    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Host': 'catalog.wb.ru',
        'Origin': 'https://www.wildberries.ru',
        'Referer': 'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/bluzki-i-rubashki',
        'Sec-Ch-Ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',

    }

    response = requests.get(url=url, headers=headers)

    return response.json()



def prepare_items(response):
    products = []

    products_raw = response.get('data', {}).get('products', None)

    if products_raw != None and len(products_raw) > 0:
        for product in products_raw:
            products.append({
                'brand': product.get('brand', None),
                'name': product.get('name', None),
                'id': product.get('id', None),
                'sale': product.get('sale', None),
                'priceU': float(product.get('priceU', None)) / 100 if product.get('priceU', None) != None else None,
                'salePriceU': float(product.get('salePriceU', None)) / 100 if product.get('salePriceU', None) != None else None,

            })

    return products

def main():
    response = get_category()
    products = prepare_items(response)

    pd.DataFrame(products).to_csv('products.csv', index=False)

if __name__ == '__main__':
    main()