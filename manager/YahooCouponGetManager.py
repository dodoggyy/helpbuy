import requests
import json
import time
import copy
import multiprocessing as mp
from utility.KeyDefine import KeyDefine as KEY

coupon_id = {"type": "CALL_RESERVICE", "payload": {"campaignId": "", "authToken": "", "viewCode": ""},
             "reservice": {"name": "ACQUIRE_COUPON_PMO", "state": "CREATED"}}

coupon_id_list = [
    262732,
    262734,
    262739,
    262741,
]

coupon_id1 = copy.deepcopy(coupon_id)
coupon_id2 = copy.deepcopy(coupon_id)
coupon_id3 = copy.deepcopy(coupon_id)
coupon_id4 = copy.deepcopy(coupon_id)

coupon_list = [
    coupon_id1,
    coupon_id2,
    coupon_id3,
    coupon_id4
]


def init_coupon():
    for i in range(len(coupon_id_list)):
        coupon_list[i]["payload"]["authToken"] = KEY.YAHOO_AUTH_TOKEN
        coupon_list[i]['payload']['campaignId'] = str(coupon_id_list[i])


def job(x):
    item = x % len(coupon_list)
    while True:
        r = requests.post('https://tw.buy.yahoo.com/morder/_reservice_/', data=json.dumps(coupon_list[item]),
                          headers=KEY.YAHOO_HEADER)
        mStr = str(r.content)
        if 'Acquired coupon is invalid' in mStr:
            localtime = time.asctime(time.localtime(time.time()))
            print("item:", item, "process:", x, "Waiting", localtime)
            continue
        else:
            localtime = time.asctime(time.localtime(time.time()))
            print("item:", item, "process:", x, "limit reached", localtime)
            # break


def multi_process():
    pool = mp.Pool()
    pool.map(job, range(KEY.YAHOO_TOTAL_PROCESS))


def main():
    init_coupon()
    print(coupon_list)
    pass


if __name__ == '__main__':
    # main()
    multi_process()
