def pagination(array, page_number):
    n, reminder = page_number, len(array) % page_number
    curr, idx, old_idx = 1, 0, 0
    while n + reminder != 0:
        idx += len(array) // page_number + bool(reminder)
        print(f"this is page {curr} have object {array[old_idx:idx]}")
        n -= 1
        reminder = max(reminder - 1, 0)
        curr += 1
        old_idx = idx


lst = list(range(1, 20))
page_number = 4

pagination(lst, page_number)