import datetime,time,os,pytz,random


f'''
|============================PyOS===============================|
|                                                               |
|    PyOS is an open source operating system based on python.   |
|         It is a very new and very bad operating system.       |
|  This project might as well be put off for the next few years |
|                But here I am working on this                  |
|                                                               |
|                       /==============|                        |
|                      / 0             |                        |
|                     |                |                        |
|                     |                |                        |
|              /======|========|       |======\                 |
|              |                       |      |                 |
|              |                       |      |                 |
|              |                       |      |                 |
|              |      |----------------|      |                 |
|              |      |                       |                 |
|              |      |                       |                 |
|              |      |                       |                 |
|              \======|        |=======|======/                 |
|                     |                |                        |
|                     |                |                        |
|                     |              0 /                        |
|                     |===============/                         |
|                                                               |
|===============================================================|

Current Version: 0.1.4

Update shenanigans:
1. Fixed settime
2. Fixed file-related functions
3. Added 'clear' to clear the console
4. Added 'timer' function
'''

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
    def hash(i,m):
        r = 1
        for h in [ord(j) for j in i]:
            r *= h
        for b in [ord(l) for l in m]:
            r *= b
        return r

class OS:
    log = ""
    def help():
        print("help - returns this function")
        print("login - logs in to your account")
        print("adduser [username] [password] - adds a user, corresponding to the username and password")
        print("deluser ")
        print("getlogs - shows the log history")
        print("gettime - shows the local time (UTC)")
        print("settime - sets your time zone to the current time")
        print("clear - clears the console <added in 0.1.4>")
        print("timer [s] - displays a timer with the amount of time left <added in 0.1.4>")
    def login():
        t = True
        while t:
            try:
                i = input("Username:")
                user.users[i]
                t = False
            except (NameError, KeyError):
                print("Invalid Username")
        if not t:
            j = input("Password:")
            if hash.hash(j,i) == user.users[i]['password']:
                user.user = i
                print("Logged In!")
                print(f"Welcome {i}")

    def setTimeZone():
        print(pytz.common_timezones)
        i = input("Timezone:    ")
        if i in pytz.common_timezones:
            f = open('user_data.txt','r')
            d = eval(f.read())
            j = d[user.user]['tz']
            d[user.user]['tz'] = i
            a = str(d).replace(j,i)
            with open('user_data.txt','w') as h:
                h.write(a)
    def adduser(uname, upass):
        with open('user_data.txt','r') as f:
            s = eval(f.read())
        s[uname] = {'password':hash.hash(upass,uname),'tz':'Europe/London','region':None}
        with open('user_data.txt','w') as f:
            f.write(str(s))
    def getTime():
        now = datetime.datetime.now(pytz.timezone(user.users[user.user]['tz']))
        return f"{now.strftime('%H:%M:%S')}"
    def getLogs():
        print("|====Logs====|")
        print(OS.log.lstrip())
        print("|====Logs====|")

    def timer(n):
        n = int(n)
        while n > 0:
            print(f'''
            ╔══════════════════════════╗
            ║ Time Left: {int(n/3600):>2}h:{int(n/60)%60:>2}m:{n%60:>2}s   ║
            ╚══════════════════════════╝
            ''')

            time.sleep(1)
            n -= 1
            os.system('clear')
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
    def deluser(u):
        if u == 'guest':
            print("<GUEST>: I am Inevitable")
            return None
        try:
            print(u)
            with open('user_data.txt','r') as f:
                d = eval(f.read())
            with open('user_data.txt','w') as f:
                del d[u]
                f.write(str(d))

        except (NameError,KeyError):
            print(f"No user named {u}")




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
                print(OS.getTime())
            elif args[0] == 'interpreter':
                OS.interpreter()
            elif args[0] == 'settime':
                OS.setTimeZone()
            elif args[0] == 'clear':
                os.system('clear')
            else:
                print("Invalid function")
        elif len(args) == 2:
            if args[0] == 'deluser':
                OS.deluser(args[1])
            if args[0] == 'timer':
                OS.timer(args[1])
        elif len(args) == 3:
            if args[0] == 'adduser':
                OS.adduser(args[1],args[2])
        else:
            print("Unable to parse")

