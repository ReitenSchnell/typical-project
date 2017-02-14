import requests


def get_questions_by_tag(tag):
    url = 'https://api.stackexchange.com/2.2/questions?site=stackoverflow&tagged=%s' % tag
    response = requests.get(url)
    json = response.json()
    items = json['items']
    tags = [item['tags'] for item in items]
    return tags


