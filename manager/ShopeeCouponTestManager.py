import requests
import json
import datetime
from time import sleep
from utility.KeyDefine import KeyDefine as KEY

my_data = {"voucher_code": "28FGM07"}
sequences = ["%.2d" % i for i in range(0, 10000)]

coupon = ['6U8D52QH2',
          'UH35ZT3B5',
          '83YPCPPTL',
          'BE28T7E3Q',
          'X5ENF34LT',
          'Z5ENF34LT',
          'R5CMJ9M8M',
          'WFFJCB4VG',
          '3BC6M8JMH',
          'HBJQJR8RQ',
          'JKD7YKYDN',
          'RTMSLVSVP',
          '45DZWGY53',
          'AUWVL7Y78',
          '5AG4W9XVE',
          'TDHT3BFL4',
          'GEV7MY4J4',
          'ECXH375K3',
          '53NCEEW34',
          'ZGS2KTKVR',
          'GMKWNU2D2',
          '8LSS7GZJ2',
          'HU3DKA7DL',
          '2UW4RV2YC',
          'AJWJXJ8XV',
          '4FZPME9EC',
          'J974GRPNS',
          'XPP9S9KHF',
          'DTWL5D2X2',
          '4FZX2SHHE',
          'PV3APWUD9',
          'N9E3768EA',
          '26SW8ZFUW',
          'LX3Y297RF',
          'SD5Q2E4TT',
          'VAN5G2NYU',
          'FPKU5LBUL',
          'BWFNX5AR3',
          'FAHP9WSN2',
          'NWGVVUYMW',
          'QDTKF6W93',
          'KKTE7RCYB',
          'VWH8V6GA6',
          'XYEGCASH9',
          '6QRPZBLCL',
          'D6VMADTJQ',
          '5Z33CB29U',
          'TSHKYPK56',
          'MN2D8UGFB',
          'QUT7CKRVW',
          'NTVFBNR76',
          'YW2H5RGNE',
          '9WRP2AJRN',
          'ZMAS2VGCC',
          'T27VVCGRE',
          '9EFRWNSFR',
          'KS4K9HR6Y',
          '7L23CYJUA',
          'V3S5WV6X8',
          'LNLYPP6HM',
          'DLTCVJTGH',
          'CJM97RXT7',

          ]

coupon2 = ['24HLFSA1106']

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
                          headers=KEY.SHOPEE_HEADER)
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
