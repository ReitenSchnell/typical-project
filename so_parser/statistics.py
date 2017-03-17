import logging
import so_parser

logger = logging.getLogger('so_client')


def calculate_statistics(tags):
    so_tags = so_parser.get_questions_by_tag(tags)
    tags_dict = {}
    for tag_list in so_tags:
        for current_tag in tag_list:
            if current_tag in tags:
                continue
            if current_tag in tags_dict:
                tags_dict[current_tag] += 1
            else:
                tags_dict[current_tag] = 1
    logger.info('Got %i tags in statistics', len(tags_dict))
    return tags_dict


def get_top_tags(tags_map, top_n):
    sorted_tags = sorted([(value, key) for (key, value) in tags_map.items()], reverse=True)
    top_tags = sorted_tags[:top_n]
    return [tag for _, tag in top_tags]