'''
|===============================================================|
|                                                               |
|                       /==============|                        |
|                      / 0             |                        |
|                     |                |                        |
|                     |                |                        |
|              /======|========|       |======\                 |
|              |                       |      |                 |
|              |                       |      |                 |
|              |                       |      |                 |
|              |      |----------------|      |                 |
|              |      |                       |                 |
|              |      |                       |                 |
|              |      |                       |                 |
|              \======|        |=======|======/                 |
|                     |                |                        |
|                     |                |                        |
|                     |              0 /                        |
|                     |===============/                         |
|                                                               |
|===============================================================|
|                                                               |
|                 z     /==============|                        |
|                  z   / _             |                        |
|                   z |                |                        |
|                     |                |                        |
|              /======|========|       |======\                 |
|              |                       |      |                 |
|              |          sleepython   |      |                 |
|              |                       |      |                 |
|              |      |----------------|      |                 |
|              |      |                       |                 |
|              |      |  time.sleep(36000)    |                 |
|              |      |                       |                 |
|              \======|        |=======|======/                 |
|                     |                |                        |
|                     |                |   z                    |
|                     |              _ /  z  z                  |
|                     |===============/        z                |
|                                                               |
|===============================================================|
|                           o                                   |
|                           /\                                  |
|                          /  \                                 |
|                         /    \                                |
|                       /==============|                        |
|                      / n             |                        |
|                     |                |                        |
|                     |                |                        |
|              /======|========|       |======\                 |
|              |                       |      |                 |
|              |                       |      |                 |
|              |                       |      |                 |
|              |      |----------------|      |                 |
|              |      |                       |                 |
|              |      |                       |                 |
|              |      |                       |                 |
|              \======|        |=======|======/                 |
|                     |                |                        |
|                     |                |                        |
|                     |              u /                        |
|                     |===============/                         |
|                              \    /                           |
|                               \  /                            |
|                                \/                             |
|                                o                              |
|                   Happy Birthday Python!                      |
|                          2/20/1991                            |
|===============================================================|
|                                                               |
|                       /==============|                        |
|                      / 0             |                        |
|                     |                |                        |
|                     |                |                        |
|              /======|========|       |======\                 |
|              |                       |/\/\/\|                 |
|              |                       |\/\/\/|                 |
|              |                       |/\/\/\|                 |
|              |      |----------------|\/\/\/|                 |
|              |      |\/\/\/\/\/\/\/\/\/\/\/\|                 |
|              |      |/\/\/\/\/\/\/\/\/\/\/\/|                 |
|              |      |\/\/\/\/\/\/\/\/\/\/\/\|                 |
|              \======|/\/\/\/\|=======|======/                 |
|                     |\/\/\/\/\/\/\/\/|                        |
|                     |/\/\/\/\/\/\/\__|                        |
|                     |\/\/\/\/\/\/\/ 0/                        |
|                     |===============/                         |
|                                                               |
|===============================================================|
|                                                               |
|                                                               |
|             |===============================|                 |
|             |                               |                 |
|             |                               |                 |
|             |                               |                 |
|             |                               |                 |
|             |                               |                 |
|             |                               |                 |
|             |                               |                 |
|             |                               |                 |
|             |                               |                 |
|             |              |=====|  //===\\ |                 |
|             |                  ||   ||      |                 |
|             |                  ||   \\===\\ |                 |
|             |             ||   ||        || |                 |
|             |              \\==//   \\===// |                 |
|             |===============================|                 |
|                                                               |
|                                                               |
|===============================================================|
|                                                               |
|                                                               |
|                  Big Brother is watching...                   |
|                                                               |
|                                                               |
|                      ================                         |
|                 ====//              \\====                    |
|                //   ||    /====\    ||    \\                  |
|              ==     ||    |    |    ||      ==                |
|             //      ||    |    |    ||       \\               |
|            ||       ||    |    |    ||        ||              |
|             \\      ||    |    |    ||       //               |
|              ==     ||    |    |    ||     ==                 |
|                \\   ||    \====/    ||   //                   |
|                 ====\\              //====                    |
|                      ================                         |
|                 ||   //==\\   //==\\    // ||                 |
|                =||  ||    || ||    ||  //  ||                 |
|                 ||   \\==//   >>==<<   =======                |
|                 ||      //   ||    ||      ||                 |
|                ====    //     \\==//       ||                 |
|                                                               |
|===============================================================|
'''

