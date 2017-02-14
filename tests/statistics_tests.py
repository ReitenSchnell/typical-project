import pytest
import so_client


class TestStatisticsTopTags:
    tags = {'tag5': 5, 'tag1': 1, 'tag8': 8, 'tag3': 3, 'tag11': 1}

    def test_returns_exactly_specified_amount_of_tags(self):
        tags_count = 3
        result = so_client.get_top_tags(self.tags, tags_count)
        assert len(result) == tags_count

    def test_returns_tags_sorted_by_amount(self):
        result = so_client.get_top_tags(self.tags, 3)
        assert result == ['tag8', 'tag5', 'tag3']
