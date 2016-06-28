#!/usr/bin/python
# -*- coding: utf-8 -*-

def assert_msg(pred, msg = ""):
    if not pred:
        print msg
        exit(-1)