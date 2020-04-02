import itchat,xlwt      #调用第三方库


def login_call():       #用来让我们知道登陆成功
    print('成功登陆')

itchat.auto_login(hotReload=True,loginCallback=login_call) #登陆微信
friend_data=itchat.get_friends(update=True)     #获取微信好友信息
#print(friend_data)  #可以把注释符号去掉看一下输出

'''总体来说就是这种  [{***},******] 列表里包含着很多个字典
每个好友就对应一个字典，每个字典用js格式存着各种信息'''
#'Sex','NickName','City','UserName','Signature'这是我想要的，你们也可以自己去字典找你们想用的

friend = []     #新建一个空列表
for i in range(len(friend_data)):   #循环*次，*为字典个数，也就是你好友的数量
    sex = friend_data[i].get('Sex')     #get到性别
    nickname = friend_data[i].get('NickName')   #get到昵称
    city = friend_data[i].get('City')    #get到次城市
    signature = friend_data[i].get('Signature')     #get到个性签名
    username = friend_data[i].get('UserName')
    afdata = [sex,nickname,city,signature,username]    #每次get到的都是一个好友的信息，把它们装进列表
    friend.append(afdata)   #把好友的列表信息装进上面建好的空列表
'''经过上面的for循环就把每个好友的信息装进friend中
大概是这个样子的  [[***],******]   '''

workbook = xlwt.Workbook(encoding='utf-8')  # 新建一个表格
worksheet = workbook.add_sheet('好友名单')  # 给表格新建一个名为 好友名单 的工作簿
al = xlwt.Alignment()   #对齐设置
al.horz = 0x02      #水平方向对齐
al.vert = 0x01      #垂直方向对齐
style = xlwt.XFStyle()  # 创建一个样式对象，初始化样式
style.alignment = al    #添加对齐设置
title = ['Sex','NickName','City','UserName','Signature']    #标题
for t in range(len(title)):      #循环5次，也就是标题个数
    worksheet.write(0,t,title[t],style)     #写入，参数分别为(第0行，第t列，内容，样式）
for i in range(len(friend)):    #循环n次，n个好友，一个好友写入一行
    for j in range(len(friend[i])):     #循环5次，之前代码中afdata的个数
        worksheet.write(i+1,j,friend[i][j],style)   #写入，第一行为标题，所以要i+1
workbook.save('微信好友一览表.xls')      #保存表格，参数为文件名，记得加上格式.xls哦
#到这里程序就任务就完成了-------------------------------------------
print('总共有好友%d个'%len(friend))    #用来打印好友个数（无关紧要）