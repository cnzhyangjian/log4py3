Log4Py ReadMe:

Log4Py is a Python logging module similar to log4j. It supports multiple levels
of logging and configurable output (either to stdout/stderr or to files). A
list of available format strings and ouput parameters can be found at the
beginning of log4py.py.

Installation:

    Automatic:
        Using Python's Distutils, you can execute:
        "python setup.py install"

    Manually:
        Either copy log4py.py into your project directory or to your site-packages directory.

Usage:

    from log4py import Logger

    class foo:
        def __init__(self):
	    cat = Logger().get_instance(self)

    Have a look at log4py-test.py and log4py-classtest.py for examples.
    For logging to databases, please have a look at the database/ directory

If you have any comments or questions, don't hesitate to contact me ;-)

Martin 						<Martin.Preishuber@eclipt.at>

2019-09-05 修订为python3运行代码（实测3.6.1成功）
1. 迁移中mysqldb，改下载mysqlclient，手动安装(注意与python平台一致，32位或64位）
2. 迁移中types的类型判定，字符串用type(xxx)==type('1')形式，判定是否为类，则用inspect.isclass
3. 迁移中String对应函数，改为log4py.py中函数改调用str.xxx函数
4. 迁移中环境变量字典dict.has_key改为 xx in dict.keys
5. 在vscode中调试单元测试成功（屏蔽mysql相关测试）


