import requests as rq

demo = rq.get("https://www.netflix.com/in/")
print(demo.status_code)
print(demo.text)
