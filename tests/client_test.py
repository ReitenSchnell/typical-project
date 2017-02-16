import so_client
import requests_mock

tag = 'python'


def test_returns_tags_inside_items_of_response():
    current_tags = ['python1', 'python2']
    with requests_mock.mock() as m:
        item11_tags = ['tag1', 'tag2']
        item12_tags = ['tag3', 'tag4']
        item21_tags = ['tag5', 'tag6']
        json_mock1 = {'items': [{'foo':'1', 'tags': item11_tags}, {'foo':'2', 'tags': item12_tags}]}
        json_mock2 = {'items': [{'moo':'1', 'tags': item21_tags}]}
        m.get('https://api.stackexchange.com/2.2/questions?site=stackoverflow&tagged=%s'%current_tags[0],
              json=json_mock1)
        m.get('https://api.stackexchange.com/2.2/questions?site=stackoverflow&tagged=%s'%current_tags[1],
              json=json_mock2)
        result = so_client.get_questions_by_tag(current_tags)
        assert result == [item11_tags, item12_tags, item21_tags]

