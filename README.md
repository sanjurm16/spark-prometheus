# spark-prometheus

To run the spark etl using spark submit:
./spark-submit ~/devrats/spark-prometheus/src/main.py ~/devrats/input/ ~/devrats/output

Run prometheus server:
1. /spark-prometheus/docker/prometheus-server$ docker build . -t prometheus-server
2. /spark-prometheus/docker/prometheus-server$ docker run -p 9090:9090 prometheus-server

To view the prometheus metrics:
Navigate to localhost:9090

To view the installed node exporter metrics:
Navigate to localhost:9100
