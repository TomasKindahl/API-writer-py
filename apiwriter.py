import sys
import requests
import time

def main(address):
    url = f'{address}/products'
    res = requests.get(url)
    print('STATUS:', res.text)
    while True:
        url = f'{address}/products'
        res = requests.post(url, json={"id": 666, "name": f"Nero", "price": 666})
        print('SET:', res.text)
        time.sleep(1)
        for i in range(145,155):
            url = f'{address}/products'
            res = requests.post(url, json={"id": i, "name": f"item{i}", "price": i*2})
            print('SET:', res.text)
            time.sleep(1)
        for i in range(145,155):
            url = f'{address}/products/{i}'
            res = requests.delete(url)
            print('DELETE:', res.text)
            time.sleep(1)
        url = f'{address}/products/666'
        res = requests.delete(url)
        time.sleep(10)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python apiwriter /serveraddress/")
        print(" e.g.: python apiwriter http://localhost:5070")
    else:
        serveraddress = sys.argv[1]
        main(serveraddress)
