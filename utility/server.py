import os
import re
import subprocess

from config.settings.common import PROJECT_NAME, ROOT_DIR, FE_DIR, CONFIG_DIR
dirname = os.path.dirname
PROJECT_PATH = ROOT_DIR
VIR_PATH = dirname(PROJECT_PATH)

g = dict(
    VIR_PATH=VIR_PATH,
    PROJECT_PATH=PROJECT_PATH,
    CONFIG_PATH=CONFIG_DIR,
    PROJECT_NAME=PROJECT_NAME,
    FE_DIR=FE_DIR)

_re = re.compile(r'\{(.*?)\}')


def start():
    source = 'source {}/bin/activate'.format(VIR_PATH)
    _call(source)
    uwsgi = 'uwsgi --ini {}/uwsgi.ini'.format(CONFIG_PATH)
    _call(uwsgi)


def stop():
    uwsgi = 'uwsgi --stop {}/{}.pid'.format(CONFIG_PATH, PROJECT_NAME)
    r = _call(uwsgi)
    r and _call('killall -9 uwsgi')


def restart():
    render()
    uwsgi = 'uwsgi --reload {}/{}.pid'.format(CONFIG_PATH, PROJECT_NAME)
    r = _call(uwsgi)
    r and start()  # pid不存在时, 即没有启动uwsgi 返回1


def _call(command):
    result = subprocess.call(command, shell=True)
    return result


def _render(filename):
    print('filename is {}'.format(filename))
    f = open(filename, 'r+')
    lines = f.readlines()
    for num, line in filter(lambda x: _re.findall(x[1]), enumerate(lines)):
        line = line.format(**g)
        lines[num] = line
        print(
            'format line {} to {}'.format(num, line),
            end='', )
    text = ''.join(lines)
    f.seek(0)
    f.write(text)
    f.truncate()
    f.close()


def render():
    print('\nrender config file:')
    print('PROJECT_PATH is {}'.format(PROJECT_PATH))
    print('VIR_PATH is {}'.format(VIR_PATH))
    rendered_list = [x for x in os.listdir('config/')
                     if x.endswith('.ini') or x.endswith('.conf')]
    [_render(str(CONFIG_DIR.path(x))) for x in rendered_list]


def printer():
    print(g)
