import OS, pytz, datetime

while True:
    j = input(f"P:/users/{OS.user.user}/").split()
    local_now = datetime.datetime.now(pytz.timezone(OS.user.users[OS.user.user]["tz"]))
    OS.OS.log += f"\n[{local_now.strftime('%H:%M:%S')}] {''.join(j)}"
    OS.OS.parse(j)