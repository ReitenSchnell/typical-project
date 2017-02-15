import so_client
import requests_mock

tag = 'python'


def test_returns_tags_inside_items_of_response():
    current_tag = 'python'
    with requests_mock.mock() as m:
        item1_tags = ['tag1', 'tag2']
        item2_tags = ['tag3', 'tag4']
        json_mock = {'items': [{'foo':'1', 'tags': item1_tags}, {'foo':'2', 'tags': item2_tags}]}
        m.get('https://api.stackexchange.com/2.2/questions?site=stackoverflow&tagged=%s'%current_tag, json=json_mock)
        result = so_client.get_questions_by_tag(current_tag)
        assert result == [item1_tags, item2_tags]

