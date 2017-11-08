#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: stdrickforce (Tengyuan Fan)
# Email: <stdrickforce@gmail.com> <fantengyuan@baixing.com>

import time

f = True
while True:
    print('tick' if f else 'tock')
    f = not f
    time.sleep(1)
