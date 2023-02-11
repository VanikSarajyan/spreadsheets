class TestBase:

    @classmethod
    def run_all(cls):
        for attr in cls.__dict__:
            ob = getattr(cls, attr)
            if callable(ob) and attr != "run_all" and not attr.startswith("__"):
                ob()

    @staticmethod
    def check(test_name, condition):
        passed = "passed V" if condition else "failed X"
        print(f"\tTest {test_name:<15} {passed}")
