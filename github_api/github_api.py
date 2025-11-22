import requests

def get_user_events(username, limit=10):
    #definition of the url
    url = f'https://api.github.com/users/{username}/events/public'
    #try to get data through requests Get method
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f'Request failed to get datas {response.status_code}')

    events = response.json()
    return events[:limit]