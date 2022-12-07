import requests

def get_api_data(url):
    x=requests.get(url)
    if x.status_code == 200:
        page=x.json()
    else:
        page='False'
    return page
data = get_api_data("https://jsonplaceholder.typicode.com/todos/1")
print(data)