#!/usr/bin/env python
# -*- coding=utf-8 -*-

"""
@version: 0.0.1
@author: lee
@license: Apache Licence
@contact: shida23577@hotmail.com
@software: PyCharm Community Edition
@file: DBTypes.py
@time: 2016/6/7 14:33
"""
__title__ = ''
__version = ''
__build__ = 0x000
__author__ = 'lee'
__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2016 li shi da'

import sqlalchemy
from sqlalchemy import Column, String, VARCHAR, create_engine  #导入包
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.interfaces import MapperExtension
from datetime import datetime

class DataUpdateExtension(MapperExtension):
    def before_update(self, mapper, connection, instance):
        if hasattr(instance, "create_time"):
            instance.create_time = datetime.now()
TableBase = declarative_base()
class DeviceServerInfoTable(TableBase):
    __tablename__ = "DeviceServerInfo"
    __mapper_args__ = {'extension':DataUpdateExtension()}
    serverIP = Column(VARCHAR(16), nullable=False, primary_key=True)
    cpuCount = Column(sqlalchemy.INT, nullable=False)
    physicalCpuCount = Column(sqlalchemy.INT, nullable=False)
    memSize = Column(sqlalchemy.FLOAT(10,2))
    availableMemory = Column(sqlalchemy.FLOAT(10,2))
    memUseRate = Column(sqlalchemy.FLOAT(5,2))
    netReceiving = Column(sqlalchemy.FLOAT(10,2))
    netSending = Column(sqlalchemy.FLOAT(10,2))
    create_time = Column(sqlalchemy.DateTime, nullable=False, server_default=text('(datetime(\'now\', \'localtime\'))'))

class DeviceRegisterInfoTable(TableBase):
    __tablename__ = "DeviceRegisterInfo"
    serviceID = Column(VARCHAR(100), nullable=False, primary_key=True)
    allDeviceCount = Column(sqlalchemy.INT, nullable=False, default=0)
    registerSuccesscount = Column(sqlalchemy.INT, nullable=False, default=0)
    registerFailcount = Column(sqlalchemy.INT, nullable=False, default=0)
    registerSuccessDeviceList = Column(sqlalchemy.TEXT)
    registerFailDeviceList = Column(sqlalchemy.TEXT)
    create_time = Column(sqlalchemy.DateTime, nullable=False, server_default=text('(datetime(\'now\', \'localtime\'))'), primary_key=True)

class ServiceLoadingInfoTable(TableBase):
    __tablename__ = "ServiceLoadingInfo"
    serviceID = Column(VARCHAR(100), nullable=False, primary_key=True)
    cpuUseRate = Column(sqlalchemy.FLOAT(5,2))
    memUseRate = Column(sqlalchemy.FLOAT(5,2))
    useMemory = Column(sqlalchemy.FLOAT(10,2))
    availableMemory = Column(sqlalchemy.FLOAT(10,2))
    threadCount = Column(sqlalchemy.INT)
    create_time = Column(sqlalchemy.DateTime, nullable=False, server_default=text('(datetime(\'now\', \'localtime\'))'), primary_key=True)

class ServiceStatusInfoTable(TableBase):
    __tablename__ = "ServiceStatusInfo"
    serviceID = Column(VARCHAR(100), nullable=False, primary_key=True)
    status = Column(sqlalchemy.BOOLEAN, default=False)
    Column(VARCHAR(500))
    create_time = Column(sqlalchemy.DateTime, nullable=False, server_default=text('(datetime(\'now\', \'localtime\'))'), primary_key=True)

class PushStatusInfoTable(TableBase):
    __tablename__ = "PushStatus"
    serviceID = Column(VARCHAR(30), nullable=False, primary_key=True)
    deviceID = Column(VARCHAR(100), nullable=False, primary_key=True)
    channel = Column(sqlalchemy.INT, nullable=False, default=0 )
    status = Column(sqlalchemy.BOOLEAN, default=True)
    errMsg = Column(VARCHAR(100))
    pushTime = Column(sqlalchemy.DateTime, nullable=False, server_default=text('(datetime(\'now\', \'localtime\'))'), primary_key=True)
    create_time = Column(sqlalchemy.DateTime, nullable=False, server_default=text('(datetime(\'now\', \'localtime\'))'), primary_key=True)

class PushStreamUrlInfoTable(TableBase):
    __tablename__ = "PushStreamUrl"
    serviceID = Column(VARCHAR(30), nullable=False, primary_key=True)
    urlCount = Column(sqlalchemy.INT, nullable=False, default=0)
    urlContent = Column(sqlalchemy.TEXT)
    pushTime = Column(sqlalchemy.DateTime, nullable=False, server_default=text('(datetime(\'now\', \'localtime\'))'), primary_key=True)
    create_time = Column(sqlalchemy.DateTime, nullable=False, server_default=text('(datetime(\'now\', \'localtime\'))'), primary_key=True)
class UrlTableData():
    def __init__(self):
        self.protocol=None
        self.deviceID=None
        self.deviceIP=None
        self.channel=None
        self.streamType=None
        self.url=None
        self.createDate=None
        self.updateDate=None



