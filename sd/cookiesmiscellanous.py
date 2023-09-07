import requests


cookie = {'visit-month':'February'}
response = requests.get('http://rahulshettyacademy.com',allow_redirects=False,cookies=cookie,timeout=1)
print(response.history)
print(response.status_code)


se =requests.session()
se.cookies.update({'visit-month':'February'})

res = se.get('https://httpbin.org/cookies',cookies={'visit-year':'2022'})
print(res.text)
print(res.history)


