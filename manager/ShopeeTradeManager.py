import requests
import json
import time
import multiprocessing as mp
from time import sleep

url_cart = 'https://shopee.tw/api/v2/checkout/get'
url_checkout = 'https://shopee.tw/api/v2/checkout/place_order'

json_path = "../conf/"
total_process = 8

process_strategy_single = False

## JSON file
file_name_list = ['cart1',
                  'cart2',
                  'cart3',
                  'cart4',
                  'cart5',
                  'cart6',
                  'cart7',
                  ]
## voucher code
voucher_list = ['24HALLC1109',
                '2TGTLKMSQ',
                'VPD78D4KV',
                'NABADSE6E',
                'FVK7M8MXP',
                'ZX4JW9LMX',
                '84EAEE9DH',
                ]

headers = {
    'Accept': 'application/json',
    'Cookie': 'SPC_EC="gIXTlrzZJ9rNVXDvqgkaAlLYHP/jD5Cscj9R1araEAzbQO+5vdFBfnQYGphLfuiIt8/ss4+gdLBNcPCdczWdJv730WtU7wuZ7s/0znsGOYWlkM05E0yGeHs3feEX1Upgq4upQpSo8axtNayNDUVyzzdKzO8ZTs3fEwfLJRgfXCE="; SPC_F=gEeA5Hdl1OInMbtUPKcKXRG5FuitOtkZ; REC_T_ID=df605bf0-e049-11e8-913a-3c15fb7e9f4a; SPC_T_ID="hGEp9SCS+GJ2hBfxzKuOtMh8mNiDUx3TgWm6mSXJL7m1sEpRFeC8BjlU9Fe9COzvJLDejq+OKDDzxebnzociLjogZS+kHsigQTdvTEbkqgY="; SPC_U=25360609; SPC_T_IV="K28PmvmW+e/U8MOJikfrOA=="; __BWfp=c1541346848325x3885467b4; _ga=GA1.2.1330090153.1541346849; cto_lwid=d48a465c-b634-40de-8f38-64f154604d77; cto_idcpy=97b2ccca-73e4-46e0-9b13-fe57b00a8b0c; _gcl_au=1.1.1181527693.1572119206; _fbp=fb.1.1572119206355.1560323436; SPC_SI=ziclg2sr3w9c66wsu3rkvxz8jj38taw4; _gid=GA1.2.100707063.1572538274; csrftoken=c70HYFrIqyWbY8AvXXVLZ7hwvNE4ceUH; SPC_IA=1; welcomePkgShown=true; SPC_SC_TK=8ac6f660f871a90e904317a3b218c0ad; UYOMAPJWEMDGJ=; SPC_SC_UD=25360609; SPC_SC_SA_TK=; SPC_SC_SA_UD=; AMP_TOKEN=%24NOT_FOUND; REC_MD_20=1572803021; _dc_gtm_UA-61915057-6=1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
    'Origin': 'https://shopee.tw',
    'Referer': 'https://shopee.tw/user/voucher-wallet/?type=0',
    'Host': 'shopee.tw',
    'X-API-SOURCE': 'pc',
    'X-CSRFToken': 'c70HYFrIqyWbY8AvXXVLZ7hwvNE4ceUH',
    'X-Requested-With': 'XMLHttpRequest',
};

store_list = []


def load_file():
    payload_list = []
    index = 0
    for file in file_name_list:
        input_file_tmp = open(json_path + file + ".json", "r", encoding="utf-8")
        payload_tmp = json.load(input_file_tmp)
        payload_tmp["promotion_data"]["voucher_code"] = voucher_list[index]
        index += 1
        payload_list.append(payload_tmp)
    return payload_list


def execute_cart_post(payload, delay):
    request_cart = requests.post(url_cart, data=json.dumps(payload), headers=headers)
    # print(request_cart.status_code)
    json_array = request_cart.text
    # print(json_array)
    try:
        json_array2 = json.loads(json_array)
    except ValueError:
        print("ValueError")
        return None
    # print(json_array)
    json_array2.setdefault("checkout_price_data")
    try:
        promocode_valid = bool(json_array2["checkout_price_data"]["promocode_applied"] is not None)
    except:
        promocode_valid = False
        print("exception")
    print(promocode_valid)
    # print(time.asctime(time.localtime(time.time())))

    sleep(delay)
    if not (promocode_valid):
        return None
    else:
        return json_array


def execute_checkout_post(json_array):
    if json_array == None:
        return False
    request_checkout = requests.post(url_checkout, data=json_array, headers=headers)
    print(request_checkout)
    return True

def job_exec_all(x):
    payload_list = load_file()
    tStart = time.time()
    while True:
        for payload in payload_list:
            print(time.asctime(time.localtime(time.time())))
            success = execute_checkout_post(execute_cart_post(payload, 0))
            tEnd = time.time()
            print("process:", x, payload["promotion_data"]["voucher_code"])
            print("%f sec" % (tEnd - tStart))
            tStart = time.time()
            if success:
                payload_list.remove(payload)
            print("\n\n\n")
        if not payload_list:
            break

def job_exec_single(x):
    payload_list = load_file()
    item = x % len(payload_list)
    tStart = time.time()
    while True:
        print(time.asctime(time.localtime(time.time())))
        success = execute_checkout_post(execute_cart_post(payload_list[item], 0))
        tEnd = time.time()
        print("process:", x, payload_list[item]["promotion_data"]["voucher_code"])
        print("%f sec" % (tEnd - tStart))
        tStart = time.time()
        if success:
            break
        print("\n\n\n")


def multi_process():
    pool = mp.Pool()
    if process_strategy_single:
        pool.map(job_exec_single, range(total_process))
    else:
        pool.map(job_exec_all, range(total_process))


def main():
    payload_list = load_file()
    tStart = time.time()
    while True:
        for payload in payload_list:
            print(payload["promotion_data"]["voucher_code"])
            success = execute_checkout_post(execute_cart_post(payload, 0))
            tEnd = time.time()
            print("%f sec" % (tEnd - tStart))
            tStart = time.time()
            if success:
                payload_list.remove(payload)
            print("\n\n\n")
        if not payload_list:
            break


if __name__ == '__main__':
    # main()
    multi_process()
