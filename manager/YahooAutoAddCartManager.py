import requests
import json
import multiprocessing as mp

total_process = 10

# Ref URL = https://tw.buy.yahoo.com/gdsale/HITACHI%E6%97%A5%E7%AB%8B16%E5%85%AC%E5%8D%87%E9%99%A4%E6%BF%95%E6%A9%9FRD-320HG-7582754.html

# my_data0 = {"type":"CALL_RESERVICE","payload":{"cartId":"kickstage2007","selectedShipType":".sh","prices":[{"type":"item","amount":520},{"type":"shipping","amount":100,"isCustomShippingFee":"false"},{"type":"order","amount":620}],"discounts":[],"items":[{"merchandiseId":"100306841725","productId":"184124846","modelId":"630048943","qty":1,"isCheckoutable":"true"}],"extra":"null"},"reservice":{"name":"FETCH_CREATE_DRAFT_ORDER","start":"FETCH_CREATE_DRAFT_ORDER_START","state":"CREATED"}}

# my_data1 = {"type":"CALL_RESERVICE","payload":{"updateData":{"draftOrderId":"Y29fNjEzNjEwMjc5NWRjMzBiMTY0YmFhMjYuMTQ0NjM1MDctMTU3MzA2MzQ0Ni0xMDQzMDgyNzI3","receiver":{"name":"徐宗煒","mobile":"0919269756","phone":"0425721281","ext":"00","address":"台元街18號8樓","city":"新竹縣","country":"tw","town":"竹北市","zipCode":"302","isForeign":"false"},"selectedAtmBankId":"822","selectedPayTypeId":"C2C_CTCB_WEB_ATM_PAY_TYPE"},"nextAction":"SUBMIT_ORDER"},"reservice":{"name":"FETCH_UPDATE_DRAFT_ORDER","start":"FETCH_UPDATE_DRAFT_ORDER_START","state":"CREATED"}}

# my_data2 = {"type":"CALL_RESERVICE","payload":{"cartId":"kickstage2007","draftOrderId":"Y29fNjEzNjEwMjc5NWRjMzBiMTY0YmFhMjYuMTQ0NjM1MDctMTU3MzA2MzQ0Ni0xMDQzMDgyNzI3","items":[{"merchandiseId":"100306841725","productId":"184124846","modelId":"630048943","qty":1}],"selectedShipType":".sh"},"reservice":{"name":"FETCH_CREATE_ORDER","start":"FETCH_CREATE_ORDER_START","state":"CREATED"}}


my_data1 = {"type": "CALL_RESERVICE",
            "payload": {"isStoreProduct": "false", "checkoutAction": "AddToCart", "cartType": "10",
                        "itemLines": [{"productBundleId": "8648586", "quantity": 1}], "isMobile": "false",
                        "authToken": "WXFvF5OInFD"},
            "reservice": {"name": "FETCH_CHECKOUT_ADD_TO_CART_RESULT", "start": "FETCH_CHECKOUT_ADD_TO_CART_START",
                          "state": "CREATED"}}

my_data2 = {"type": "CALL_RESERVICE", "reservice": {"name": "FETCH_DISTRICTS_DATA", "state": "CREATED"}}

