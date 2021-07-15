import os,sys
import logging
from celery import Celery, Task
import celery

class TCelery():

    tcelery = None

    def __init__(self, name: str, broker: str):
        self._name = name
        self._broker = broker
        #self._handle = Celery(self._name,
        self._handle = Celery( broker=self._broker,
                               backend=self._broker)
        #self._handle = Celery()


        self._handle.conf.update(
            task_serializer='json',
            accept_content=['json'],
            result_serializer='json',
            timezone='Asia/Seoul',
            enable_utc=True,
        )


    @staticmethod
    def get_celery(name: str, broker: str) -> Celery:
        if TCelery.tcelery is None:
            TCelery.tcelery = TCelery(name=name, broker=broker)
        return TCelery.tcelery._handle


def get_celery() -> Celery:
    from tcelery import TCelery
    return TCelery.get_celery(name="main",broker="redis://localhost:6379/1")


celery_app = get_celery()

import testapi 
