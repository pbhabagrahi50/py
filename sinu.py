
# a=input("Type a number : ")
# b=input("2nd value : ")
# c= a<b
# # print (type(c),c)
# d=a>=b
# if c is True :
#     print('hello world')

# elif d is True :
#     print('helloworld 2')
    
# else:
#     print('false')
# f= 'hello world'
# print(f)
# my_list=[1,5,6,78,46,"hello","world",]
# first_list=my_list[4:7]
# first_list.append(["raju","herry","papu","sinu"])
# if "papu" in first_list:
#     print('last word : ',first_list,":",len(first_list))
# servers = ['web-server-01', 'db-server-01', 'app-server-01']
# system=servers
# system.remove('db-server-01')
# print(servers)
# print(system)
# import re
# def sys():
#    servers = ['server','web-server-01', 'db-server-01', 'app-server-01']
#    return servers
# pax=sys()
# jex=input("server_name : ")
# pax.append(jex)
# for rex in pax:
#    print(rex)


# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)
# dex=['hacker','devloper','ui/ux designer']
# rex=dex
# print(rex)



# count = 0
# while count < 100:
#     print(count)
#     count += 1


# log_file = [
#    "INFO: Operation successful",
#    "ERROR: File not found",
#    "DEBUG: Connection established",
#    "ERROR: Database connection failed",
# ]
# dex=input("keyword : ")
# rex=(dex.upper())
# for line in log_file:
#     if rex in line:
#         print(line)


import os
def main():
    folder_paths =input("Enter Folder Path : ").split()
    return folder_paths
for folders in main():
    # try:
        files=os.listdir(folders)
    # except FileNotFoundError:
    #     print("pls provide a valid folder name"+ folders)
    #     continue
    # except PermissionError:
    #     print("No access to the folder"+folders)
        print("===== listing files for the Folder === " + folders)


for file in files:
    print(file)
