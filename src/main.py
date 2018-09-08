import argparse

from pyspark import SparkContext
from pyspark.sql import SparkSession

from src.pipeline_counters import PipelineCounters


def main(spark: SparkSession, input_path: str, output_path: str):
    spark_df = spark.read.csv(path=input_path, inferSchema=True, header=True)
    pc = PipelineCounters()
    pc.records_counter(spark_df.count())
    spark_df.write.parquet(path=output_path)


if __name__ == '__main__':
    spark_session = SparkSession(SparkContext.getOrCreate())
    parser = argparse.ArgumentParser(description='spark some files')
    parser.add_argument("csv_file_ip_path", help="location of some csv files")
    parser.add_argument("parquet_file_op_path", help="location of output path")
    args = parser.parse_args()
    main(spark_session, args.csv_file_ip_path, args.parquet_file_op_path)
