#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from ryu.cmd import manager


def main():
    #Substitution with the full path to the script to be debugged / HOME/Tao/Workspace/python/ryu_test/app/simple_switch_lacp_13.py is already
    sys.argv.append('./shortestpath.py')
    sys.argv.append('--verbose')
    sys.argv.append('--enable-debugger')
    manager.main()

if __name__ == '__main__':
    main()