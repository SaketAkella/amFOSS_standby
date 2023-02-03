import time, pyperclip, datetime

def stopwatch():
    print("Press 'Enter' to begin, press it again to start the watch. Crtl-c to quit.")
    input()
    print("Stopwatch started...")
    line = ' '
    startTime = time.time()
    lastTime = startTime
    lapNum = 1

    try:
        while True:
            input()
            lapTime = round(time.time()-lastTime,2)
            totalTime = round(time.time()-startTime,2)
            output = 'LAP#%s %s %s' %(str(lapNum).rjust(2), str(totalTime).center(5), str(lapTime).rjust(6))
            line+=output + '\n'
            print(output, end=" ")
            lapNum+=1
            lastTime=time.time()
    except KeyboardInterrupt:
        print("\n Exitted")

if __name__=="__main__":
    stopwatch()







