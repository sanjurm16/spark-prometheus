import os
import time

import atexit
from prometheus_client import multiprocess
from prometheus_client.core import REGISTRY
from prometheus_client.exposition import write_to_textfile

_LAST__FLUSHED_TIME = 0
prom_dir = '/tmp/prom/'
if not os.path.exists(prom_dir):
    os.makedirs(prom_dir)
os.environ['prometheus_multiproc_dir'] = prom_dir

registry = REGISTRY
multiprocess.MultiProcessCollector(registry)


def get_last_flushed_time()->int:
    return _LAST__FLUSHED_TIME


def set_last_flushed_time(value: int):
    global _LAST__FLUSHED_TIME
    _LAST__FLUSHED_TIME = value


def flush_metrics():
    write_to_textfile(prom_dir+'pipeline.prom', registry=registry)


def periodic_flush_metrics():

    current_time = time.time()

    if get_last_flushed_time() + 10 < current_time:
        flush_metrics()
        set_last_flushed_time(current_time)


atexit.register(flush_metrics)

