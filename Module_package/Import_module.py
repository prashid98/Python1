import mod1 as Module1
import mod2 as Module2
#build in module 
import platform

#import data from the module file
new_num= Module1.module_num_list
print(list(new_num))

#import data from the buildin module
sys=dir(platform)
print(sys)

#importing the 2 different module and having a computation among them
sum = Module1.module_num_list + Module2.module2_num_list
print(list(sum))