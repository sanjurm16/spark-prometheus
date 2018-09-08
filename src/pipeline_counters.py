from prometheus_client.core import Counter

from src.instrumentation import periodic_flush_metrics


class PipelineCounters:

    def __init__(self):
        self.records_counter = Counter('pipeline_records', 'Number of records processed in the pipeline', ['type'])

    def increment_pipeline_counter(self, type, value):
        self.records_counter.labels(type=type).inc(value)
        periodic_flush_metrics()
