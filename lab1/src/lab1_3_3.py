def find_longest_peak(arr: list) -> int:
    length = len(arr)
    if length < 3:
        return -1
    max_length = -1
    current_length = -1
    is_active_peak = False
    is_decreased = False

    for i in range(length - 1):
        if arr[i] == arr[i + 1]:
            is_decreased = False
            is_active_peak = False
            current_length = -1
            continue

        if arr[i] > arr[i + 1] and not is_decreased and not is_active_peak:
            continue
        if arr[i] > arr[i + 1] and is_active_peak:
            is_decreased = True
            current_length += 1

        if arr[i] < arr[i + 1]:
            if is_decreased:
                max_length = max(max_length, current_length)
                is_decreased = False
                current_length = -1
                is_active_peak = False
            if not is_active_peak:
                is_active_peak = True
                current_length = 1
            if is_active_peak:
                current_length += 1

    if is_decreased and is_active_peak:
        max_length = max(max_length, current_length)
    return max_length


print(find_longest_peak([1, 2, 6, 6, 3]))
