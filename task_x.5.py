def check_values(a, b):

    if a is True and b is False:
        return True
    if a is None or b is None:
        return None
    if a > b:
        return 1
    if a < b:
        return -1
    if a == b:
        return 0


def process_flag():

    flag = True
    while flag:
        flag = False