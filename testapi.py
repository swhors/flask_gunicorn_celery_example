import os,sys
import logging
from celery import Celery, Task
from flask_restful import Resource, request

from tcelery import celery_app


class TestApi_Old(Resource):

    @staticmethod
    @celery_app.task
    def printhw(ppid: int) -> str:
        msg = f"Pid => {ppid}, {os.getpid()}"
        return {'msg': msg}


    @classmethod
    def get(cls) -> str:
        ret = cls.printhw.apply_async((os.getpid(),))
        return ret.get(timeout = 1)


class TestApi_New(Resource):

    @classmethod
    def printhw_internal(cls, ppid:int) -> str:
        msg = f"Pid => {ppid}, {os.getpid()}"
        return msg


    @classmethod
    def printhw(cls, ppid: int) -> str:
        msg = cls.printhw_internal(ppid)
        return {'msg': msg}


    @classmethod
    def get(cls) -> str:
        from testapi import printhw_ex
        ret = printhw_ex.delay(os.getpid())
        return ret.get(timeout = 1)


@celery_app.task
def printhw_ex(ppid: int) -> str:
    return TestApi_New.printhw(ppid)


