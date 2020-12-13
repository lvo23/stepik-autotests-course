import unittest  # встроенный в питоне тест-раннер


# Тесты обязательно должны находиться в специальном тестовом классе.
class TestAbs(unittest.TestCase):
    def test_abs1(self):
        # Вместо assert должны использоваться специальные assertion методы.
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")

    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")


if __name__ == "__main__":
    unittest.main()
