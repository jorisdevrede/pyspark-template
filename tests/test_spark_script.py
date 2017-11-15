# import required 3rd party packages to perform the tests
from pyspark import SparkConf, SparkContext

# import the function(s) to be tested
from spark_script import perform_function


def test_perform_function():
    """Tests output of the core function"""
    conf = SparkConf()
    sc = SparkContext(conf=conf)

    rdd = sc.parallelize([1, 2, 3])

    assert perform_function(rdd) == rdd
