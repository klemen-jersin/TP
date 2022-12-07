import requests

def get_html(url):
    x=requests.get(url)
    if x.status_code == 200:
        page=x.text
    else:
        page='False'
    return page
page = get_html("http://example.com/neobstaja")
print(page)