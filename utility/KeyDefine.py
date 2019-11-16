class KeyDefine:
    # For input user config key
    # For Yahoo config
    YAHOO_TOTAL_PROCESS = 10
    YAHOO_HEADER = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Cookie': '_ga=GA1.3.1611441426.1557213431; AO=u=1; ASPSESSIONIDSGDBRBBS=CLMLNAKDGIEGICAJBFMCNDED; ASPSESSIONIDSEBBBARA=LFLHKAKDPLHAAJGINCEOIOLO; ASPSESSIONIDSEBQASRQ=BCEHPNJANFJODJBEBOMNJBFL; ASPSESSIONIDSEBDAARA=CEJHFCPAJMBOBOBCMKACOHKE; ASPSESSIONIDQETRDQDD=BFJHFCPADLDBHHMIHOPEHGJG; ASPSESSIONIDQEBBSAAS=DDOPEPOBDDJNMEDAODHNDLJP; ASPSESSIONIDAEACDTSS=KBPJHPOBGHFIMNOIOCGBJJAF; APID=UP4eee2d8c-7099-11e9-b7fd-069dbc375c4a; ucs=fs=1; ASPSESSIONIDQECRARCB=DAMLLLFDJOGJDJCKIOFFEIOI; ASPSESSIONIDQWQTRTSC=IHLHLLFDAHFHLKDEJMIFJDDA; ASPSESSIONIDCGTCDQBA=JEBIJMFDKIEMLANDGHNNCIOI; ASPSESSIONIDSUDRCSBA=CAMLMLFDIOKCCDHMJOEAHHGI; ASPSESSIONIDQUTARART=CIMHLLFDDHPODPPJOJPNHNNJ; ASPSESSIONIDSWDQCSBA=BKPMPPKDGDPCKKBGKIEMPFEI; ASPSESSIONIDCWASTDDS=INPFEOEBCGFJOIJJIICDCMAL; ASPSESSIONIDAGTTBCBQ=KBAGEOEBGELMOLFKGKAAKNBD; ASPSESSIONIDSURBBQTR=KPAFGOEBAGJFEHNGHEMHFHAP; ASPSESSIONIDCWCSDQAD=CNHDEGGCBACHNHLEADLGLJBH; ASPSESSIONIDCWDACSCC=JJFBCGKCKAOEEKKEGGLOKLDD; ASPSESSIONIDQEQRRCDC=LBJFIDADPKAFPAAOGDEHOHFF; ASPSESSIONIDQWADTRTC=ONJLKDADMNFDKHELNCKLNANF; _gac_UA-71726228-1=1.1570990857.CjwKCAiAv9riBRANEiwA9Dqv1Umjp8tkJjQezWCjBsiOX8PManMsnztUZqO42LMaEDmUp0GTMxep0BoCnMUQAvD_BwE; coservername2=tw%2Ebuy%2Eyahoo%2Ecom; ASPSESSIONIDCWCRADQD=NNAKGHADMGMFHIFPOILMNIMD; ASPSESSIONIDAWQCTSSS=LDCNJHADFPBBMABKCDEDFECK; ASPSESSIONIDQUDBSRTR=HHNLFJADKMJECGACAJLEDMOK; _gid=GA1.3.759313711.1572792543; ms=act=ACT191021009&act_expire=1573005536797&c2=0&c2_expire=0&co_servername=oeya_iP1Q5yxrZX&co_servername_expire=1572790087000; APIDTS=1573142579; YSessionRegUser=d=V9Udpdhnoxi1LSnxRbCUC88okPtN_bNACzn5lJz6kcDH08x5NpAJbkYQ13fs0VWzvfqZ2T.AoJHi6eCEOV9FinZ_HAvdygVdviANI62Z5u8Ncm5AsReFB2yMMtN.fw_RPvcV1_2MieDnijX9242Tlw--&v=1; mdysd=1%255FleCr4KgHGXLXQjERCEhNavSSqr0a8orbVDhFU6%252Fshq2j9Xr27ozob2pFdX864aP%252FfYdmeB3LLGW4LiXxXTE3RoGdAZxx7nnLax3%252FPeGCTGkEWGfHvin3Qux%252F59QX4Yi96fFsGb6j8pAHPyAz7FfL1g%253D%253D; YAct=d=WOQR.N4Vt1lnHQRT_kZIk2pyH_Y8okub6zlmaSz5a_jXdPWcB3VvNccQeGnLurE617Su2NculMiaOZOZuDg0JLxvImokveu.kkcDgUgZPy0MBdRe8jO1QeCZ7VUm7nHY8Q--&v=1; B=291eq59ed2c7m&b=4&d=iRvbXBtpYEPAjF4uHj1UJpsqfTolqOMuTvc-&s=v9&i=_dHYlvHLKq29f.LZR8ou; T=z=8hMxdB81z1dBEll/Huqs.TLMjc2NQY0NjZPTzAxNzYw&a=QAE&sk=DAAhvf1F6quBew&ks=EAAIx4HCnhq5s1ILCh5MXGV.w--~G&kt=EAAjxHH5gHQJvSwgGHJT2Yc4g--~I&ku=FAAr19QC8Kwv5VWj0RsxJjxWTVyA6N2gL7yr8frS3oUK5pgu8OOmund8PwVie6FAzZmFhsGT3RsG71vJZIrsMOoyhX0e6GGLgTP9.yeluQ_M69bIG.jy8PMsBIdv4qrBp0unG33cwEXprD5ddR49HnlXSdt0HDvs0XSaTHLdTTTxlM-~A&d=bnMBeWFob28BZwFTVE1DV1RKSFhHUFpWRzY2TzdBNkJHNU41TQFzbAFOVEF4TWdFek1URTRPRGMyTURFMwFhAVFBRQFhYwFBRU1oaHNETQFsYXQBOGhNeGRCAWNzAQFzYwFkZXNrdG9wX3dlYgFmcwFZOHVWN3lCYzBUTHABenoBOGhNeGRCQTdF&af=QkNBQkJBQ3FBQjVoJnRzPTE1NzMxNzc0NjgmcHM9QW1MT1JhNHRFTC5jd1Jqd0xMOTNWQS0t; F=d=JUrut2s9v7EfmNQbgzJL7t7UcgXe1ial9SLdP50HZtx7yC_SKhmXvlNsCR9VHL3rgg--; PH=fn=I92SZbkLomPpoHiPRi_i&l=zh-Hant-TW&i=tw; Y=v=1&n=7dc5sevjl0bpo&l=75jyqrsv/o&p=m2rvvtw00000000&iz=408&r=dt&intl=tw; GUCS=AaNtYcrB; GUC=AQEAAQJdxhVemUIZngPj&s=AQAAAOHIIpy1&g=XcTIhg; _gat=1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
        'Origin': 'https://tw.buy.yahoo.com',
        'Referer': 'https://tw.buy.yahoo.com/coupons',
        'Host': 'tw.buy.yahoo.com',
    };

    # For Shopee config
    SHOPEE_TOTAL_PROCESS = 10
    SHOPEE_HEADER = {
        'Accept': 'application/json',
        'Cookie': '__BWfp=c1557236768161x607d029c5; SPC_F=w0FUlwK6CD8huOtjtpqCgNv9EVjebA0b; REC_T_ID=77daac7c-70ce-11e9-8fab-b4969130adac; _ga=GA1.2.729012483.1557236769; cto_lwid=d31e0f9c-f1b6-4271-a280-aea1c5e82517; csrftoken=ldDYrD0JsF5ibSShaKeQFB26UY8Vinb2; welcomePkgShown=true; bannerShown=true; UYOMAPJWEMDGJ=; SPC_SC_SA_TK=; SPC_SC_SA_UD=; _fbp=fb.1.1560818539651.1954273152; SPC_RW_HYBRID_ID=97; __LOCALE__=TW; __ENV__=live; _hjid=0ef52ffa-30fa-41af-969a-d88abfe1590c; _hjIncludedInSample=1; selected_checkout_payment_category=1; credit_card=3556308; SPC_SI=cpmjf26gwpodtuj4a5una75yob4427sx; _gid=GA1.2.228146082.1572111580; language=zhHant; cto_bundle=NtAA9180TlMyY1dGYkNMY3JIanhiOGxGWFVzNTd6QjR3ZGRJakUyRVNScFFoVCUyRnhaWnlEUnE2bDhZc2t2bjA3VzIwdFBydUNCN2J1UVRKcWJRb1BvYlVPeiUyRnMwZldtemZmZmVnWXNVaFpRVXVUdFFHdlYwNVBUdFpNM2p4cm5COHhFamVlamg4NlprU00yWlRJUyUyQndPazl1VFElM0QlM0Q; cardNumber=* 3109; card_bank_id=4203; _gcl_au=1.1.2021662752.1572803707; SPC_SC_TK=db1120f2330e5c507d27b09fcf75de24; SPC_SC_UD=25360609; SPC_EC="AaAmB9Bmls6h53QYeokhw8/gpigNB4d1dt1K1GqPVSddGmt0mfWfq/POhb4nT7WoA/CUzgO6LrKP8pYgEJMQaH3FtM48d+nGF1D9mhNNXWuog8SEXCI+0Ub2OfAqgbtL1XyQWzeSNLxBolhkV3tQV/KTpPdNCyGEZBTn3ujBTJI="; SPC_U=25360609; SPC_IA=1; _fbc=fb.1.1573401640872.IwAR1VtiqIZ06Ss94DPHWG0ogsYm4oM_ywiW8Y384xASAPaDfmEAF6-IfIHhY; PHPSESSID=63ca5328cc01c41844ff73f4b0fc937f; _med=refer; AMP_TOKEN=%24NOT_FOUND; _dc_gtm_UA-61915057-6=1; SPC_T_IV="VTAFvRPH+RE8ePWMVqI1EA=="; SPC_T_ID="aJRhhFwDNGyj+lQnT6NupccCwl8OsIDdyt8DqROcNkm2aDYug0PMc3/CAp5BEB5jW6JGW1Z6m962G99YT/SQ6ltDxEcK4X/cDgWIlEqm1qo="; _gali=main',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
        'Origin': 'https://shopee.tw',
        'Referer': 'https://shopee.tw/user/voucher-wallet/?type=0',
        'Host': 'shopee.tw',
        'X-API-SOURCE': 'pc',
        'X-CSRFToken': 'ldDYrD0JsF5ibSShaKeQFB26UY8Vinb2',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/json',
        'Connection': 'keep-alive',
    };
