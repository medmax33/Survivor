def BiggerGreater(input_str: str) -> str:
    input_list = list(input_str)
    for i in range(len(input_list) - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            if input_list[i] > input_list[j]:
                input_list[i], input_list[j] = input_list[j], input_list[i]
                return ''.join(rotate(j + 1, input_list))
    return ""

def rotate(i: int, input_list: list) -> list:
    for j in range(i, len(input_list)):
        for k in range(j + 1, len(input_list)):
            if input_list[k] < input_list[j]:
                input_list[k], input_list[j] = input_list[j], input_list[k]
    return input_list

