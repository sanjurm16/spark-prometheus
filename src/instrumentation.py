import os
import time

import atexit
from prometheus_client import multiprocess
from prometheus_client.core import CollectorRegistry
from prometheus_client.exposition import write_to_textfile

_LAST__FLUSHED_TIME = 0

registry = CollectorRegistry()
multiprocess.MultiProcessCollector(registry)


def get_last_flushed_time()->int:
    return _LAST__FLUSHED_TIME


def set_last_flushed_time(value: int):
    global _LAST__FLUSHED_TIME
    _LAST__FLUSHED_TIME = value


def flush_metrics():
    prom_dir = '/var/log/textcollector'
    if not os.path.exists(prom_dir):
        os.makedirs(prom_dir)
    write_to_textfile(prom_dir, registry=registry)


def periodic_flush_metrics():

    current_time = time.time()

    if get_last_flushed_time() + 10 < current_time:
        flush_metrics()
        set_last_flushed_time(current_time)


atexit.register(flush_metrics())

