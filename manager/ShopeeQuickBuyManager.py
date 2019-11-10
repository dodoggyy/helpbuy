import requests
import json
import multiprocessing as mp


total_process = 2

json_path = "../conf/"
json_name_cart = "Quick_buy_S1.json"
json_name_checkout = "Quick_buy_S2.json"

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
    'Content-Type': 'application/json',
    'Connection': 'keep-alive',
};

my_data_list = []

# my_data0 = {"quantity":1,"checkout":"true","update_checkout_only":"false","donot_add_quantity":"false","source":"{\"refer_urls\":[\"\"]}","shopid":26022437,"itemid":1972720549}

#### example #####
# 1.
# add_on_deal_id = ''
# is_add_on_sub_item = ''
# item_group_id = ''
# itemid = 1783031836
# modelid = 2986365729
# shopid = 1546550
# index = 0
# voucher = ""
#
# 2.
# add_on_deal_id = ''
# is_add_on_sub_item = ''
# item_group_id = ''
# itemid = 784819375
# modelid = ''
# shopid = 1546550
# index = 0
# voucher = ""
#
# 3.
# add_on_deal_id = ''
# item_group_id = ''
# is_add_on_sub_item = ''
# itemid = 1406607303
# modelid = 1958485669
# shopid = 7333053
# index = 0
# voucher = 'C7PHKJ6W7'
#

item1 = {"add_on_deal_id": "", "item_group_id" : "", "is_add_on_sub_item": '', "itemid": 1406607303, "modelid": 1958485669, "shopid":7333053, "index":0, "voucher":"C7PHKJ6W7"}
item2 = {"add_on_deal_id": "", "item_group_id" : "", "is_add_on_sub_item": '', "itemid": 784819375, "modelid": "", "shopid":1546550, "index":0, "voucher":""}
item3 = {"add_on_deal_id": "", "item_group_id" : "", "is_add_on_sub_item": '', "itemid": 1406607303, "modelid": 1958485669, "shopid":7333053, "index":0, "voucher":"C7PHKJ6W7"}
item4 = {"add_on_deal_id": "", "item_group_id" : "", "is_add_on_sub_item": '', "itemid": 1406607303, "modelid": 1958485669, "shopid":7333053, "index":0, "voucher":"C7PHKJ6W7"}

item_list = [
    item1,
#    item2,
#    item3,
#    item4,
]

url_list = []

if 'item2' in locals():
    url1 = 'https://shopee.tw/api/v2/item/get?' + 'itemid=' + str(item1["itemid"]) + '&shopid=' + str(item1["shopid"])
    url_list.append(url1)
if 'item2' in locals():
    url2 = 'https://shopee.tw/api/v2/item/get?' + 'itemid=' + str(item2["itemid"]) + '&shopid=' + str(item2["shopid"])
    url_list.append(url2)
if 'item4' in locals():
    url3 = 'https://shopee.tw/api/v2/item/get?' + 'itemid=' + str(item3["itemid"]) + '&shopid=' + str(item3["shopid"])
    url_list.append(url3)
if 'item4' in locals():
    url4 = 'https://shopee.tw/api/v2/item/get?' + 'itemid=' + str(item4["itemid"]) + '&shopid=' + str(item4["shopid"])
    url_list.append(url4)

# https://shopee.tw/api/v2/checkout/get
# https://shopee.tw/api/v2/cart/add_to_cart


def load_json_file():
    my_data = []
    input_file_add_cart = open(json_path + json_name_cart, "r", encoding="utf-8")
    input_file_checkout = open(json_path + json_name_checkout, "r", encoding="utf-8")
    my_data.append(json.load(input_file_add_cart))
    my_data.append(json.load(input_file_checkout))
    input_file_add_cart.close()
    input_file_checkout.close()
    return my_data


