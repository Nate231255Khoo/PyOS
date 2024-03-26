import pytz,random
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
                    print(k)
                    f = False
                    return k
f = open("user_data.txt","w")
f.write(str({"guest":{"password":"guest","tz":"Europe/London","region":None,"hash":randPrime.randPrime(32)}}))
f.close()
