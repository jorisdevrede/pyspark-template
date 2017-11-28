import pytest


@pytest.fixture(scope='module')
def spark():
    """Fixture to create a single SparkSession for all tests"""
    from pyspark.sql import SparkSession

    session = SparkSession.builder.appName('pytest').getOrCreate()

    yield session

    session.stop()
