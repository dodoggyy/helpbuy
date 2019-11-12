import requests
import json
import multiprocessing as mp

total_process = 10

# 宅配
data_home_deivery = {"type": "CALL_RESERVICE",
                     "payload": {"isStoreProduct": "false", "checkoutAction": "AddToCart", "cartType": "10",
                                 "itemLines": [{"productBundleId": "8641705", "quantity": 1}], "isMobile": "false",
                                 "authToken": "J4yUEbjxznX"},
                     "reservice": {"name": "FETCH_CHECKOUT_ADD_TO_CART_RESULT",
                                   "start": "FETCH_CHECKOUT_ADD_TO_CART_START",
                                   "state": "CREATED"}}

# 快速到貨
data_fast_arrival = {"type": "CALL_RESERVICE",
                     "payload": {"isStoreProduct": "false", "checkoutAction": "AddToCart", "cartType": "30",
                                 "itemLines": [{"productBundleId": "8194593", "quantity": 1}], "isMobile": "false",
                                 "authToken": "J4yUEbjxznX"},
                     "reservice": {"name": "FETCH_CHECKOUT_ADD_TO_CART_RESULT",
                                   "start": "FETCH_CHECKOUT_ADD_TO_CART_START",
                                   "state": "CREATED"}}

# 超商快取
data_convenience_store = {"type": "CALL_RESERVICE",
                          "payload": {"isStoreProduct": "false", "checkoutAction": "AddToCart", "cartType": "20",
                                      "itemLines": [{"productBundleId": "8660785", "quantity": 1}], "isMobile": "false",
                                      "authToken": "WXFvF5OInFD"},
                          "reservice": {"name": "FETCH_CHECKOUT_ADD_TO_CART_RESULT",
                                        "start": "FETCH_CHECKOUT_ADD_TO_CART_START", "state": "CREATED"}}

# 配送方式
data_deliver_type = data_fast_arrival

