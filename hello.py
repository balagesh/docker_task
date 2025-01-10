#!/usr/bin/env python3
import os

username = os.getenv("USER")
print(f"Hello, {username}!")
print("current working directory: "+str((os.getcwd())))
print("current process' real user id: "+str(os.getuid()))
print("directories in which the system looks for named exec progs: ")
for x in (os.get_exec_path()):
    print("* "+x)
print(("size of terminal: "+str(os.get_terminal_size())))
