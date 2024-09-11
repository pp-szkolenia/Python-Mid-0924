def get_item_by_id(items: list, id_: int):
    for item in items:
        if item["id"] == id_:
            result = item
            break
    else:
        result = None

    return result


def get_item_index_by_id(items_list, id_):
    for i, item in enumerate(items_list):
        if item["id"] == id_:
            return i
