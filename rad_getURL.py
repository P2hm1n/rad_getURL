# -*- coding: utf-8 -*-
# @Author  : P2hm1n
# @Software: PyCharm
# @Blog    ：https://p2hm1n.com/

import subprocess


def scan(fileline):
    target_txt = filter_target(fileline + ".txt")
    cmd = ["./rad", "-t", fileline, "-text-output", target_txt]
    rsp = subprocess.Popen(cmd)
    output, error = rsp.communicate()
    print(output)


def filter_target(target):
    if "://" in target:
        target_split = target.split("://")[1]
    else:
        target_split = target
    if target_split.endswith("/"):
        final_target_split = target_split[:-1]
    else:
        final_target_split = target_split
    return final_target_split


def myfilter(sfilename):
    filename = filter_target(sfilename + ".txt")
    with open(filename) as f1:
        with open("filter_" + filename, 'a+') as f2:
            for line in f1.readlines():
                line2 = line.strip().split()[1]
                f2.write(line2 + "\n")


if __name__ == '__main__':
    with open("url.txt") as f1:
        for line in f1.readlines():
            data = line.strip('\n')
            scan(data)
            myfilter(data)
            cmd = ["rm", filter_target(data + ".txt")]
            subprocess.Popen(cmd)
