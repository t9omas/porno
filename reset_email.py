import requests;cookies={'csrftoken':'X2my0jz_gM8Fx0AFuTnDUA','dpr':'2.75','datr':'izhAZ-wDTHDpFTMZgOD8qLjH','ig_did':'55A1ED1E-32F8-4AE3-9938-7C60526941D6','mid':'Z0A4iwABAAHexmqymQnKLZLEn6A7','wd':'393x767'};headers={'content-type':'application/x-www-form-urlencoded','origin':'https://www.instagram.com','referer':'https://www.instagram.com/accounts/password/reset/?source=fxcal','user-agent':'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36','x-csrftoken':'X2my0jz_gM8Fx0AFuTnDUA'}
while True:email=input("Email: ");data={'email_or_username':email,'flow':'fxcal'};print(requests.post('https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/',cookies=cookies,headers=headers,data=data).text)
# @t5omas