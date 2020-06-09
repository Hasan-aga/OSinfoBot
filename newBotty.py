import telegram
import platform



def bop(bot,chatid,msg):
    # send the msg
    bot.send_message(chat_id=chatid, text=msg)

def main():
    # bot tokken
    token = '1145900772:AAF9OtRgU9CQ2wb-Fiz2kYUhrg5Cm2xNFa0'
    # group id
    groupid=-435312318
    # creating the bot
    bot = telegram.Bot(token=token)
    # get system name
    sysName = platform.system()

    bop(bot,groupid,"Your Laptop was turned on "+ sysName)

    
if __name__ == '__main__':
    main()
