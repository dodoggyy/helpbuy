import requests
import json
import datetime
from time import sleep

my_data = {"voucher_code": "28FGM07"}
sequences = ["%.2d" % i for i in range(0, 10000)]

coupon = ['LLRUFNZ4X',
          'JCDD68PHX',
          '84EAEE9DH',
          '44LGU983U',
          'FVK7M8MXP',
          'WJ7ZTA45W',
          'E2RMPMBY9',
          'DAF9S58NN',
          'ZX4JW9LMX',
          'LFGJBNJHB',
          'GMYDJGA9J',
          'NABADSE6E',
          'PDMWT2WT2',
          'B78CAATP4',
          '99GU4RJ6S',
          'V3CLR9M3H',
          'TZTE484ZB',
          'S9DZD7S58',
          '7GBBMEQ2S',
          'C86NNRYXL',
          'EX9AHNNCN',
          'VPD78D4KV',
          '527HHEYKE',
          'P8SESJPAL',
          'QMMDHMPBE',
          '3DRHK5587',
          'K67RBFH6Y',
          'YFP58G3KQ',
          '2TGTLKMSQ',
          '6PNZYQKS7'
          ]

coupon2 = ['24HLFSA1106']

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
mStr = ''
record_item = []
record_time = []

for seq in sequences:
    print(datetime.datetime.now())
    print(record_item)
    print(record_time)
    for i in list(coupon):
        # voucher = "28AKV01"
        payload = {"voucher_code": i}
        r = requests.post('https://shopee.tw/api/v2/voucher_wallet/save_voucher', data=json.dumps(payload),
                          headers=headers)
        # print(i, r.text)
        mStr = str(r.text)
        # print(mStr)
        # print(i,j,k, seq)
        if '\"error\":null' in mStr:
            record_item.append(i)
            record_time.append(str(datetime.datetime.now()))
            print(i)
            print(mStr)
    sleep(1)
