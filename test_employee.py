import pytest
from employee import Employee

@pytest.fixture
def employee_instance():
    return Employee("John", "Doe", 60000)

def test_give_default_raise(employee_instance):
    # Initial salary is 60000, default raise amount is 5000
    employee_instance.give_raise()
    assert employee_instance.annual_salary == 65000

def test_give_custom_raise(employee_instance):
    # Initial salary is 60000, custom raise amount is 8000
    employee_instance.give_raise(8000)
    assert employee_instance.annual_salary == 68000
