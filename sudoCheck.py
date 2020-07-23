#!/usr/bin/python3
# Human.Gilland(charlotte)
# Function to respond to sudo password prompts when using pxssh()
# Requires ssh module from pexpect - pip install pexpect for dependency
from pexpect import pxssh

'''After sudo is invoked the function can be used to assess to 
prompt and input the sudo password if requested'''
def sudoCheck(adminPass,pxsshVar):
    s = pxsshVar # {1}
    #check for possible prompts
    p = s.expect(['.*:','.*\$']) # [1] pg14 {2}
    if p == 0: #if 1st item in list password needed
        s.sendline(adminPass)
        return s.prompt()
    elif p == 1: #if second item 
        return s.prompt()

#For reference
#[1] https://readthedocs.org/projects/pexpect/downloads/pdf/latest/ 

#End Notes
#{1} common pxssh covention s = pxssh.pxssh()
#    __inst__ must be carried over from current pxshh session
#   s = s = pxssh.pxssh()
#{2} List of expected promps [regex,regex]