# -*- coding: utf-8 -*-
from datetime import datetime
import os
import platform
import re
import sys

import connexion

RAW_DIR     = '/hao/compdata1/Data/CoMP/raw'
PROCESS_DIR = '/hao/compdata1/Data/CoMP/process'

datedir_re = re.compile('^[0-9]{8}$')


def root():
    return {'server_name': platform.node(), 'time': datetime.now().isoformat()}

def valid_dirname(basedir, name):
    return os.path.isdir(os.path.join(basedir, name)) and re.match(datedir_re, name)

def dates():
    rnames = [name for name in os.listdir(RAW_DIR) if valid_dirname(RAW_DIR, name)]
    pnames = [name for name in os.listdir(PROCESS_DIR) if valid_dirname(PROCESS_DIR, name)]

    result = [{'date': d,
               'level': [{'name': 'L0',
                          'n_files': len(os.listdir(os.path.join(RAW_DIR, d)))}],
               'link': '/dates/%s' % d} for d in rnames]
    return result
    

if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='apispec/')
    app.add_api('data_api.yaml')

    # start the server
    app.run(port=1234)
