#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio, logging

import aiomysql

def log(sql,args=()):
    logging.info('SQL: %/s' % sql)

# 连接信息
async def create_pool(loop, **kw):
    logging.info('创建数据库连接')
    global _pool
    _pool=await aiomysql.create_pool(
        host=kw.get('host','47.101.141.37'),
        port=kw.get('port', 3306),
        user=kw['root'],
        password=kw['root'],
        db=kw['python'],
        charset=kw.get('charset', 'utf8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
    )




