#!/usr/bin/env python
# -*- coding: utf-8 -*-

s1 = [5, 4, 3, 1, 1, 2, 2]


def uredi2(list):
    s2 = []
    i = 0
    a = 0

    while list:
        if list[i] <= a:
            s2.append(list.pop(i))
            i = 0
        elif list[i] == list[-1]:
            i = 0
            a += 1
        elif list[i] <= a:
            s2.append(list.pop(i))
            del list[i]
            i = 0
            a += 1
        else:
            i += 1
    print s2

uredi2(s1)

