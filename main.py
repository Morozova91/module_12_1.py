import unittest

from module_12_1 import Runner
from unittest import TestCase


# test_walk - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод walk у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 50.
# test_run - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод run у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 100.
# test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами. Далее 10 раз у объектов вызываются методы run и walk соответственно. Т.к. дистанции должны быть разными, используйте метод assertNotEqual, чтобы убедится в неравенстве результатов.
# Запустите кейс RunnerTest. В конечном итоге все 3 теста должны пройти проверку.


class RunnerTest(TestCase):
    def test_walk(self):
        runner = Runner("John")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)
        print('Test OK')

    def test_run(self):
        runner = Runner('Maria')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)
        print('Test OK')

    def test_challenge(self):
        runner_1 = Runner('Oleg')
        runner_2 = Runner('Roman')
        for i in range(10):
            if i % 2 == 0:
                runner_1.run()
            else:
                runner_2.walk()
            self.assertNotEqual(runner_1.distance, runner_2.distance)
            print('Test OK')


if __name__ == '__main__':
    unittest.main()
