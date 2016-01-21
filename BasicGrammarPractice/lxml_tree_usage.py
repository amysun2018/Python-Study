'''
Created on 2013-11-13

@author: yannpxia
'''
from xml.etree import ElementTree as ET

'''make the string as file input'''
from StringIO import StringIO

# filename = 'C:\Users\yannpxia\Desktop\NS710000.XML'
# 
# content_string='''<?xml version="1.0" encoding="UTF-8"?>
# <OMeS version="2.3" adapId="com.nsn.nx" adapRelease="com.nsn.ns.ns10"><PMSetup startTime="2013-11-04T06:28:35.980+02:00:00" interval="1440"><PMMOResult><MO dimension="network"><DN>FLEXINS-123456/MCC-262/MNC-1/TA-1</DN></MO><PMTarget measurementType="UTLM"><M71C000>0</M71C000><M71C001>2</M71C001><M71C002>4</M71C002><M71C003>4</M71C003><M71C004>0</M71C004><M71C005>2</M71C005><M71C006>4</M71C006><M71C007>4</M71C007></PMTarget></PMMOResult><PMMOResult><MO dimension="network"><DN>FLEXINS-123456/MCC-262/MNC-1/TA-2</DN></MO><PMTarget measurementType="UTLM"><M71C000>0</M71C000><M71C001>1</M71C001><M71C002>2</M71C002><M71C003>3</M71C003><M71C004>0</M71C004><M71C005>1</M71C005><M71C006>1</M71C006><M71C007>3</M71C007></PMTarget></PMMOResult></PMSetup></OMeS>
# '''
# tree = ET.parse(StringIO(content_string))
# 
# for pmmo_result in tree.iter('PMMOResult'):
#     dn = 0
#     for item in pmmo_result:
#         for i in item :
#             print "-------------------"
#             if i.text == 'FLEXINS-123456/MCC-262/MNC-1/TA-2':
#                 dn=1
#                 print i.text
#             if dn==1:
#                 print i.text, i.tag
# 
# 
# tree = ET.parse(filename)
# root = tree.getroot()
# a =  root.find("PMSetup")
# print a.tag
# print a.attrib['startTime']


