import OS, pytz, datetime

print(
'''
|============================PyOS===============================|
|                       /==============|                        |
|   |\  | | /          / 0             |                        |
|   | \ | |<          |                |                        |
|   |  \| | \         |                |                        |
|              /======|========|       |======\                 |
|              |                       |      |                 |
|              |       Python : 3.12.2 |      |                 |
|              |                       |      |                 |
|              |      |----------------|      |                 |
|              |      |                       |                 |
|              |      | PyOS  : 0.1.4         |                 |
|              |      |                       |                 |
|              \======|        |=======|======/                 |
|                     |                |                        |
|                     |                |                        |
|                     |              0 /                        |
|                     |===============/                         |
|===============================================================|
'''
)
while True:
    try:
        OS.user.users = OS.cache_user_data.load()
        j = input(f"P:/users/{OS.user.user}/").split()
        local_now = datetime.datetime.now(pytz.timezone(OS.user.users[OS.user.user]["tz"]))
        OS.OS.log += f"\n[{local_now.strftime('%H:%M:%S')}] {''.join(j)}"
        OS.OS.parse(j)
    except Exception as err:
        f = open('log.txt','r+')
        f.write(f"{str(OS.OS.log).lstrip()}\n{err} occured")
        f.close()
    except KeyboardInterrupt:
        f = open('log.txt','r+')
        f.write(f"{str(OS.OS.log).lstrip()}")
        f.close()
        
        break
