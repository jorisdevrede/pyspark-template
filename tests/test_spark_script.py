# import the function(s) to be tested
from spark_script import perform_function

# this test uses the pytest fixture 'spark' from conftest.py
def test_perform_function(spark):
    """Tests output of the core function"""

    rdd = spark.sparkContext.parallelize([1, 2, 3])

    # testing the 'perform_function()' function from spark_script.py
    assert perform_function(rdd).collect() == rdd.collect()
