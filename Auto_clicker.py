import mouse, keyboard, time, os, datetime

def Config():
    print("Click every")
    hour = int(input("Hour: "))
    minute = int(input("Minute: "))
    second = float(input("Second: "))
    total_time = hour * 3600 + minute * 60 + second

    print("f6 to start and f10 to stop")
    keyboard.wait("f6")
    clicking = True
    while clicking:

        mouse.click()
        s = datetime.datetime.now()

        while (datetime.datetime.now() - s).total_seconds() < total_time:
            # This runs while the difference in time since you started the loop is less than the time you want to wait
            if keyboard.is_pressed("f10"):
                clicking = False
                greeting()
                break


def Fastest():
    print("f6 to start and f10 to stop")
    keyboard.wait("f6")
    clicking = True
    while clicking:

        mouse.click()

        if keyboard.is_pressed("f10"):
            clicking = False
            greeting()
            break


def greeting():
    
    print("""  
    Auto clicker!!!
       By ze
    """)
    time.sleep(3)
    os.system('cls')
        
    print(
            """
IMPORTANT
    
    This auto clicker can lag and break your pc
    
    The config mode is where u make it click at what time u desire, If you make the settings to low/fast your pc might crash
    
    The fastest mode makes it click as fast as it can BUT it makes your pc laggy
    
    Milliseconds in seconds eg. 0.1
    """
        )
        
    time.sleep(3.4)
    
    os.system("cls")
    global choose
    choose = int(input(
            """
1. Config
2. Fastest 
    
"""))
    
    if choose == 1:
        Config()
    elif choose == 2:
        Fastest()




greeting()