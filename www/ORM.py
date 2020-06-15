# -*- coding: utf-8 -*-

import asyncio
import aiomysql
import logging


def log(sql,args = ()):
    logging.info('SQL: %s'%sql)


