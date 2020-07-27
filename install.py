import os

to_be_installed = [
    'flask',
    'flask_bootstrap',
    'flask_moment',
    'flask_script',
    'flask_wtf',
    'flask_sqlalchemy',
    'pymysql'
]

import_str = "__import__('{}')"
install_cmd = 'pip install {}'

for i in to_be_installed:
    try:
        eval(import_str.format(i))
    except ImportError:
        os.system(install_cmd.format(i))