import pytest

# Путь для запуска из директории stepic_auto_tests_course:
# pytest -rx -v selenium_course/Module3_5/test_xfail.py

@pytest.mark.xfail(reason="This test is dropped", strict = True) # Этот тест упавший
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False