content_string = '''<?xml version="1.0" encoding="UTF-8"?>
<OMeS version="2.3" adapId="com.nsn.nx" adapRelease="com.nsn.ns.ns10"><PMSetup startTime="2013-12-05T08:26:40.900+02:00:00" interval="1440"><PMMOResult><MO dimension="network"><DN>FLEXINS-123456/MCC-262/MNC-1/TA-1</DN></MO><PMTarget measurementType="Mobility_Management"><M50C000>1</M50C000><M50C001>0</M50C001><M50C002>1</M50C002><M50C003>0</M50C003><M50C004>0</M50C004><M50C005>0</M50C005><M50C006>0</M50C006><M50C007>0</M50C007><M50C008>0</M50C008><M50C009>0</M50C009><M50C010>0</M50C010><M50C011>0</M50C011><M50C012>0</M50C012><M50C013>0</M50C013><M50C014>0</M50C014><M50C015>0</M50C015><M50C016>0</M50C016><M50C017>0</M50C017><M50C018>0</M50C018><M50C019>0</M50C019><M50C020>0</M50C020><M50C021>0</M50C021><M50C022>0</M50C022><M50C023>0</M50C023><M50C024>0</M50C024><M50C025>0</M50C025><M50C026>0</M50C026><M50C027>0</M50C027><M50C028>0</M50C028><M50C029>0</M50C029><M50C030>0</M50C030><M50C031>0</M50C031><M50C032>0</M50C032><M50C033>0</M50C033><M50C034>0</M50C034><M50C035>0</M50C035><M50C036>0</M50C036><M50C037>0</M50C037><M50C038>0</M50C038><M50C039>0</M50C039><M50C040>0</M50C040><M50C041>0</M50C041><M50C042>0</M50C042><M50C043>0</M50C043><M50C044>0</M50C044><M50C045>0</M50C045><M50C046>0</M50C046><M50C047>0</M50C047><M50C048>0</M50C048><M50C049>0</M50C049><M50C050>0</M50C050><M50C051>0</M50C051><M50C052>0</M50C052><M50C053>0</M50C053><M50C054>0</M50C054><M50C055>0</M50C055><M50C056>0</M50C056><M50C057>0</M50C057><M50C058>0</M50C058><M50C059>0</M50C059><M50C060>0</M50C060><M50C061>0</M50C061><M50C062>0</M50C062><M50C063>0</M50C063><M50C064>0</M50C064><M50C065>0</M50C065><M50C066>0</M50C066><M50C067>0</M50C067><M50C068>0</M50C068><M50C069>0</M50C069><M50C070>0</M50C070><M50C071>0</M50C071><M50C072>0</M50C072><M50C073>0</M50C073><M50C074>0</M50C074><M50C075>0</M50C075><M50C076>0</M50C076><M50C077>0</M50C077><M50C078>0</M50C078><M50C079>0</M50C079><M50C080>0</M50C080><M50C081>0</M50C081><M50C082>0</M50C082><M50C083>0</M50C083><M50C084>0</M50C084><M50C085>0</M50C085><M50C086>0</M50C086><M50C087>0</M50C087><M50C088>0</M50C088><M50C089>0</M50C089><M50C090>0</M50C090><M50C091>0</M50C091><M50C092>0</M50C092><M50C093>0</M50C093><M50C094>0</M50C094><M50C095>0</M50C095><M50C096>0</M50C096><M50C097>0</M50C097><M50C098>0</M50C098><M50C099>0</M50C099><M50C100>0</M50C100><M50C101>0</M50C101><M50C102>0</M50C102><M50C103>0</M50C103><M50C104>0</M50C104><M50C105>0</M50C105><M50C106>0</M50C106><M50C107>0</M50C107><M50C108>0</M50C108><M50C109>0</M50C109><M50C110>0</M50C110><M50C111>0</M50C111><M50C112>0</M50C112><M50C113>0</M50C113><M50C114>0</M50C114><M50C115>0</M50C115><M50C116>0</M50C116><M50C117>0</M50C117><M50C118>0</M50C118><M50C119>0</M50C119><M50C120>0</M50C120><M50C121>0</M50C121><M50C122>0</M50C122><M50C123>0</M50C123><M50C124>0</M50C124><M50C125>0</M50C125><M50C126>0</M50C126><M50C127>0</M50C127><M50C128>0</M50C128><M50C129>0</M50C129><M50C130>0</M50C130><M50C131>0</M50C131><M50C132>0</M50C132><M50C133>0</M50C133><M50C134>0</M50C134><M50C135>0</M50C135><M50C136>0</M50C136><M50C137>0</M50C137><M50C138>0</M50C138><M50C139>0</M50C139><M50C140>0</M50C140><M50C141>0</M50C141><M50C142>0</M50C142><M50C143>0</M50C143><M50C144>0</M50C144><M50C145>0</M50C145><M50C146>0</M50C146><M50C147>0</M50C147><M50C148>0</M50C148><M50C149>0</M50C149><M50C150>0</M50C150><M50C151>0</M50C151><M50C152>0</M50C152><M50C153>0</M50C153><M50C154>0</M50C154><M50C155>0</M50C155><M50C156>0</M50C156><M50C157>0</M50C157><M50C158>0</M50C158><M50C159>0</M50C159><M50C160>0</M50C160><M50C161>0</M50C161><M50C162>0</M50C162><M50C163>0</M50C163><M50C164>0</M50C164><M50C165>0</M50C165><M50C166>0</M50C166><M50C167>0</M50C167></PMTarget></PMMOResult></PMSetup></OMeS>'''
tree = ET.parse(StringIO(content_string))

for pmmo_result in tree.iter('PMMOResult'):
    dn = 0
    print pmmo_result.tag
    for item in pmmo_result:
        print item.tag
        for i in item:
            #             print "-------------------"
            if i.text == 'FLEXINS-123456/MCC-262/MNC-1/TA-1':
                dn = 1
            #                 print i.text
            if dn == 1:
                #                 yield i
                print i.text, i.tag

root = tree.getroot()
a = root.find("PMSetup")
print a.tag
print a.attrib['startTime']
