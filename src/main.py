import argparse

from pyspark.sql import SparkSession


def main(spark:SparkSession, args):
    spark_df = spark.read.csv(path=args.csv_file_location, inferSchema=True, header=True)
    spark_df.write.parquet(path=args.parquet_file_op_path)


if __name__ == '__main__':
    spark_session = SparkSession(SparkContext.getOrCreate())
    parser = argparse.ArgumentParser(description='spark some files')
    parser.add_argument("csv_file_ip_path", help="location of some csv files")
    parser.add_argument("parquet_file_op_path", help="location of output path")
    args = parser.parse_args()
    main(spark_session, args)
