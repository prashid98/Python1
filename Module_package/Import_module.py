import mod1 as Module
#build in module 
import platform

#import data from the module file
new_num= Module.module_num_list
print(list(new_num))

#import data from the buildin module
sys=dir(platform)
print(sys)