'''
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Cookie': '_ga=GA1.3.1611441426.1557213431; AO=u=1; ASPSESSIONIDSGDBRBBS=CLMLNAKDGIEGICAJBFMCNDED; ASPSESSIONIDSEBBBARA=LFLHKAKDPLHAAJGINCEOIOLO; ASPSESSIONIDSEBQASRQ=BCEHPNJANFJODJBEBOMNJBFL; ASPSESSIONIDSEBDAARA=CEJHFCPAJMBOBOBCMKACOHKE; ASPSESSIONIDQETRDQDD=BFJHFCPADLDBHHMIHOPEHGJG; ASPSESSIONIDQEBBSAAS=DDOPEPOBDDJNMEDAODHNDLJP; ASPSESSIONIDAEACDTSS=KBPJHPOBGHFIMNOIOCGBJJAF; APID=UP4eee2d8c-7099-11e9-b7fd-069dbc375c4a; ucs=fs=1; ASPSESSIONIDQECRARCB=DAMLLLFDJOGJDJCKIOFFEIOI; ASPSESSIONIDQWQTRTSC=IHLHLLFDAHFHLKDEJMIFJDDA; ASPSESSIONIDCGTCDQBA=JEBIJMFDKIEMLANDGHNNCIOI; ASPSESSIONIDSUDRCSBA=CAMLMLFDIOKCCDHMJOEAHHGI; ASPSESSIONIDQUTARART=CIMHLLFDDHPODPPJOJPNHNNJ; ASPSESSIONIDSWDQCSBA=BKPMPPKDGDPCKKBGKIEMPFEI; ASPSESSIONIDCWASTDDS=INPFEOEBCGFJOIJJIICDCMAL; ASPSESSIONIDAGTTBCBQ=KBAGEOEBGELMOLFKGKAAKNBD; ASPSESSIONIDSURBBQTR=KPAFGOEBAGJFEHNGHEMHFHAP; ASPSESSIONIDCWCSDQAD=CNHDEGGCBACHNHLEADLGLJBH; ASPSESSIONIDCWDACSCC=JJFBCGKCKAOEEKKEGGLOKLDD; ASPSESSIONIDQEQRRCDC=LBJFIDADPKAFPAAOGDEHOHFF; ASPSESSIONIDQWADTRTC=ONJLKDADMNFDKHELNCKLNANF; _gac_UA-71726228-1=1.1570990857.CjwKCAiAv9riBRANEiwA9Dqv1Umjp8tkJjQezWCjBsiOX8PManMsnztUZqO42LMaEDmUp0GTMxep0BoCnMUQAvD_BwE; coservername2=tw%2Ebuy%2Eyahoo%2Ecom; ASPSESSIONIDCWCRADQD=NNAKGHADMGMFHIFPOILMNIMD; ASPSESSIONIDAWQCTSSS=LDCNJHADFPBBMABKCDEDFECK; ASPSESSIONIDQUDBSRTR=HHNLFJADKMJECGACAJLEDMOK; _gid=GA1.3.759313711.1572792543; ms=act=ACT191021009&act_expire=1573005536797&c2=0&c2_expire=0&co_servername=oeya_iP1Q5yxrZX&co_servername_expire=1572790087000; APIDTS=1573142579; YSessionRegUser=d=V9Udpdhnoxi1LSnxRbCUC88okPtN_bNACzn5lJz6kcDH08x5NpAJbkYQ13fs0VWzvfqZ2T.AoJHi6eCEOV9FinZ_HAvdygVdviANI62Z5u8Ncm5AsReFB2yMMtN.fw_RPvcV1_2MieDnijX9242Tlw--&v=1; mdysd=1%255FleCr4KgHGXLXQjERCEhNavSSqr0a8orbVDhFU6%252Fshq2j9Xr27ozob2pFdX864aP%252FfYdmeB3LLGW4LiXxXTE3RoGdAZxx7nnLax3%252FPeGCTGkEWGfHvin3Qux%252F59QX4Yi96fFsGb6j8pAHPyAz7FfL1g%253D%253D; YAct=d=WOQR.N4Vt1lnHQRT_kZIk2pyH_Y8okub6zlmaSz5a_jXdPWcB3VvNccQeGnLurE617Su2NculMiaOZOZuDg0JLxvImokveu.kkcDgUgZPy0MBdRe8jO1QeCZ7VUm7nHY8Q--&v=1; B=291eq59ed2c7m&b=4&d=iRvbXBtpYEPAjF4uHj1UJpsqfTolqOMuTvc-&s=v9&i=_dHYlvHLKq29f.LZR8ou; T=z=8hMxdB81z1dBEll/Huqs.TLMjc2NQY0NjZPTzAxNzYw&a=QAE&sk=DAAhvf1F6quBew&ks=EAAIx4HCnhq5s1ILCh5MXGV.w--~G&kt=EAAjxHH5gHQJvSwgGHJT2Yc4g--~I&ku=FAAr19QC8Kwv5VWj0RsxJjxWTVyA6N2gL7yr8frS3oUK5pgu8OOmund8PwVie6FAzZmFhsGT3RsG71vJZIrsMOoyhX0e6GGLgTP9.yeluQ_M69bIG.jy8PMsBIdv4qrBp0unG33cwEXprD5ddR49HnlXSdt0HDvs0XSaTHLdTTTxlM-~A&d=bnMBeWFob28BZwFTVE1DV1RKSFhHUFpWRzY2TzdBNkJHNU41TQFzbAFOVEF4TWdFek1URTRPRGMyTURFMwFhAVFBRQFhYwFBRU1oaHNETQFsYXQBOGhNeGRCAWNzAQFzYwFkZXNrdG9wX3dlYgFmcwFZOHVWN3lCYzBUTHABenoBOGhNeGRCQTdF&af=QkNBQkJBQ3FBQjVoJnRzPTE1NzMxNzc0NjgmcHM9QW1MT1JhNHRFTC5jd1Jqd0xMOTNWQS0t; F=d=JUrut2s9v7EfmNQbgzJL7t7UcgXe1ial9SLdP50HZtx7yC_SKhmXvlNsCR9VHL3rgg--; PH=fn=I92SZbkLomPpoHiPRi_i&l=zh-Hant-TW&i=tw; Y=v=1&n=7dc5sevjl0bpo&l=75jyqrsv/o&p=m2rvvtw00000000&iz=408&r=dt&intl=tw; GUCS=AaNtYcrB; GUC=AQEAAQJdxhVemUIZngPj&s=AQAAAOHIIpy1&g=XcTIhg; _gat=1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    'Origin': 'https://tw.buy.yahoo.com',
    'Referer': 'https://tw.buy.yahoo.com/coupons',
    'Host': 'tw.buy.yahoo.com',
};
# "authToken": "WXFvF5OInFD"
'''
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Cookie': '_ga=GA1.3.1611441426.1557213431; AO=u=1; ASPSESSIONIDSGDBRBBS=CLMLNAKDGIEGICAJBFMCNDED; ASPSESSIONIDSEBBBARA=LFLHKAKDPLHAAJGINCEOIOLO; ASPSESSIONIDSEBQASRQ=BCEHPNJANFJODJBEBOMNJBFL; ASPSESSIONIDSEBDAARA=CEJHFCPAJMBOBOBCMKACOHKE; ASPSESSIONIDQETRDQDD=BFJHFCPADLDBHHMIHOPEHGJG; ASPSESSIONIDQEBBSAAS=DDOPEPOBDDJNMEDAODHNDLJP; ASPSESSIONIDAEACDTSS=KBPJHPOBGHFIMNOIOCGBJJAF; APID=UP4eee2d8c-7099-11e9-b7fd-069dbc375c4a; ucs=fs=1; ASPSESSIONIDQECRARCB=DAMLLLFDJOGJDJCKIOFFEIOI; ASPSESSIONIDQWQTRTSC=IHLHLLFDAHFHLKDEJMIFJDDA; ASPSESSIONIDCGTCDQBA=JEBIJMFDKIEMLANDGHNNCIOI; ASPSESSIONIDSUDRCSBA=CAMLMLFDIOKCCDHMJOEAHHGI; ASPSESSIONIDQUTARART=CIMHLLFDDHPODPPJOJPNHNNJ; ASPSESSIONIDSWDQCSBA=BKPMPPKDGDPCKKBGKIEMPFEI; ASPSESSIONIDCWASTDDS=INPFEOEBCGFJOIJJIICDCMAL; ASPSESSIONIDAGTTBCBQ=KBAGEOEBGELMOLFKGKAAKNBD; ASPSESSIONIDSURBBQTR=KPAFGOEBAGJFEHNGHEMHFHAP; ASPSESSIONIDCWCSDQAD=CNHDEGGCBACHNHLEADLGLJBH; ASPSESSIONIDCWDACSCC=JJFBCGKCKAOEEKKEGGLOKLDD; ASPSESSIONIDQEQRRCDC=LBJFIDADPKAFPAAOGDEHOHFF; ASPSESSIONIDQWADTRTC=ONJLKDADMNFDKHELNCKLNANF; _gac_UA-71726228-1=1.1570990857.CjwKCAiAv9riBRANEiwA9Dqv1Umjp8tkJjQezWCjBsiOX8PManMsnztUZqO42LMaEDmUp0GTMxep0BoCnMUQAvD_BwE; coservername2=tw%2Ebuy%2Eyahoo%2Ecom; ASPSESSIONIDCWCRADQD=NNAKGHADMGMFHIFPOILMNIMD; ASPSESSIONIDAWQCTSSS=LDCNJHADFPBBMABKCDEDFECK; ASPSESSIONIDQUDBSRTR=HHNLFJADKMJECGACAJLEDMOK; _gid=GA1.3.759313711.1572792543; APIDTS=1573558997; ms=act=ACT191108015&act_expire=1573594952516&c2=0&c2_expire=0&co_servername=LN_3e51e5d2916610b652b24b6c8eea342a&co_servername_expire=1573656770711; YMy=d=eNkZ9Krxg13Wlivfopc3P0OkKnBUDxKp5dy0Quc.ypo3fva7yq4eFcqkOOTcJI9uKlz6vXJAtw6o81r1faoK_qw5ETdxQ5wGkeabFzgCCB_eSIlFhel6AA--&v=1; B=291eq59ed2c7m&b=4&d=iRvbXBtpYEPAjF4uHj1UJpsqfTolqOMuTvc-&s=v9&i=Rt38EQO0OM1Yr7JSQqWc; T=z=0luydB05V3dB5NooAdn.EOcMjc2NwY2NDYwNDc1Tjc3MDExMz&a=QAE&sk=DAArlXtW3kMGlv&ks=EAAdzGkRYTe.ShJ51M8juWqRA--~G&kt=EAA.91.v20b3GkFgkwc3PVnDA--~I&ku=FAAYYbA3oeilu8by3BLik7kWUoZx6X2SHDZcF6ehHNB7zEAm9x.bFDvHcO.MS4IK_VQzNRrXR7RSg90APXrFnDFkohTk5rg2AEpUDFc9.65SQBiyy3Sqj3pO3v2wVb.3p1RGnJA8CpCmhkXyqtjssoPBctem2VVqKzlWZ3XpEebwyE-~A&d=bnMBeWFob28BZwE3UlRWQkVVWFJWNTZYT0laWERIM0VENUVYTQFzbAFOVEF4TUFFeE16RTNNekF5T1RBd056WTJORE14T0RVLQFhAVFBRQFhYwFBS296Ul9TegFsYXQBMGx1eWRCAWNzAQFzYwFkZXNrdG9wX3dlYgFmcwFZOHVWN3lCYzBUTHABenoBMGx1eWRCQTdF&af=QkNBQkJBJnRzPTE1NzM1NzkxMjQmcHM9OFFPdkhkSkZqRVBtbFZFRUZ2R3lody0t; F=d=Tq_iiAI9vyEKUr7y0p4M6KWkwa5CWHT9TCcFqZiKUAdVl_qTWKgiW1sjUlb7VhQD5w--; PH=fn=mjlp4c4Dg22Xz1dxH23w&l=zh-Hant-TW&i=tw; Y=v=1&n=4qrlgorept1um&l=75jyqrsw/o&p=m2rvvtw00000000&iz=408&r=rq&intl=tw; GUCS=AbFeI0DP; GUC=AQEAAQJdzDNerUIZngPj&s=AQAAACXyuTWe&g=XcrpgA; YAct=d=TtrZMn3zllfqSsjJN.94NU7ztCI7rw2c73f9uctxoP0LzcyYSmM2BYnIBqJ4mO.sdmGrf0r5gpIGQ4GdwZy.yGSF8NCfSwzmyWVcwFwWKBTUAPw.KIT.fNSaIpElKBvCfete31VqqkatNs7.NxWrhBsc3EmOvTPaopp83jybqeuRtjysdgbsbKYGogU.Nfv9aKIDEcSpzTVEhtuHWYWbYqvzftEKciBpjQ.c5uBfnFo86.iYzTRGgfeQAcOwuVJIKL6QXiyDwDkyr.Zr5sImawH6EGKsUX_pQGjVGG0o1obKTC4YYP1AIoRDtwir1UTVbt2y.cPXNFoOfilvBiVCQ5SbdeMEcd0-&v=1; mdysd=1%255FleCr4KgHGXLXQjERCEhNavSSqr0a8orbVDhFU6%252Fshq2j9Xr27ozob2pFdX864aP%252FfYdmeB3LLGW4LiXxXTE3RoGdAZxx7nnLax3%252FPeGCTGkEWGfHvin3Qux%252F59QX4Yi96fFsGb6j8pAHPyAz7FfL1g%253D%253D; YSessionRegUser=d=n9wjXjjkNBbfUWIfOWqOLnibqQ9I_WOIm7GB8yCWcZxFPW7PFvd5RVbUVERu0GfAXwzMmDjCClUKvGYldPvOG8GKcqinCdM9PAani05cLeS_XrVxoFTLLBxrgTMIBktg3Ebs_GeyRJjNqrIsglugAw--&v=1; _gat=1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
    'Origin': 'https://tw.buy.yahoo.com',
    'Referer': 'https://tw.buy.yahoo.com/coupons',
    'Host': 'tw.buy.yahoo.com',
};


# "authToken": "J4yUEbjxznX"


def main():
    while True:
        r1 = requests.put('https://tw.buy.yahoo.com/ssfe/_service_/', data=json.dumps(data_deliver_type),
                          headers=headers)
        print(r1.status_code)
        # print(r1.text)


def job(x):
    while True:
        r1 = requests.put('https://tw.buy.yahoo.com/ssfe/_service_/', data=json.dumps(data_deliver_type),
                          headers=headers)
        print("Process:", x, "status:", r1.status_code)
        # print(r1.text)


def multi_process():
    pool = mp.Pool()
    pool.map(job, range(total_process))


if __name__ == '__main__':
    # main()
    multi_process()
