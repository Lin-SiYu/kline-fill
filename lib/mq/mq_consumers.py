from kline_filler.logs.logger import log


class MQConsumer:
    def __init__(self, ):
        self._subscribers = []  # e.g. [{data_dict}, ...]

    def register(self, consumer_callback, queue_name, exchange_name, routing_key='', prefetch_count=1, no_ack=True):
        data_dict = dict(
            consumer_callback=consumer_callback,
            queue_name=queue_name,
            exchange_name=exchange_name,
            routing_key=routing_key,
            prefetch_count=prefetch_count,
            no_ack=no_ack
        )
        self._subscribers.append(data_dict)
        log.info('%s - Subscribers append success! queue_name:%s' % (self, queue_name))

    @property
    def subscribers(self):
        return self._subscribers


consumer = MQConsumer()
