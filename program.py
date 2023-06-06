import webbrowser
import time

# tis is first ptoject with python
stat_time=time.ctime()
start = 1 #start 1
target = 10 # end in 10 times
while start<=target :
    webbrowser.open("https://www.youtube.com/watch?v=oMqIjZoz9co&pp=ygUZaW5mZWN0ZWQgdmFsb3JhbnQgbW9udGFnZQ%3D%3D")
    time.sleep(60*60)
    start=start+1
#end program
