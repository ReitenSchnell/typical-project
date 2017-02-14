import so_client


def calculate_statistics(tag):
    tags = so_client.get_questions_by_tag(tag)
    tags_dict = {}
    for tag_list in tags:
        for current_tag in tag_list:
            if current_tag in tags_dict:
                tags_dict[current_tag] += 1
            else:
                tags_dict[current_tag] = 1
    if tag in tags_dict:
        del tags_dict[tag]
    return tags_dict


def get_top_tags(tags_map, top_n):
    sorted_tags = sorted([(value,key) for (key,value) in tags_map.items()])
    top_tags = sorted_tags[-top_n:]
    return [tag for _, tag in top_tags]