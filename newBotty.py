import telegram
import platform



def bop(bot,chatid,msg):
    # send the msg
    bot.send_message(chat_id=chatid, text=msg)

def main():
    # out bot tokken
    token = '1145900772:AAF9OtRgU9CQ2wb-Fiz2kYUhrg5Cm2xNFa0'
    # creating the bot
    bot = telegram.Bot(token=token)
    # call the function bop
    sysName = platform.system()
    bop(bot,-435312318,"Your Laptop was turned on "+ sysName)

    
if __name__ == '__main__':
    main()
