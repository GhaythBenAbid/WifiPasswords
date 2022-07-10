import subprocess

routers_data = subprocess.check_output(["netsh" , "wlan" , "show" , "profiles"]).decode('utf-8' , errors="backslashreplace").split('\n')


routers = []
for router in routers_data:
    if(":" in router):
        routers.append(router[router.index(":") + 2:-1])

passwords = []
for router in routers:
    if(router != ""):
        password_data = subprocess.check_output(["netsh" , "wlan" , "show" , "profile" , router , "key=clear"]).decode('utf-8' , errors="backslashreplace").split('\n')
        password_text = password_data[32]
        try:
            passwords.append(password_text[password_text.index(":") + 2:-1])
        except:
            passwords.append("No password found")

for index in range(1,len(routers)):
    print(routers[index] ," => " , passwords[index-1])