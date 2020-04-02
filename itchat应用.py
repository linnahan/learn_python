import itchat,time

def login_call():
    print('成功登陆')
def exit_call():
    print('退出')

@itchat.msg_register(itchat.content.TEXT,isFriendChat=True)
def simple_reply(msg):
    itchat.send_msg(msg['Text'],toUserName=msg['FromUserName'])
    #print(msg)
itchat.auto_login(loginCallback=login_call,exitCallback=exit_call,hotReload=True)
itchat.run()
#itchat.search_friends(name='罗密欧与猪过夜')
#print(result)