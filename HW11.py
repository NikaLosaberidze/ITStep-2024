import requests

url = "https://fakestoreapi.com/products"

def get_data():
    return requests.get(url).json()



def fetch_data(my_data):
    prices = []
    min,max = float("inf"),0

    categories = set()

    product_brief = {}

    ratings = []


    for product in my_data:
        curPrice = product['price']
        if max < curPrice:
            max = curPrice
        elif min > curPrice:
            min = curPrice

        prices.append(curPrice)


        categories.add(product['category'])


        product_brief[product['title']] = product['id']
        
        ratings.append(product['rating']['rate'])


    product_brief = {k : product_brief[k] for k in sorted(product_brief)}


    print(f"Prices: {prices}\nMax Price: {max}, Min Price:{min}" + "\n")
    print(f"Categories: {sorted(categories)}" + "\n")
    print(f"Products With Ids: {product_brief}" + "\n")
    print(f"Rating: {sorted(ratings)}")




fetch_data(get_data())