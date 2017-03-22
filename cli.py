#!/usr/bin/env python3.5
import os
import importlib
import argparse
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('path', help=u'方法指向的路径， 如 foo.bar  即 foo文件的bar函数')
parser.add_argument('--args', help=u'函数的参数', default='')
parser = parser.parse_args()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')


def import_module(dotted_path):
    module_parts = dotted_path.split(".")
    module_path = ".".join(module_parts[:-1])
    module = importlib.import_module(module_path)
    return getattr(module, module_parts[-1])


def main():
    path, args = parser.path, parser.args or []
    if not os.environ.get('VIRTUAL_ENV'):
        print(u'\n没有进入虚拟环境!!!\n')
    if 'server' not in path:
        from django import setup
        setup()
    path_str = 'utility.' + path
    func = import_module(path_str)
    func(*args)


if __name__ == "__main__":
    main()
