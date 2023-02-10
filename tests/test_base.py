from abc import ABC, abstractmethod


class TestBase(ABC):

    @staticmethod
    @abstractmethod
    def run_all():
        pass

    @staticmethod
    def check(test_name, condition):
        passed = "passed V" if condition else "failed X"
        print(f"Test {test_name} {passed}")
