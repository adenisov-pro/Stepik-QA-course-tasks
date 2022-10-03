# assert abs(-42) == -42, "Должно быть абсолютное значение числа"
# assert self.is_element_present('create_class_button', timeout=30), "No create class button"

# def test_input_text(expected_result, actual_result):
#     x = expected_result
#     y = actual_result
#
#     assert (x == y), f"expected {expected_result}, got {actual_result}"

# s = 'My Name is Julia'
# if 'Name' in s:
#     print('Substring found') # подстрока найдена
# index = s.find('Name')
# if index != -1:
#     print(f'Substring found at index {index}')
def test_substring(full_string, substring):
    assert (substring in full_string), f"expected '{substring}' to be substring of '{full_string}'"

