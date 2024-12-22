data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(data_structure):
    if isinstance(data_structure, int):
        return data_structure
    elif isinstance(data_structure, str):
        return len(data_structure)
    elif isinstance(data_structure, (list, tuple, set)):
        count = 0
        for item in data_structure:
            count += calculate_structure_sum(item)
        return count
    elif isinstance(data_structure, dict):
        count = 0
        for j, value in data_structure.items():
            count += calculate_structure_sum(j) + calculate_structure_sum(value)
        return count
    return 0

result = calculate_structure_sum(data_structure)
print(result)