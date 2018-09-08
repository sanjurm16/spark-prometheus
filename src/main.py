import argparse

from pyspark import SparkContext
from pyspark.sql import SparkSession

from pipeline_counters import PipelineCounters


def main(spark: SparkSession, input_path: str, output_path: str):
    spark_df = spark.read.csv(path=input_path, inferSchema=True, header=True)
    # log4jLogger = spark._jvm.org.apache.log4j
    # logger = log4jLogger.LogManager.getLogger(__name__)
    # logger.info("=============pyspark script logger initialized")
    pc = PipelineCounters()
    pc.increment_pipeline_counter('total_rec_proc', spark_df.count())

    spark_df.write.parquet(path=output_path)


if __name__ == '__main__':
    spark_session = SparkSession(SparkContext.getOrCreate())
    #SparkContext.addPyFile(path='dependencies.zip')
    parser = argparse.ArgumentParser(description='spark some files')
    parser.add_argument("csv_file_ip_path", help="location of some csv files")
    parser.add_argument("parquet_file_op_path", help="location of output path")
    args = parser.parse_args()
    main(spark_session, args.csv_file_ip_path, args.parquet_file_op_path)
