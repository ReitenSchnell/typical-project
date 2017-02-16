import so_client

tags_map = {'tag5': 5, 'tag1': 1, 'tag8': 8, 'tag3': 3, 'tag11': 1}


def test_top_tags_returns_exactly_specified_amount_of_tags():
    tags_count = 3
    result = so_client.get_top_tags(tags_map, tags_count)
    assert len(result) == tags_count


def test_top_tags_returns_tags_sorted_by_amount():
    result = so_client.get_top_tags(tags_map, 3)
    assert result == ['tag8', 'tag5', 'tag3']


def test_calculate_statistics_returns_tags_mapped_to_dict_with_counts(mocker):
    returned_tags = [['tag1', 'tag2'], ['tag1', 'tag4'], ['tag3', 'tag4', 'tag5', 'tag1']]
    mocker.patch('so_client.get_questions_by_tag', return_value=returned_tags)
    tags = ['python1', 'python2']
    result = so_client.calculate_statistics(tags)
    assert result == {'tag1': 3, 'tag2': 1, 'tag3': 1, 'tag4': 2, 'tag5': 1}


def test_calculate_statistics_does_not_include_original_tag(mocker):
    tags = ['python1', 'python2']
    returned_tags = [['tag1', tags[0], tags[1]]]
    mocker.patch('so_client.get_questions_by_tag', return_value=returned_tags)
    result = so_client.calculate_statistics(tags)
    assert result == {'tag1': 1}