data_convenience_store = {"type": "CALL_RESERVICE",
                          "payload": {"isStoreProduct": "false", "checkoutAction": "AddToCart", "cartType": "20",
                                      "itemLines": [{"productBundleId": "8660785", "quantity": 1}], "isMobile": "false",
                                      "authToken": "WXFvF5OInFD"},
                          "reservice": {"name": "FETCH_CHECKOUT_ADD_TO_CART_RESULT",
                                        "start": "FETCH_CHECKOUT_ADD_TO_CART_START", "state": "CREATED"}}

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Cookie': '_ga=GA1.3.1611441426.1557213431; AO=u=1; ASPSESSIONIDSGDBRBBS=CLMLNAKDGIEGICAJBFMCNDED; ASPSESSIONIDSEBBBARA=LFLHKAKDPLHAAJGINCEOIOLO; ASPSESSIONIDSEBQASRQ=BCEHPNJANFJODJBEBOMNJBFL; ASPSESSIONIDSEBDAARA=CEJHFCPAJMBOBOBCMKACOHKE; ASPSESSIONIDQETRDQDD=BFJHFCPADLDBHHMIHOPEHGJG; ASPSESSIONIDQEBBSAAS=DDOPEPOBDDJNMEDAODHNDLJP; ASPSESSIONIDAEACDTSS=KBPJHPOBGHFIMNOIOCGBJJAF; APID=UP4eee2d8c-7099-11e9-b7fd-069dbc375c4a; ucs=fs=1; ASPSESSIONIDQECRARCB=DAMLLLFDJOGJDJCKIOFFEIOI; ASPSESSIONIDQWQTRTSC=IHLHLLFDAHFHLKDEJMIFJDDA; ASPSESSIONIDCGTCDQBA=JEBIJMFDKIEMLANDGHNNCIOI; ASPSESSIONIDSUDRCSBA=CAMLMLFDIOKCCDHMJOEAHHGI; ASPSESSIONIDQUTARART=CIMHLLFDDHPODPPJOJPNHNNJ; ASPSESSIONIDSWDQCSBA=BKPMPPKDGDPCKKBGKIEMPFEI; ASPSESSIONIDCWASTDDS=INPFEOEBCGFJOIJJIICDCMAL; ASPSESSIONIDAGTTBCBQ=KBAGEOEBGELMOLFKGKAAKNBD; ASPSESSIONIDSURBBQTR=KPAFGOEBAGJFEHNGHEMHFHAP; ASPSESSIONIDCWCSDQAD=CNHDEGGCBACHNHLEADLGLJBH; ASPSESSIONIDCWDACSCC=JJFBCGKCKAOEEKKEGGLOKLDD; ASPSESSIONIDQEQRRCDC=LBJFIDADPKAFPAAOGDEHOHFF; ASPSESSIONIDQWADTRTC=ONJLKDADMNFDKHELNCKLNANF; _gac_UA-71726228-1=1.1570990857.CjwKCAiAv9riBRANEiwA9Dqv1Umjp8tkJjQezWCjBsiOX8PManMsnztUZqO42LMaEDmUp0GTMxep0BoCnMUQAvD_BwE; coservername2=tw%2Ebuy%2Eyahoo%2Ecom; ASPSESSIONIDCWCRADQD=NNAKGHADMGMFHIFPOILMNIMD; ASPSESSIONIDAWQCTSSS=LDCNJHADFPBBMABKCDEDFECK; ASPSESSIONIDQUDBSRTR=HHNLFJADKMJECGACAJLEDMOK; _gid=GA1.3.759313711.1572792543; ms=act=ACT191021009&act_expire=1573005536797&c2=0&c2_expire=0&co_servername=oeya_iP1Q5yxrZX&co_servername_expire=1572790087000; APIDTS=1573142579; YSessionRegUser=d=V9Udpdhnoxi1LSnxRbCUC88okPtN_bNACzn5lJz6kcDH08x5NpAJbkYQ13fs0VWzvfqZ2T.AoJHi6eCEOV9FinZ_HAvdygVdviANI62Z5u8Ncm5AsReFB2yMMtN.fw_RPvcV1_2MieDnijX9242Tlw--&v=1; mdysd=1%255FleCr4KgHGXLXQjERCEhNavSSqr0a8orbVDhFU6%252Fshq2j9Xr27ozob2pFdX864aP%252FfYdmeB3LLGW4LiXxXTE3RoGdAZxx7nnLax3%252FPeGCTGkEWGfHvin3Qux%252F59QX4Yi96fFsGb6j8pAHPyAz7FfL1g%253D%253D; YAct=d=WOQR.N4Vt1lnHQRT_kZIk2pyH_Y8okub6zlmaSz5a_jXdPWcB3VvNccQeGnLurE617Su2NculMiaOZOZuDg0JLxvImokveu.kkcDgUgZPy0MBdRe8jO1QeCZ7VUm7nHY8Q--&v=1; B=291eq59ed2c7m&b=4&d=iRvbXBtpYEPAjF4uHj1UJpsqfTolqOMuTvc-&s=v9&i=_dHYlvHLKq29f.LZR8ou; T=z=8hMxdB81z1dBEll/Huqs.TLMjc2NQY0NjZPTzAxNzYw&a=QAE&sk=DAAhvf1F6quBew&ks=EAAIx4HCnhq5s1ILCh5MXGV.w--~G&kt=EAAjxHH5gHQJvSwgGHJT2Yc4g--~I&ku=FAAr19QC8Kwv5VWj0RsxJjxWTVyA6N2gL7yr8frS3oUK5pgu8OOmund8PwVie6FAzZmFhsGT3RsG71vJZIrsMOoyhX0e6GGLgTP9.yeluQ_M69bIG.jy8PMsBIdv4qrBp0unG33cwEXprD5ddR49HnlXSdt0HDvs0XSaTHLdTTTxlM-~A&d=bnMBeWFob28BZwFTVE1DV1RKSFhHUFpWRzY2TzdBNkJHNU41TQFzbAFOVEF4TWdFek1URTRPRGMyTURFMwFhAVFBRQFhYwFBRU1oaHNETQFsYXQBOGhNeGRCAWNzAQFzYwFkZXNrdG9wX3dlYgFmcwFZOHVWN3lCYzBUTHABenoBOGhNeGRCQTdF&af=QkNBQkJBQ3FBQjVoJnRzPTE1NzMxNzc0NjgmcHM9QW1MT1JhNHRFTC5jd1Jqd0xMOTNWQS0t; F=d=JUrut2s9v7EfmNQbgzJL7t7UcgXe1ial9SLdP50HZtx7yC_SKhmXvlNsCR9VHL3rgg--; PH=fn=I92SZbkLomPpoHiPRi_i&l=zh-Hant-TW&i=tw; Y=v=1&n=7dc5sevjl0bpo&l=75jyqrsv/o&p=m2rvvtw00000000&iz=408&r=dt&intl=tw; GUCS=AaNtYcrB; GUC=AQEAAQJdxhVemUIZngPj&s=AQAAAOHIIpy1&g=XcTIhg; _gat=1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    'Origin': 'https://tw.buy.yahoo.com',
    'Referer': 'https://tw.buy.yahoo.com/coupons',
    'Host': 'tw.buy.yahoo.com',
};


def main():
    while True:
        r1 = requests.put('https://tw.buy.yahoo.com/ssfe/_service_/', data=json.dumps(data_convenience_store),
                          headers=headers)
        print(r1.status_code)
        # print(r1.text)


def job(x):
    while True:
        r1 = requests.put('https://tw.buy.yahoo.com/ssfe/_service_/', data=json.dumps(data_convenience_store),
                          headers=headers)
        print("Process:", x, "status:", r1.status_code)
        # print(r1.text)


def multi_process():
    pool = mp.Pool()
    pool.map(job, range(total_process))


# r2 = requests.post('https://twpay.buy.yahoo.com/checkout/_reservice_/', data=json.dumps(my_data2), headers=headers)
# print(r2.status_code)
# print(r2.text)


# r = requests.put('https://tw.bid.yahoo.com/fe/_reservice_/', data=json.dumps(my_data2), headers=headers)
# print(r.status_code)
# print(r.text)


if __name__ == '__main__':
    # main()
    multi_process()
