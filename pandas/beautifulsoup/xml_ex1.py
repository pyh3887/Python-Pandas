#XML처리 기본 모듈

import xml.etree.ElementTree as etree

xml_f = open('my.xml','r',encoding='utf-8').read()
print(xml_f , type(xml_f)) # <class 'str>
root = etree.fromstring(xml_f)
print(root)
print(root.tag) 
print(len(root)) # 하위 엘리먼트 item > 2개

print('--------------')
xmlfile = etree.parse('my.xml')
print(xmlfile)
root = xmlfile.getroot()
print(root.tag)
print(root[0].tag)
print(root[1].tag)
print(root[0][1].tag)
print(root[0][0].tag)
print(root[0][0].attrib)
print(root[0][0].attrib.keys())
print(root[0][0].attrib.get('id'))

print()
myname = root.find('item').find('name').text
mytel = root.find('item').find('tel').text
print(myname)

for child in root:
    print(child.tag)
    for child2 in child:
        print(child2.tag, ' ', child2.attrib)
        
        
print()
for e in root.iter('exam'):
    print(e.attrib)

print('-------')

children = root.findall('item')
for c in children:
    re_id = c.find('name').get('id')
    re_name = c.find('name').text
    re_tel = c.find('tel').text
    print(re_id , re_name , re_tel)

    

    
    

