def edit_distance(str1, str2):
    if len(str1) == 0 and len(str2) == 0:
        return 0
    if len(str1) == 0 and len(str2) > 0:
        return len(str2)
    if len(str2) == 0 and len(str1) > 0:
        return len(str1)
    if str1[-1] == str2[-1]:
        return edit_distance(str1[:-1], str2[:-1])
    else:
        insert = edit_distance(str1, str2[:-1])
        delete = edit_distance(str1[:-1], str2)
        substitute = edit_distance(str1[:-1], str2[:-1])
        distances = [insert, delete, substitute]
        return min(distances) + 1


def main():
    # ("docter office", "doctors office", 2),
    dist = edit_distance("docter office", "doctors office")
    print(dist)


main()
