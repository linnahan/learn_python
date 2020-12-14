#DOM vs SAX

'''操作XML有两种方法：DOM和SAX。DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，
优点是可以任意遍历树的节点。SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。
在Python中使用SAX解析XML非常简洁，通常我们关心的事件是start_element，end_element和char_data，
准备好这3个函数，然后就可以解析xml了。'''

from xml.parsers.expat import ParserCreate
#利用SAX解析XML文档牵涉到两个部分: 解析器和事件处理器
#解析器负责读取XML文档，并向事件处理器发送事件，如元素开始跟元素结束事件。
#而事件处理器则负责对事件作出响应，对传递的XML数据进行处理
from cgitb import text
from ctypes.test.test_pickling import name
from attr._make import attrs

class DefaultSaxHandler(object):
    def start_element(self,name,attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))
        #name表示节点名称，attrs表示节点属性（字典）
    
    def end_element(self,name):
        print('sax:end_element: %s' % name)
    
    def char_data(self,text):
        print('sax:char_data: %s' % text)
        #text表示节点数据
xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

#处理器实例
handler = DefaultSaxHandler()
#解析器实例
parser = ParserCreate()
#下面3为解析器设置自定义的回调函数
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
#开始解析XML
parser.Parse(xml)