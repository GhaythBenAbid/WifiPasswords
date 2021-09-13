import subprocess

routers_data = subprocess.check_output(["netsh" , "wlan" , "show" , "profiles"]).decode('utf-8' , errors="backslashreplace").split('\n')


routers = []
for router in routers_data:
    if(":" in router):
        routers.append(router[router.index(":") + 2:-1])


passwords = []
for index in range(1,len(routers)):
    password_data = subprocess.check_output(["netsh" , "wlan" , "show" , "profile" , routers[index] , "key=clear"]).decode('utf-8' , errors="backslashreplace").split('\n')
    password_text = password_data[32]
    passwords.append(password_text[password_text.index(":") + 2:-1])

for index in range(1,len(routers)):
    print(routers[index] ," => " , passwords[index-1])