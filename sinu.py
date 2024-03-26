
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
def sys():
   servers = ['web-server-01', 'db-server-01', 'app-server-01']
   return servers
pax=sys()
jex=input("server_name : ")
pax.append(jex)
print(pax)
print(jex)
print(sys())
