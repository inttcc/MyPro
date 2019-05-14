#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import logging

logging.basicConfig(
    filename='runlog.log',
    level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
)

logging.debug('debug info')
logging.info('hello world')
logging.warning('warning info')
logging.error('error info')
logging.critical('critical info')