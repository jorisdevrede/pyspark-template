from pyspark import SparkConf, SparkContext


def perform_function(rdd):
    """Performs the core function of this script

    This is de dummy core function of the pyspark script that we want to maintain.
    :param rdd: the rdd to transform
    :return: rdd
    """
    transformed_rdd = rdd.map(lambda x: x)

    return transformed_rdd


if __name__ == '__main__':
    """Main Spark script
    
    This is the actual code of the pyspark-template project."""
    conf = SparkConf().setAppName('spark_script')
    sc = SparkContext(conf=conf)

    rdd = sc.parallelize([1, 2, 3, 4, 5])

    rdd2 = perform_function(rdd)
