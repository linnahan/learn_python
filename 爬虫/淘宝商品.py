import requests,re,json

cookies = {
  "cna": "Ii7RG1AAX2oCAXFadFMYjehu",
  "xlly_s": "1",
  "_samesite_flag_": "true",
  "cookie2": "13bae64c6787c127e57ee28a49366b03",
  "t": "3dbaf3268898272b49fbdc1cd7d149f1",
  "_tb_token_": "36be7e815ee91",
  "_m_h5_tk": "d2131c023b2070ce79316cdaa5316e00_1677659374204",
  "_m_h5_tk_enc": "2b4447f59f16951ba45d8c140aef0149",
  "sgcookie": "E100pCqwkrxjY65LfsPN9nl0vKLO37+EYME0KRxYwNdm6J8+an0OAR8foMQgLqCxZu6PfkLH3s92bZwyZEhEHxMd2IfxawRJsIWVBg6KUoAEpUk=",
  "unb": "4246050204",
  "uc3": "id2=Vy68BtSVapB1mg==&vt3=F8dCsfbfGmQJzEBYXl8=&nk2=D8roKFvvlSEUBXVW&lg2=UtASsssmOIJ0bQ==",
  "csg": "966e35c7",
  "lgc": "linnahan2018",
  "cancelledSubSites": "empty",
  "cookie17": "Vy68BtSVapB1mg==",
  "dnk": "linnahan2018",
  "skt": "6dcf2d227f512d86",
  "existShop": "MTY3NzY1MDc3NA==",
  "uc4": "id4=0@VXkbmgRhdcSN/xX0mD7CkJTr/HLE&nk4=0@DenSP6IYZrmLfhfq3c34P58HbDAdUlE=",
  "tracknick": "linnahan2018",
  "_cc_": "W5iHLLyFfA==",
  "_l_g_": "Ug==",
  "sg": "840",
  "_nk_": "linnahan2018",
  "cookie1": "AVSwmg+eydbFGtnb2e0Cd0hNuzryEI7tVKsgUx5qY+o=",
  "mt": "ci=3_1",
  "thw": "cn",
  "uc1": "cookie14=UoezSHF11ppe+w==&cookie21=VFC/uZ9aiKCaj7AzMHh1&existShop=false&cookie16=V32FPkk/xXMk5UvIbNtImtMfJQ==&cookie15=UtASsssmOIJ0bQ==&pas=0",
  "tfstk": "cZD1B2itqNb_7FJcIPte0w_kYDefZTAQvCaEfFcM9SMyBun1im6zPkSiiw6Lwk1..",
  "l": "fBjeDVvITsvlpoVsBOfwFurza77t_IRAguPzaNbMi9fPOK1p50TVW68EFKL9CnGVF6yMJ3utY56DBeYBqCmWfdWqIosM_pDmne_7Qn5..",
  "isg": "BM_PHX_i8DhGJfT1sE_enKo2XmPZ9CMW-F4BiuHcdD5FsO-y6sR3Zu2qsuAOyPuO"
}
headers = {
"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
}


reponse = requests.get("https://s.taobao.com/search?q=小米&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.jianhua.201856-taobao-item.2&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=1&ntoffset=1&p4ppushleft=2%2C48&s=44",headers = headers,cookies = cookies)
# print(reponse.text)
print(reponse.url)
g_page_config = re.search('g_page_config = ({.*?});',reponse.text).group(1)
g_page_config = json.loads(g_page_config)
auctions = g_page_config['mods']['itemlist']['data']['auctions']
for i in auctions:
    print(i.get('raw_title') + i.get('view_price')+ i.get('item_loc')+ i.get('view_sales')+ i.get('shopName'))

