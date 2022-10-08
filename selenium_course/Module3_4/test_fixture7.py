import pytest

# Путь для запуска из директории stepic_auto_tests_course:
# pytest -s selenium_course/Module3_4/test_fixture7.py
# pytest -s --tb=line selenium_course/Module3_4/test_fixture7.py

@pytest.fixture(scope="class")
def prepare_faces(): # подготовить_лица
    print("^_^", "\n")
    yield
    print(":3", "\n")


@pytest.fixture()
def very_important_fixture(): # очень_важная_фикстура
    print(":)", "\n")


@pytest.fixture(autouse=True)
def print_smiling_faces(): # напечатать_улыбающиеся_лица
    print(":-Р", "\n")


class TestPrintSmilingFaces():
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture): # проверьте_первые_улыбающиеся_лица
        print()


    def test_second_smiling_faces(self, prepare_faces):
        print()

# Вставьте код в файл и запустите с такими параметрами
# pytest -s --setup-show <file-name>.py
# так  будет сразу понятно, где фикстуры начинают, а где заканчивают работу