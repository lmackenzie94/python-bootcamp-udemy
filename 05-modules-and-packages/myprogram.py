from mymodule import my_func  # import from module
from MyMainPackage import some_main_script  # import from package
# these only work b/c of the __init__ files
from MyMainPackage.SubPackage import mysubscript

my_func()
some_main_script.report_main()
mysubscript.sub_report()
