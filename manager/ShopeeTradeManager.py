import requests
import json
import time
import multiprocessing as mp
from utility.KeyDefine import KeyDefine as KEY
from time import sleep


process_strategy_single = False

## JSON file
file_name_list = ['cart1',
 #                 'cart2',
 #                 'cart3',
 #                 'cart4',
 #                 'cart5',
 #                 'cart6',
 #                 'cart7',
 #                 'cart8',
 #                 'cart9',
 #                 'cart10',
 #                 'cart11',
 #                 'cart12',
                  ]
## voucher code
voucher_list = ['D6VMADTJQ',
                'AJWJXJ8XV',
                'PV3APWUD9',
                '45DZWGY53',
                'JKD7YKYDN',
                'VAN5G2NYU',
                'KKTE7RCYB',
                'HBJQJR8RQ',
                'VWH8V6GA6',
                '6QRPZBLCL',
                '2UW4RV2YC',
                'DTWL5D2X2',
                ]


store_list = []


def load_file():
    payload_list = []
    index = 0
    for file in file_name_list:
        input_file_tmp = open(KEY.JSON_PATH + file + ".json", "r", encoding="utf-8")
        payload_tmp = json.load(input_file_tmp)
        payload_tmp["promotion_data"]["voucher_code"] = voucher_list[index]
        index += 1
        payload_list.append(payload_tmp)
    return payload_list


def execute_cart_post(payload, delay):
    request_cart = requests.post(KEY.SHOPEE_URL_CART, data=json.dumps(payload), headers=KEY.SHOPEE_HEADER)
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
    request_checkout = requests.post(KEY.SHOPEE_URL_CHECKOUT, data=json_array, headers=KEY.SHOPEE_HEADER)
    print(request_checkout)
    return True


def job_exec_all(x):
    payload_list = load_file()
    time_start = time.time()
    while True:
        for payload in payload_list:
            print(time.asctime(time.localtime(time.time())))
            success = execute_checkout_post(execute_cart_post(payload, 0))
            time_end = time.time()
            print("process:", x, payload["promotion_data"]["voucher_code"])
            print("%f sec" % (time_end - time_start))
            time_start = time.time()
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
        pool.map(job_exec_single, range(KEY.SHOPEE_TOTAL_PROCESS))
    else:
        pool.map(job_exec_all, range(KEY.SHOPEE_TOTAL_PROCESS))


def main():
    payload_list = load_file()
    time_start = time.time()
    while True:
        for payload in payload_list:
            print(payload["promotion_data"]["voucher_code"])
            success = execute_checkout_post(execute_cart_post(payload, 0))
            time_end = time.time()
            print("%f sec" % (time_end - time_start))
            time_start = time.time()
            if success:
                payload_list.remove(payload)
            print("\n\n\n")
        if not payload_list:
            break


if __name__ == '__main__':
    # main()
    multi_process()
