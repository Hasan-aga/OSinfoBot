import telegram
import platform



def bop(bot,chatid,msg):
    # send the msg
    bot.send_message(chat_id=chatid, text=msg)

def main():
    # bot tokken
    token = ''
    # group id
    groupid=
    # creating the bot
    bot = telegram.Bot(token=token)
    # get system name
    sysName = platform.system()

    bop(bot,groupid,"Your Laptop was turned on "+ sysName)

    
if __name__ == '__main__':
    main()
