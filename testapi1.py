import os,sys
import logging
from celery import Celery, Task
from flask_restful import Resource, request


class TestApi_Old(Resource):

    @staticmethod
    def printhw(ppid: int) -> str:
        msg = f"Pid => {ppid}, {os.getpid()}"
        return {'msg': msg}


    @classmethod
    def get(cls) -> str:
        return cls.printhw(os.getpid())

from lib.psql import PSQL

psql = PSQL()

class Api_StudentAdd(Resource):

    @classmethod
    def insert_student(cls, name:str, grade: int, work):
        psql.insert(name=name, grade = grade, work=work)

    @classmethod
    def post(cls, name: str, grade: int):
        work_data= request.data
        cls.insert_student(name, grade, work_data)
        return 'OK',200

class TestApi_New(Resource):

    @classmethod
    def printhw_internal(cls, ppid:int) -> str:
        import math
        t = 0
        for i in range(0,2000):
            t += i 
        t = math.sqrt(t)
        t = math.pow(t,2)
        t = math.sqrt(t)
        t = math.pow(t,2)
        t = math.sqrt(t)
        t = math.pow(t,2)
        t = math.sqrt(t)
        t = math.pow(t,2)
        msg = f"Pid => {ppid}, {os.getpid()}, {t}"
        return msg


    @classmethod
    def printhw(cls, ppid: int) -> str:
        msg = cls.printhw_internal(ppid)
        return {'msg': msg}


    @classmethod
    def get(cls) -> str:
        return cls.printhw(os.getpid())
