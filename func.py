def sides_coord(list_coord):
    max_y = [list_coord[0][1], 0]
    max_x = [list_coord[0][0], 0]
    min_y = [list_coord[0][1], 0]
    min_x = [list_coord[0][0], 0]
    for count, elem in enumerate(list_coord):
        if elem[0] > max_x[0]:
            max_x[0] = elem[0]
            max_x[1] = count
        if elem[0] < min_x[0]:
            min_x[0] = elem[0]
            min_x[1] = count
        if elem[1] < max_y[0]:
            max_y[0] = elem[1]
            max_y[1] = count
        if elem[1] > min_y[0]:
            min_y[0] = elem[1]
            min_y[1] = count

    return max_x[1], min_x[1], max_y[1], min_y[1]


def is_shooted(left, right, up, down, bull):
    index = []
    if len(bull) != 0:
        for count, elem in enumerate(bull):
            if elem[0] <= right and elem[0] >= left:
                if elem[1] >= up  and elem[1] <= down:
                    index.append(count)
                if elem not in index:
                    if elem[1]+15 >= up and elem[1]+15 <= down:
                        index.append(count)
    return index
# list_coord = [[160, 80], [148, 112], [132, 100], [128, 84],
#               [104, 116], [108, 132], [124, 148], [148, 148],
#               [160, 136], [172, 148], [196, 148], [212, 132],
#               [216, 116], [192, 84], [188, 100], [172, 112],
#               [160, 80]]
#
# max_x_index, min_x_index, max_y_index, min_y_index = sides_coord(list_coord)
# print(max_x_index, min_x_index, max_y_index, min_y_index)