def load_item(my_data, index):
    print(my_data)
    my_data[0]["itemid"] = item_list[index]["itemid"]
    my_data[0]["shopid"] = item_list[index]["shopid"]
    my_data[1]["shoporders"][0]["shop"]["shopid"] = item_list[index]["shopid"]
    my_data[1]["shoporders"][0]["items"][0]["add_on_deal_id"] = item_list[index]["add_on_deal_id"]
    my_data[1]["shoporders"][0]["items"][0]["is_add_on_sub_item"] = item_list[index]["is_add_on_sub_item"]
    my_data[1]["shoporders"][0]["items"][0]["item_group_id"] = item_list[index]["item_group_id"]
    my_data[1]["shoporders"][0]["items"][0]["itemid"] = item_list[index]["itemid"]
    my_data[1]["promotion_data"]["voucher_code"] = item_list[index]["voucher"]
    return my_data


def job(x):
    pass


def single_preprocess(index):
    while True:
        r = requests.get(url_list[index], headers=headers)
        print(r.status_code)
        json_array = json.loads(r.text)
        if (item_list[index]["modelid"] == ''):
            print(json_array["item"]["stock"])
            if (json_array["item"]["stock"]):
                del my_data_list[index][0]['modelid']
                del my_data_list[index][1]["shoporders"][0]["items"][0]["modelid"]
                break
        else:
            print(json_array["item"]["models"][index]["stock"])
            if (json_array["item"]["stock"]):
                my_data_list[index][0]["modelid"] = item_list[index]["modelid"]
                my_data_list[index][1]["shoporders"][0]["items"][0]["modelid"] = item_list[index]["modelid"]
                break
    # print(my_data_list)
    # print(json.dumps(my_data_list[index][0]))
    r1 = requests.post('https://shopee.tw/api/v2/cart/add_to_cart', data=json.dumps(my_data_list[index][0]),
                       headers=headers)
    print("R1 status: ", r1.status_code)

    #print(my_data_list[index][1])
    return


def multi_process():
    pool = mp.Pool()
    pool.map(job, range(total_process))


def main():
    index = 0
    my_data_list = []
    for i in range(len(item_list)):
        my_data_list.append(load_json_file())
    for i in range(len(my_data_list)):
        my_data_list[i] = load_item(my_data_list[i], i)

    while True:
        r = requests.get(url_list[index], headers=headers)
        print(r.status_code)
        json_array = json.loads(r.text)
        if (item_list[index]["modelid"] == ''):
            print(json_array["item"]["stock"])
            if (json_array["item"]["stock"]):
                del my_data_list[index][0]['modelid']
                del my_data_list[index][1]["shoporders"][0]["items"][0]["modelid"]
                break
        else:
            print(json_array["item"]["models"][index]["stock"])
            if (json_array["item"]["stock"]):
                my_data_list[index][0]["modelid"] = item_list[index]["modelid"]
                my_data_list[index][1]["shoporders"][0]["items"][0]["modelid"] = item_list[index]["modelid"]
                break
    # print(my_data_list)
    #print(json.dumps(my_data_list[index][0]))
    r1 = requests.post('https://shopee.tw/api/v2/cart/add_to_cart', data=json.dumps(my_data_list[index][0]), headers=headers)
    print("R1 status: ", r1.status_code)

    print(my_data_list[index][1])
    while True:
        r2 = requests.post('https://shopee.tw/api/v2/checkout/get', data=json.dumps(my_data_list[index][1]), headers=headers)
        json_r2 = json.loads(r2.text)
        if bool(json_r2["buyer_txn_fee_info"]["error"] == 'invalid_rule_id'):
            break
    print("R2 status:", r2.status_code)
    #print(r2.text)

    r3 = requests.post('https://shopee.tw/api/v2/checkout/place_order', data=r2.text, headers=headers)
    print("R3 status:", r3.status_code)
    print(r3.text)


if __name__ == '__main__':
    main()
    # for i in range(len(item_list)):
    #     my_data_list.append(load_json_file())
    # for i in range(len(my_data_list)):
    #     my_data_list[i] = load_item(my_data_list[i], i)
    # for i in range(len(item_list)):
    #     single_preprocess(i)
    # multi_process()
