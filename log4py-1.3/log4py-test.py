#!/usr/bin/python
# -*- coding: utf-8 -*-

import log4py
import sys
from os import utime
from time import time

class Log4PyTest:

    def __init__(self):
        self.log4py = log4py.Logger().get_instance(self)

    def run(self):
        self.log4py.error("error message")
        self.log4py.warn("warn message")
        self.log4py.info("info message")
        self.log4py.debug("debug message")

    def output(self, message):
        self.log4py.info(message)

mytest = Log4PyTest()

print ("\nSettings from log4py.conf\n")
mytest.run()

print ("\nNormal level - Long format (written to d:\\test\\log4py-test.log)")
mytest.log4py.set_target("d:\\test\\log4py-test.log")
mytest.run()
mytest.log4py.set_target(sys.stdout)

print ("\nNormal level - Long format (ansi color)\n")
mytest.log4py.set_use_ansi_codes(log4py.TRUE)
mytest.run()
mytest.log4py.set_use_ansi_codes(log4py.FALSE)


print ("\nDebug level - Debug format\n")
mytest.log4py.set_formatstring(log4py.FMT_DEBUG)
mytest.log4py.set_loglevel(log4py.LOGLEVEL_DEBUG)
mytest.run()

print ("\nVerbose level - Medium format\n")
mytest.log4py.set_formatstring(log4py.FMT_MEDIUM)
mytest.log4py.set_loglevel(log4py.LOGLEVEL_VERBOSE)
mytest.run()

print ("\nVerbose level - User defined format\n")
mytest.log4py.set_formatstring("[ %u (%F) ] %D: %M")
mytest.log4py.set_loglevel(log4py.LOGLEVEL_VERBOSE)
mytest.run()

print ("\nNormal, long format - Testing Nested Diagnostic Context\n")
mytest.log4py.set_formatstring(log4py.FMT_LONG)
mytest.log4py.set_loglevel(log4py.LOGLEVEL_VERBOSE)
mytest.log4py.push("ndc1")
mytest.output("Should say \"ndc1\"")
mytest.log4py.push("ndc2")
mytest.output("Should say \"ndc1 ndc2\"")
mytest.log4py.pop()
mytest.output("Should say \"ndc1\"")
mytest.log4py.push("ndc3")
mytest.output("Should say \"ndc1 ndc3\"")
mytest.log4py.clear_ndc()
mytest.output("Should not have any ndc items")
"""
print "\nTesting MySQL target\n"
mytest.log4py.add_target(log4py.TARGET_MYSQL, "localhost", "syslog", "log4py", "mysecretpwd", "logs")
mytest.output("hello world")
mytest.log4py.remove_target(log4py.TARGET_MYSQL)

print ("\nTesting Syslog target\n")
mytest.log4py.add_target(log4py.TARGET_SYSLOG)
mytest.run()
mytest.log4py.remove_target(log4py.TARGET_SYSLOG)
"""
print ("\nGetting all available targets\n")
print (mytest.log4py.get_targets())

print ("\nTesting log-file rotation (d:\\test\\log4py-rotation.log)\n")
mytest.log4py.set_target("d:\\test\\log4py-rotation.log")
mytest.run()

#按日期输出文件
mytest.log4py.set_rotation(log4py.ROTATE_DAILY)
yesterday = time() - 60 * 60 * 24  #昨天
#os.utime() 方法用于设置指定路径文件最后的修改和访问时间
utime("d:\\test\\log4py-rotation.log", (yesterday, yesterday))
mytest.run()

#测试debug时改时间来处理，可以自动改日期log4py-new-y-m-d.log
i=0
mytest.log4py.set_target("d:\\test\\log4py-new.log")
mytest.log4py.set_rotation(log4py.ROTATE_DAILY)
while i<100 :
    mytest.run()  #output message
    i+=1
    pass

mytest.log4py.set_target(sys.stdout)
