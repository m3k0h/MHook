from os import system
from colorama import Fore, init
import time as tm
import itertools
from dhooks import Webhook, Embed, File
import keyboard
init(autoreset=True)

system("title MHOOK")
system("cls")
print(Fore.RED+'''
    
            ███╗   ███╗██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
            ████╗ ████║██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
            ██╔████╔██║███████║██║   ██║██║   ██║█████╔╝ 
            ██║╚██╔╝██║██╔══██║██║   ██║██║   ██║██╔═██╗ 
            ██║ ╚═╝ ██║██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
            ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝

                     '''+Fore.WHITE+'''MHook - Creation of Mekoih
                     ''')
hook = Webhook(input(Fore.RED+"[+] WebHook: "+Fore.WHITE))

def mhook_wh():
    system("cls")
    print(Fore.RED+'''
    
            ███╗   ███╗██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
            ████╗ ████║██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
            ██╔████╔██║███████║██║   ██║██║   ██║█████╔╝ 
            ██║╚██╔╝██║██╔══██║██║   ██║██║   ██║██╔═██╗ 
            ██║ ╚═╝ ██║██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
            ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝

                     '''+Fore.WHITE+'''MHook - Creation of Mekoih
    
    ''')
    system("cls")
    print(Fore.RED+'''
    
            ███╗   ███╗██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
            ████╗ ████║██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
            ██╔████╔██║███████║██║   ██║██║   ██║█████╔╝ 
            ██║╚██╔╝██║██╔══██║██║   ██║██║   ██║██╔═██╗ 
            ██║ ╚═╝ ██║██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
            ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝

                     '''+Fore.WHITE+'''MHook - Creation of Mekoih
    
    ''')
    print(Fore.RED+'''
    [1] WH Info
    [2] Infinite Message Spam 
    [3] Infinite Embed Spam
    [4] Change Name (of Webhook)
    [5] Remove Webhook
    [X] Exit

    ''')
    opt = input(">> ")
    def animate():
        print(Fore.RED+"Wait")
        system("cls")
        print(Fore.RED+"Wait.")
        system("cls")
        print(Fore.RED+"Wait..")
        system("cls")
        print(Fore.RED+"Wait...")
        system("cls")
        print(Fore.RED+"Wait")
        system("cls")
        animate()
    if opt=="1":
        system("cls")
        print(Fore.RED+'''
    
            ███╗   ███╗██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
            ████╗ ████║██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
            ██╔████╔██║███████║██║   ██║██║   ██║█████╔╝ 
            ██║╚██╔╝██║██╔══██║██║   ██║██║   ██║██╔═██╗ 
            ██║ ╚═╝ ██║██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
            ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝

                     '''+Fore.WHITE+'''MHook - Creation of Mekoih
    
    ''')
        hook.get_info()
        print(Fore.RED+f"\n GUILD ID    : {hook.guild_id}")
        print(Fore.RED+f" CHANNEL ID  : {hook.channel_id}")
        print(Fore.RED+f" USERNAME    : {hook.default_name}")
        print(Fore.RED+f" AVATAR       : {hook.default_avatar_url}")
        system("pause >nul") 
        mhook_wh()

    if opt =="2":
        system("cls")
        print(Fore.RED+'''
    
            ███╗   ███╗██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
            ████╗ ████║██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
            ██╔████╔██║███████║██║   ██║██║   ██║█████╔╝ 
            ██║╚██╔╝██║██╔══██║██║   ██║██║   ██║██╔═██╗ 
            ██║ ╚═╝ ██║██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
            ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝

                     '''+Fore.WHITE+'''MHook - Creation of Mekoih
    
    ''')
        msg = input(Fore.RED+"Message : "+Fore.WHITE)
        system("cls")
        print(Fore.RED+'''
    
            ███╗   ███╗██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
            ████╗ ████║██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
            ██╔████╔██║███████║██║   ██║██║   ██║█████╔╝ 
            ██║╚██╔╝██║██╔══██║██║   ██║██║   ██║██╔═██╗ 
            ██║ ╚═╝ ██║██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
            ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝

                     '''+Fore.WHITE+'''MHook - Creation of Mekoih
    
    ''')
        loop = True
        print(Fore.LIGHTRED_EX+' Press "S" to stop ')
        while True:
            if keyboard.is_pressed('s'):
                break
                mhook_wh() 
            hook.send(msg)
            print(Fore.RED+"[+] Send Message")
            if keyboard.is_pressed('s'):
                break
                mhook_wh() 
    if opt =="3":
        system("cls")
        print(Fore.RED+'''
    
            ███╗   ███╗██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
            ████╗ ████║██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
            ██╔████╔██║███████║██║   ██║██║   ██║█████╔╝ 
            ██║╚██╔╝██║██╔══██║██║   ██║██║   ██║██╔═██╗ 
            ██║ ╚═╝ ██║██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
            ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝

                     '''+Fore.WHITE+'''MHook - Creation of Mekoih
    
    ''')
        title = input(Fore.RED+"Embed Title : "+Fore.WHITE)
        n_field = input(Fore.RED+"Field Title : "+Fore.WHITE)
        v_field = input(Fore.RED+"Field Value : "+Fore.WHITE)
        system("cls")
        print(Fore.RED+'''
    
            ███╗   ███╗██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
            ████╗ ████║██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
            ██╔████╔██║███████║██║   ██║██║   ██║█████╔╝ 
            ██║╚██╔╝██║██╔══██║██║   ██║██║   ██║██╔═██╗ 
            ██║ ╚═╝ ██║██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
            ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝

                     '''+Fore.WHITE+'''MHook - Creation of Mekoih
    
    ''')
        print(Fore.LIGHTRED_EX+' Press "S" to stop ')
        while True: 
            if keyboard.is_pressed('s'):
                break
                mhook_wh() 
            embed = Embed(
            description=title,
            color=0x5CDBF0,
            timestamp='now'  # sets the timestamp to current time
            )
            embed.add_field(name=n_field, value=v_field)
            hook.send(embed=embed)
            print(Fore.WHITE+"[+] Embed Send (stop with enter)")
            if keyboard.is_pressed('enter'):
                break
                mhook_wh() 
    if opt=="4":
        system("cls")
        print(Fore.RED+'''
    
            ███╗   ███╗██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
            ████╗ ████║██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
            ██╔████╔██║███████║██║   ██║██║   ██║█████╔╝ 
            ██║╚██╔╝██║██╔══██║██║   ██║██║   ██║██╔═██╗ 
            ██║ ╚═╝ ██║██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
            ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝

                     '''+Fore.WHITE+'''MHook - Creation of Mekoih
    
    ''')
        n_n = input(Fore.RED+"New Name : "+Fore.WHITE)
        hook.modify(name=n_n)
        print(Fore.WHITE+"Name Modificated!")
        tm.sleep(2)
        mhook_wh()
    if opt=="5":
        system("cls")
        print(Fore.RED+'''
    
            ███╗   ███╗██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
            ████╗ ████║██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
            ██╔████╔██║███████║██║   ██║██║   ██║█████╔╝ 
            ██║╚██╔╝██║██╔══██║██║   ██║██║   ██║██╔═██╗ 
            ██║ ╚═╝ ██║██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
            ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝

                     '''+Fore.WHITE+'''MHook - Creation of Mekoih
    
    ''')
        hook.delete()
        print(Fore.WHITE+"Webhook Removed!")
        tm.sleep(2)
        mhook_wh()
    if opt=="x" or "exit":
        system("cls")
        print(Fore.RED+'''
    
            ███╗   ███╗██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
            ████╗ ████║██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
            ██╔████╔██║███████║██║   ██║██║   ██║█████╔╝ 
            ██║╚██╔╝██║██╔══██║██║   ██║██║   ██║██╔═██╗ 
            ██║ ╚═╝ ██║██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
            ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝

                     '''+Fore.WHITE+'''MHook - Creation of Mekoih
    
    ''')
        exit

def u_log():
    u = input(Fore.RED+"[-] Username: "+Fore.WHITE)
    if u == "mekoih":
        p_log()
    else:
        u_log()
def p_log():
    p = input(Fore.RED+"[-] Password: "+Fore.WHITE)
    if p == "mekoihook":
        mhook_wh()
    else:
        tm.sleep(1)
        u_log

system("cls")
print()
print(Fore.RED+'''
    
            ███╗   ███╗██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
            ████╗ ████║██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
            ██╔████╔██║███████║██║   ██║██║   ██║█████╔╝ 
            ██║╚██╔╝██║██╔══██║██║   ██║██║   ██║██╔═██╗ 
            ██║ ╚═╝ ██║██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
            ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝

                     '''+Fore.WHITE+'''MHook - Creation of Mekoih
    
    ''')
u_log()


        
