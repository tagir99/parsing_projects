import requests
import json

# converter - curlconverter.com
# json.dump
# join

def get_data():
    cookies = {
        'COMPARISON_INDICATOR': 'false',
        'HINTS_FIO_COOKIE_NAME': '2',
        'MVID_AB_SERVICES_DESCRIPTION': 'var4',
        'MVID_ADDRESS_COMMENT_AB_TEST': '2',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'false',
        'MVID_CART_MULTI_DELETE': 'false',
        'MVID_CATALOG_STATE': '1',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'MVID_GIFT_KIT': 'true',
        'MVID_GTM_DELAY': 'true',
        'MVID_GUEST_ID': '21273701892',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_SOLD_VARIANTS': '3',
        'MVID_MCLICK': 'true',
        'MVID_MINDBOX_DYNAMICALLY': 'true',
        'MVID_MINI_PDP': 'true',
        'MVID_MOBILE_FILTERS': 'true',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_DESKTOP_FILTERS': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_SERVICES': '111',
        'MVID_SERVICES_MINI_BLOCK': 'var2',
        'MVID_TAXI_DELIVERY_INTERVALS_VIEW': 'new',
        'MVID_WEBP_ENABLED': 'true',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'PICKUP_SEAMLESS_AB_TEST': '2',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'true',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'searchType2': '2',
        '_ym_uid': '1660842825831885616',
        '_ym_d': '1660842825',
        '__ttl__widget__ui': '1660842826465-dc8b56f2e4c4',
        '__SourceTracker': 'google__organic',
        'admitad_deduplication_cookie': 'google__organic',
        'tmr_lvid': 'c9c97073611462c02a83867138d39c09',
        'tmr_lvidTS': '1660842828135',
        'gdeslon.ru.__arc_domain': 'gdeslon.ru',
        'gdeslon.ru.user_id': '69e91abf-afe4-47b2-90e5-4663641f63dc',
        'advcake_track_id': '7743ea6a-0229-dbf2-1890-bfd48e30caa4',
        'advcake_session_id': '5eda0110-4610-180b-6b63-ae0c72de402a',
        'uxs_uid': '1f967170-1f19-11ed-af99-99e2d0590a3a',
        'afUserId': '2663f99f-29b9-486c-b6c7-bc2a43f4bf35-p',
        'flocktory-uuid': 'cc510667-5387-46e0-bbb4-c3c1d9c11637-4',
        'wurfl_device_id': 'generic_web_browser',
        'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9',
        'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==',
        'deviceType': 'desktop',
        'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
        'mindboxDeviceUUID': '1e8b23e2-cb2b-4112-8651-fe83f5f41595',
        'directCrm-session': '%7B%22deviceGuid%22%3A%221e8b23e2-cb2b-4112-8651-fe83f5f41595%22%7D',
        'MVID_GEOLOCATION_NEEDED': 'false',
        'MVID_CHECKOUT_REGISTRATION_AB_TEST': '2',
        'MVID_CITY_ID': 'CityCZ_975',
        'MVID_REGION_ID': '1',
        'MVID_REGION_SHOP': 'S002',
        'MVID_TIMEZONE_OFFSET': '3',
        'MVID_CITY_CHANGED': 'false',
        'MVID_KLADR_ID': '7700000000000',
        '__lhash_': '27508805890134a96c9d968f28601ba6',
        'MVID_CART_AVAILABILITY': 'true',
        'MVID_CREDIT_AVAILABILITY': 'true',
        'MVID_HANDOVER_SUMMARY': 'true',
        'MVID_LP_HANDOVER': '1',
        'MVID_SMART_BANNER_BOTTOM': '1',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5',
        'flacktory': 'no',
        '_gid': 'GA1.2.251638812.1661519590',
        '_ym_isad': '2',
        'SMSError': '',
        'authError': '',
        'AF_SYNC': '1661519593786',
        'JSESSIONID': 'n2FnjLhpJtYX3lTVwdLG7r2NQpFTn1QdBrB2FTFGPvh51GJP15Ry!-1557130946',
        'bIPs': '434929338',
        '_sp_ses.d61c': '*',
        'BIGipServeratg-ps-prod_tcp80': '1812257802.20480.0000',
        'MVID_GTM_BROWSER_THEME': '1',
        '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VnPXtbIWMZX10hdikoVTUlOldrHhIlP18WOz9fKx4Ie2thVVdjJTswMUUrKFAeJXs+RhdEGjhmImROWiJDXlF/FhoXfWwoUQsRYj1DbnkbN1ddHBEkWA4hPwtpW1Y0ZxUbQEgYL0tueS88ah9jTWAmRF5TdRdgSkMrNhZGRhxyM3c/awgiGVETKl94R1drZVVCODFnDE9PTRIWIep6yQ==',
        '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VnPXtbIWMZX10hdikoVTUlOldrHhIlP18WOz9fKx4Ie2thVVdjJTswMUUrKFAeJXs+RhdEGjhmImROWiJDXlF/FhoXfWwoUQsRYj1DbnkbN1ddHBEkWA4hPwtpW1Y0ZxUbQEgYL0tueS88ah9jTWAmRF5TdRdgSkMrNhZGRhxyM3c/awgiGVETKl94R1drZVVCODFnDE9PTRIWIep6yQ==',
        'cfidsgib-w-mvideo': '7CI7HeJqaSGlPxNNbPOWP1NmqQmWavPzBx4xY66oUJSRrSZVOZPQ2z39mMERJXsExydY5wwvPxWLk49V+JmVMU7uWtpZkFFi75vV/t1Ak0XSd5r7MyJcEGY8tIs5mRWcCXTVkog0PEBP+aIIuJrLVH/ZkJGnoqh8Iq61',
        'cfidsgib-w-mvideo': '7CI7HeJqaSGlPxNNbPOWP1NmqQmWavPzBx4xY66oUJSRrSZVOZPQ2z39mMERJXsExydY5wwvPxWLk49V+JmVMU7uWtpZkFFi75vV/t1Ak0XSd5r7MyJcEGY8tIs5mRWcCXTVkog0PEBP+aIIuJrLVH/ZkJGnoqh8Iq61',
        'gsscgib-w-mvideo': 'HpYosUtUzCVax7AaClS15tNWqfsjmI31DSmEsU9ufBYgdBVoWzmtwxMX9xKakUMeelpqQqw1oFj/AtARcyaHfih87ZkMLiVqR0FNwiPGmvKyrECKzh6X1eUrpotiEHjhwe+bUF/bml567cWSS65x9ZU8JsA+pg+XoXeApdu9/NUInhEeRfg2ZKafg1CHylPpYGTl64C0t3v5LlVtWT+RfUPImurBY7n6D/ZfYkcPNQmio8C/3IyaKbWDoyS/uQ==',
        'gsscgib-w-mvideo': 'HpYosUtUzCVax7AaClS15tNWqfsjmI31DSmEsU9ufBYgdBVoWzmtwxMX9xKakUMeelpqQqw1oFj/AtARcyaHfih87ZkMLiVqR0FNwiPGmvKyrECKzh6X1eUrpotiEHjhwe+bUF/bml567cWSS65x9ZU8JsA+pg+XoXeApdu9/NUInhEeRfg2ZKafg1CHylPpYGTl64C0t3v5LlVtWT+RfUPImurBY7n6D/ZfYkcPNQmio8C/3IyaKbWDoyS/uQ==',
        'fgsscgib-w-mvideo': 'LIY99c62b97bcf24d15f26e3d0d9c204bec5415a',
        'fgsscgib-w-mvideo': 'LIY99c62b97bcf24d15f26e3d0d9c204bec5415a',
        'cfidsgib-w-mvideo': '7CMCrw0F+TlnF8Tn9hiZUhIofzQcDnws5Km84xA9JPUZNiiIJ9zdaQ9ooYJQH8keykZOw+nEB4sjv4CrX8br4LdY0l+RIU5LJsr0kRgNWA2MX9iAyR6jUKwIyh3VwCnTm5cE1BOJ9cvKrJMuBq5mySZTCXb/FR1D7bfN',
        'CACHE_INDICATOR': 'false',
        '_sp_id.d61c': 'a9de557f-a099-4eb0-a860-c12fc3d4631c.1661519590.2.1661524690.1661520175.a374e5ed-ea23-4b8e-83b3-e7f6bd864326.9ea6a6e4-3030-4ade-bcf9-c71937002c73.7a612f63-eb7e-4e56-b283-5ea04897e405.1661524674557.3',
        '_ga': 'GA1.2.170153320.1660842825',
        'tmr_detect': '0%7C1661524694996',
        'MVID_ENVCLOUD': 'prod1',
        'tmr_reqNum': '236',
        '_ga_CFMZTSS5FM': 'GS1.1.1661524674.5.1.1661524862.0.0.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1661524674.5.1.1661524862.60.0.0',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'baggage': 'sentry-transaction=%2F,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=c4dcba6ba1a349c9a2ab634da1494190,sentry-sample_rate=0%2C5',
        'cache-control': 'no-cache',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'COMPARISON_INDICATOR=false; HINTS_FIO_COOKIE_NAME=2; MVID_AB_SERVICES_DESCRIPTION=var4; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=false; MVID_CART_MULTI_DELETE=false; MVID_CATALOG_STATE=1; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_GTM_DELAY=true; MVID_GUEST_ID=21273701892; MVID_IS_NEW_BR_WIDGET=true; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_MOBILE_FILTERS=true; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_TAXI_DELIVERY_INTERVALS_VIEW=new; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PICKUP_SEAMLESS_AB_TEST=2; PRESELECT_COURIER_DELIVERY_FOR_KBT=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; searchType2=2; _ym_uid=1660842825831885616; _ym_d=1660842825; __ttl__widget__ui=1660842826465-dc8b56f2e4c4; __SourceTracker=google__organic; admitad_deduplication_cookie=google__organic; tmr_lvid=c9c97073611462c02a83867138d39c09; tmr_lvidTS=1660842828135; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=69e91abf-afe4-47b2-90e5-4663641f63dc; advcake_track_id=7743ea6a-0229-dbf2-1890-bfd48e30caa4; advcake_session_id=5eda0110-4610-180b-6b63-ae0c72de402a; uxs_uid=1f967170-1f19-11ed-af99-99e2d0590a3a; afUserId=2663f99f-29b9-486c-b6c7-bc2a43f4bf35-p; flocktory-uuid=cc510667-5387-46e0-bbb4-c3c1d9c11637-4; wurfl_device_id=generic_web_browser; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; deviceType=desktop; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; mindboxDeviceUUID=1e8b23e2-cb2b-4112-8651-fe83f5f41595; directCrm-session=%7B%22deviceGuid%22%3A%221e8b23e2-cb2b-4112-8651-fe83f5f41595%22%7D; MVID_GEOLOCATION_NEEDED=false; MVID_CHECKOUT_REGISTRATION_AB_TEST=2; MVID_CITY_ID=CityCZ_975; MVID_REGION_ID=1; MVID_REGION_SHOP=S002; MVID_TIMEZONE_OFFSET=3; MVID_CITY_CHANGED=false; MVID_KLADR_ID=7700000000000; __lhash_=27508805890134a96c9d968f28601ba6; MVID_CART_AVAILABILITY=true; MVID_CREDIT_AVAILABILITY=true; MVID_HANDOVER_SUMMARY=true; MVID_LP_HANDOVER=1; MVID_SMART_BANNER_BOTTOM=1; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; flacktory=no; _gid=GA1.2.251638812.1661519590; _ym_isad=2; SMSError=; authError=; AF_SYNC=1661519593786; JSESSIONID=n2FnjLhpJtYX3lTVwdLG7r2NQpFTn1QdBrB2FTFGPvh51GJP15Ry!-1557130946; bIPs=434929338; _sp_ses.d61c=*; BIGipServeratg-ps-prod_tcp80=1812257802.20480.0000; MVID_GTM_BROWSER_THEME=1; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VnPXtbIWMZX10hdikoVTUlOldrHhIlP18WOz9fKx4Ie2thVVdjJTswMUUrKFAeJXs+RhdEGjhmImROWiJDXlF/FhoXfWwoUQsRYj1DbnkbN1ddHBEkWA4hPwtpW1Y0ZxUbQEgYL0tueS88ah9jTWAmRF5TdRdgSkMrNhZGRhxyM3c/awgiGVETKl94R1drZVVCODFnDE9PTRIWIep6yQ==; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VnPXtbIWMZX10hdikoVTUlOldrHhIlP18WOz9fKx4Ie2thVVdjJTswMUUrKFAeJXs+RhdEGjhmImROWiJDXlF/FhoXfWwoUQsRYj1DbnkbN1ddHBEkWA4hPwtpW1Y0ZxUbQEgYL0tueS88ah9jTWAmRF5TdRdgSkMrNhZGRhxyM3c/awgiGVETKl94R1drZVVCODFnDE9PTRIWIep6yQ==; cfidsgib-w-mvideo=7CI7HeJqaSGlPxNNbPOWP1NmqQmWavPzBx4xY66oUJSRrSZVOZPQ2z39mMERJXsExydY5wwvPxWLk49V+JmVMU7uWtpZkFFi75vV/t1Ak0XSd5r7MyJcEGY8tIs5mRWcCXTVkog0PEBP+aIIuJrLVH/ZkJGnoqh8Iq61; cfidsgib-w-mvideo=7CI7HeJqaSGlPxNNbPOWP1NmqQmWavPzBx4xY66oUJSRrSZVOZPQ2z39mMERJXsExydY5wwvPxWLk49V+JmVMU7uWtpZkFFi75vV/t1Ak0XSd5r7MyJcEGY8tIs5mRWcCXTVkog0PEBP+aIIuJrLVH/ZkJGnoqh8Iq61; gsscgib-w-mvideo=HpYosUtUzCVax7AaClS15tNWqfsjmI31DSmEsU9ufBYgdBVoWzmtwxMX9xKakUMeelpqQqw1oFj/AtARcyaHfih87ZkMLiVqR0FNwiPGmvKyrECKzh6X1eUrpotiEHjhwe+bUF/bml567cWSS65x9ZU8JsA+pg+XoXeApdu9/NUInhEeRfg2ZKafg1CHylPpYGTl64C0t3v5LlVtWT+RfUPImurBY7n6D/ZfYkcPNQmio8C/3IyaKbWDoyS/uQ==; gsscgib-w-mvideo=HpYosUtUzCVax7AaClS15tNWqfsjmI31DSmEsU9ufBYgdBVoWzmtwxMX9xKakUMeelpqQqw1oFj/AtARcyaHfih87ZkMLiVqR0FNwiPGmvKyrECKzh6X1eUrpotiEHjhwe+bUF/bml567cWSS65x9ZU8JsA+pg+XoXeApdu9/NUInhEeRfg2ZKafg1CHylPpYGTl64C0t3v5LlVtWT+RfUPImurBY7n6D/ZfYkcPNQmio8C/3IyaKbWDoyS/uQ==; fgsscgib-w-mvideo=LIY99c62b97bcf24d15f26e3d0d9c204bec5415a; fgsscgib-w-mvideo=LIY99c62b97bcf24d15f26e3d0d9c204bec5415a; cfidsgib-w-mvideo=7CMCrw0F+TlnF8Tn9hiZUhIofzQcDnws5Km84xA9JPUZNiiIJ9zdaQ9ooYJQH8keykZOw+nEB4sjv4CrX8br4LdY0l+RIU5LJsr0kRgNWA2MX9iAyR6jUKwIyh3VwCnTm5cE1BOJ9cvKrJMuBq5mySZTCXb/FR1D7bfN; CACHE_INDICATOR=false; _sp_id.d61c=a9de557f-a099-4eb0-a860-c12fc3d4631c.1661519590.2.1661524690.1661520175.a374e5ed-ea23-4b8e-83b3-e7f6bd864326.9ea6a6e4-3030-4ade-bcf9-c71937002c73.7a612f63-eb7e-4e56-b283-5ea04897e405.1661524674557.3; _ga=GA1.2.170153320.1660842825; tmr_detect=0%7C1661524694996; MVID_ENVCLOUD=prod1; tmr_reqNum=236; _ga_CFMZTSS5FM=GS1.1.1661524674.5.1.1661524862.0.0.0; _ga_BNX5WPP3YK=GS1.1.1661524674.5.1.1661524862.60.0.0',
        'pragma': 'no-cache',
        'referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/noutbuki-118/f/brand=hp/skidka=da/tolko-v-nalichii=da',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': 'c4dcba6ba1a349c9a2ab634da1494190-9c3bfade79a880e0-1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'x-set-application-id': 'd4120dfb-5d78-4dd6-adfe-5602070d9322',
    }

    params = {
        'categoryId': '118',
        'offset': '0',
        'limit': '24',
        'filterParams': [
            'WyJicmFuZCIsIiIsImhwIl0=',
            'WyJza2lka2EiLCIiLCJkYSJd',
            'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
        ],
        'doTranslit': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies, headers=headers).json()
    #print(response)

    products_ids = response.get('body').get('products')

    with open ('1_products_ids.json', 'w') as file:
        json.dump(products_ids, file, indent=4, ensure_ascii=False)

    json_data = {
        'productIds': products_ids,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers,json=json_data).json()

    with open ('2_products_ids.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    #print(len(response.get('body').get('products')))

    products_ids_str = ','.join(products_ids)

    params = {
        'productIds': products_ids_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies,headers=headers).json()

    with open('3_prices.json', 'w') as file:
        json.dump(response, file ,indent=4 , ensure_ascii=False)

    items_prices = {}

    material_prices = response.get('body').get('materialPrices')

    #Объекты list записываются в словарь [items_prices] через цикл for
    for item in material_prices:
        item_id = item.get('price').get('productId')
        item_base_price = item.get('price').get('basePrice')
        item_sale_prise = item.get('price').get('salePrice')
        item_max_sale = item_base_price - item_sale_prise

        items_prices[item_id] = {
            'item_base_price' : item_base_price,
            'item_sale_prise' : item_sale_prise,
            'item_max_sale' : item_max_sale
        }

    # записать словарь items_prices в json
    with open('4_item_prices.json', 'w') as file:
        json.dump(items_prices, file, indent=4, ensure_ascii=False)

#обединить словарь с данными
def get_result():
    with open('2_products_ids.json') as file:
        products_data = json.load(file)

    with open('4_item_prices.json') as file:
        products_prices = json.load(file)

    products_data = products_data.get('body').get('products')

    for item in products_data:
        product_id = item.get('productId')

        if product_id in products_prices:
            prices = products_prices[product_id]

        item['item_base_price'] = prices.get('item_base_price')
        item['item_sale_prise'] = prices.get('item_sale_prise')
        item['item_max_sale'] = prices.get('item_max_sale')

    with open('5_resul.json', 'w') as file:
        json.dump(products_data, file, indent=4, ensure_ascii=False)

def main():
    get_data()
    get_result()

if __name__ == '__main__':
    main()
