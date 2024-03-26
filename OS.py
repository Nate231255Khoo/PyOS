import datetime,time,os,pytz,random
class randPrime:
    def randPrime(n):
        f = True
        while f:
            k = random.choice(range(2**(n-1),(2**n)-1))
            for i in range(3,round(k**1/2),2):
                if k % 2 == 0:
                    break
                elif k % i == 0:
                    break
                elif i >= round(k**1/2)-2:
                    f = False
                    break
        return k

class cache_user_data:
    def save(dict_data):
        f = open('user_data.txt','w')
        f.write(str(dict_data))
        f.close()
    def load():
        f = open('user_data.txt','r')
        data = f.read()
        f.close()
        return eval(data)
class user:
    users = cache_user_data.load()
    user = "guest"
class man:
    def man(i):
        if i == "help":
            print(i)
class hash:
    def hash(i):
        r = 1
        for h in [ord(j) for j in i]:
            r *= h

class OS:
    log = ""
    def help():
        print("help - returns this function")
        print("login - logs in to your account")
        print("adduser [username] [password] - adds a user, corresponding to the username and password")
        print("getlogs - shows the log history")
        print("gettime - shows the local time (CST)")
    def login():
        t = True
        while t:
            try:
                i = input("Username:")
                user.users[i]
                print(user.users[i])
                t = False
            except (NameError, KeyError):
                print("Invalid Username")
        if not t:
            j = input("Password:")
            if j == user.users[i]['password']:
                user.user = i
                print("Logged In!")
                print(f"Welcome {i}")

    def setTimeZone():
        print(pytz.all_timezones)
    def adduser(uname, upass):
        f = open('user_data.txt','r+')
        s = eval(f.read())
        s[uname] = {'password':upass,'tz':'Europe/London','region':None}
        f.write(str(s))
        f.close()
    def getTime():
        now = eval(datetime.datetime.now(user.users[user.user][tz]))
        print(f"{now.strftime('%H:%M:%S')}")
    def getLogs():
        print("|====Logs====|")
        print(OS.log.lstrip())
        print("|====Logs====|")
    def interpreter():
        while True:
            i = input(">>>  ")
            try:
                eval(i)
            except:
                pass
            if i == "help":
                print("Use quit to exit, and use help to come here")
            elif i == "quit":
                break



    def parse(args):
        if len(args) == 1:
            if args[0] == 'help':
                OS.help()
            elif args[0] == 'pyhelp':
                help()
            elif args[0] == 'login':
                OS.login()
            elif args[0] == 'getlogs':
                OS.getLogs()
            elif args[0] == 'gettime':
                OS.getTime()
            elif args[0] == 'interpreter':
                OS.interpreter()
            else:
                print("Invalid function")
        elif len(args) == 2:
            pass
        elif len(args) == 3:
            if args[0] == 'adduser':
                OS.adduser(args[1],args[2])
        else:
            print("Unable to parse")


