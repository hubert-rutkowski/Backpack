def brute_force(C, items):
    n = len(items)
    max_value = 0
    selected_items = []

    for i in range(2 ** n):
        current_value = 0
        current_weight = 0
        current_items = []

        for j in range(n):
            if (i >> j) & 1:
                current_value += items[j][0]
                current_weight += items[j][1]
                current_items.append(items[j])

        if current_weight <= C and current_value > max_value:
            max_value = current_value
            selected_items = current_items

    return max_value, selected_items