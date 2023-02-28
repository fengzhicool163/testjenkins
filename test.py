print("hello python")
import re
#提取出python
# key = "javapythonc++php"
# str = re.findall('python',key)[0]
# print(str)

# key="<html><h1>hello world<h1></html>"
# str = re.findall('<h1>(.*)<h1>',key)
# print(str)
# key ='<section class="note-item" like-points="[object Object]" note-points="[object Object]" track-data="[object Object]" data-v-edde9d4c="" data-v-6fd32383-s="" style="transform: translate(0px, 0px); --5051610a:216px;"><a href="/explore/63bd5cad0000000019023133" class="cover ld" data-v-edde9d4c="" style="height: 162px; background: url(&quot;https://sns-img-hw.xhscdn.com/7ce53b57-06f3-a6af-1b77-a3bdea08995d?imageView2/2/w/648/format/webp&quot;) left top 100% / 100% no-repeat;"><!----></a><div class="footer" data-v-edde9d4c=""><a href="/explore/63bd5cad0000000019023133" class="title" data-v-edde9d4c=""><span data-v-7daa87a8="" data-v-edde9d4c="">耶梅拉打卡第一天 </span></a><div class="author-wrapper" data-v-edde9d4c=""><a href="/user/profile/60ca79c90000000001006897" class="author" target="_blank" data-v-edde9d4c=""><img class="author-avatar" src="https://sns-avatar-qc.xhscdn.com/avatar/61ec154df7046540ae0e034e.jpg?imageView2/2/w/60/format/webp" data-v-edde9d4c=""><span class="name" data-v-edde9d4c="">pooh</span></a><span class="like-wrapper" data-v-106bfd91="" data-v-edde9d4c=""><span class="like-lottie" data-v-106bfd91="" style="width: 16px; height: 16px;"></span><svg class="reds-icon like-icon" width="16" height="16" data-v-0800f4d4="" data-v-106bfd91=""><use xlink:href="#like" data-v-0800f4d4=""></use></svg><span class="count" data-v-106bfd91="">100+</span></span></div></div></section>'
# ex='background: url\(.*\)'
# str = re.findall(ex , key,re.S)
# print(str)

# from bs4 import BeautifulSoup
# fp = open("./sogou.html",'r',encoding='utf-8')
# soup = BeautifulSoup(fp,'lxml')
#print(soup.find('div',attrs={'class':'top-nav'}))
# print(soup.select('.top-nav > ul > li  a')[0]['href'])

# from lxml import etree
# # 实例化etree对象，且
# tree = etree.parse('sogou.html')
# print(tree)

import sys
print(sys.path)




