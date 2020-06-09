def checkio(array: list) -> int:
    result = 0
    for i in range(0, len(array), 2):
        result += array[i]
    result = result * array[len(array)-1]
    print(result)
    return result


checkio([0, 1, 2, 3, 4, 5])
