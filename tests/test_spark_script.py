# import the function(s) to be tested
from spark_script import perform_function
from pyspark.sql import SparkSession

import unittest


class TestSparkScript(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # setup spark once for all tests
        cls._spark = SparkSession.builder.appName('unittest').getOrCreate()

    def test_perform_function(self):
        rdd = self._spark.sparkContext.parallelize([1, 2, 3])

        # testing the 'perform_function()' function from spark_script.py
        self.assertEqual(perform_function(rdd).collect(), rdd.collect())

    @classmethod
    def tearDownClass(cls):
        # stop spark after all tests
        cls._spark.stop()


if __name__ == '__main__':
    unittest.main()
