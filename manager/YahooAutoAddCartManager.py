import requests
import json
import multiprocessing as mp
from utility.KeyDefine import KeyDefine as KEY


class PayLoad:
    # 宅配 :      10
    # 超商快取:   20
    # 快速到貨:   30
    DELIVER_TYPE = 30
    # 商品編號
    ITEM_ID = 8435376


data_deliver = {"type": "CALL_RESERVICE",
                "payload": {"isStoreProduct": "false", "checkoutAction": "AddToCart", "cartType": "",
                            "itemLines": [{"productBundleId": "", "quantity": 1}], "isMobile": "false",
                            "authToken": ""},
                "reservice": {"name": "FETCH_CHECKOUT_ADD_TO_CART_RESULT",
                              "start": "FETCH_CHECKOUT_ADD_TO_CART_START",
                              "state": "CREATED"}}


def init_config():
    data_deliver['payload']['cartType'] = str(PayLoad.DELIVER_TYPE)
    data_deliver['payload']['itemLines'][0]['productBundleId'] = str(PayLoad.ITEM_ID)
    # print(data_deliver['payload']['itemLines'][0]['productBundleId'])
    data_deliver['payload']['authToken'] = KEY.YAHOO_AUTH_TOKEN
    return data_deliver


def main():
    data = init_config()
    while True:
        r1 = requests.put('https://tw.buy.yahoo.com/ssfe/_service_/', data=json.dumps(data),
                          headers=KEY.YAHOO_HEADER)
        print(r1.status_code)
        # print(r1.text)


def job(x):
    data = init_config()
    while True:
        r1 = requests.put('https://tw.buy.yahoo.com/ssfe/_service_/', data=json.dumps(data),
                          headers=KEY.YAHOO_HEADER)
        print("Process:", x, "status:", r1.status_code)
        # print(r1.text)


def multi_process():
    pool = mp.Pool()
    pool.map(job, range(KEY.YAHOO_TOTAL_PROCESS))


if __name__ == '__main__':
    # main()
    multi_process()
