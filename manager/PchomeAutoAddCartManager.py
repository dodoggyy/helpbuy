import requests
import re
import time
import multiprocessing as mp
from time import sleep
from utility.KeyDefine import KeyDefine as KEY


class PayLoad:
    # 商品網址代碼
    ITEM_ID = "DGBJCW-A900AIN4C-000"


data = 'data=%7B%22G%22%3A%5B%5D%2C%22A%22%3A%5B%5D%2C%22B%22%3A%5B%5D%2C%22TB%22%3A%2224H%22%2C%22TP%22%3A1%2C%22T%22%3A%22ADD%22%2C%22TI%22%3A%22AAAA%22%2C%22RS%22%3A%22DGBJCI%22%2C%22YTQ%22%3A1%7D'
origin_item_url = "AAAA"
data = data.replace(origin_item_url, PayLoad.ITEM_ID)


def main():
    while True:
        sleep(0.2)
        print(time.asctime(time.localtime(time.time())))
        r1 = requests.post(KEY.PCHOME_URL_REQUEST, data=data,
                           headers=KEY.PCHOME_HEADER)
        print(r1.status_code)
        # print(r1.text)
        request_text = str(r1.text)
        result = re.search(r'"PRODTOTAL":(\d*)', request_text)
        if (int(request_text[result.regs[1][0]:result.regs[1][1]])):
            break


def job(x):
    while True:
        sleep(0.2)
        print(time.asctime(time.localtime(time.time())))
        r1 = requests.post(KEY.PCHOME_URL_REQUEST, data=data,
                           headers=KEY.PCHOME_HEADER)
        print(r1.status_code)
        # print(r1.text)
        request_text = str(r1.text)
        result = re.search(r'"PRODTOTAL":(\d*)', request_text)
        if (int(request_text[result.regs[1][0]:result.regs[1][1]])):
            break


def multi_process():
    pool = mp.Pool()
    pool.map(job, range(KEY.PCHOME_TOTAL_PROCESS))


if __name__ == '__main__':
    main()
    # multi_process()
