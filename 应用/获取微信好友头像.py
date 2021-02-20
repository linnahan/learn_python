import itchat
import os



def getHeadImgs():
    itchat.auto_login()     # 通过二维码登录微信网页版
    friendList = itchat.get_friends(update=True)    # 获取微信好友信息列表
    '''这里会用到的微信好友信息如下： 
    User= {'UserName': '@........','PYQuanPin': '....','NickName': '.....'}'''
    
    # 获取用户个人昵称，用于之后文件夹命名、用户头像命名
    if friendList[0]['PYQuanPin']:  # 好友列表中第0个是自己
        user = friendList[0]['PYQuanPin']
    else:
        user = friendList[0]['NickName']

    # 存储本人头像
    selfHead = "{}/{}.jpg".format(os.getcwd(),user)
    with open(selfHead,'wb') as f:
        head = itchat.get_head_img(friendList[0]['UserName'])
        f.write(head)

    # 建个文件夹来存储好友头像
    if not os.path.exists(user):
        os.mkdir(user)
    
    os.chdir(user)  # 工作路径转到新建文件夹中
    print("开始读取%d位好友头像..."%(len(friendList)-1))
    for i in range(1,len(friendList)):
        if i % 20 ==0:  # 每读取20位好友头像打印一条信息
            print("已读取%d位好友头像，请耐心等待~"% i)
        try:    # 把第i个好友的头像、名称信息添加进friendList[i]字典中
            friendList[i]['head_img'] = itchat.get_head_img(userName=friendList[i]['UserName'])
            friendList[i]['head_img_name'] = "%s.jpg" % friendList[i]['UserName']
        except ConnectionError:
            print('Fail to get %s' % friendList[i]['UserName'])

        with open(friendList[i]['head_img_name'],'wb') as f:
            f.write(friendList[i]['head_img'])
    print("读取好友头像完毕！")

getHeadImgs()


