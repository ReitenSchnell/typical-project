import concurrent.futures as cf
import requests_futures.sessions as rf


def get_questions_by_tag(tags):
    url = 'https://api.stackexchange.com/2.2/questions?site=stackoverflow&tagged={}'
    session = rf.FuturesSession()
    futures = [session.get(url.format(tag)) for tag in tags]
    tags = []
    for future in cf.as_completed(futures):
        response = future.result()
        json = response.json()
        items = json['items']
        for item in items:
            tags.append(item['tags'])
    return tags


