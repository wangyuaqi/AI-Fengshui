#三元九运速算法

#上元甲子一宫连，中元起巽下兑间；上五中二下八女，男逆女顺起根源。

#按后天八卦分九个宫：1、北宫：坎（水）；2、西南宫：坤（土）；3、东宫：震（木）；4、东南宫：巽（木）；
#5、中宫：男坤女艮（土）；6、西北宫：乾（金）；7、西宫：兑（金）；8、东北宫：艮（土）；9、南宫：离（火）

#男命
nan={0:'坎水',8:'坤土',7:'震木',6:'巽木',5:'坤土',4:'乾金',3:'兑金',2:'艮土',1:'离火'}
#女命
nv={5:'坎水',6:'坤土',7:'震木',8:'巽木',0:'艮土',1:'乾金',2:'兑金',3:'艮土',4:'离火'}

#1900年男命是坎水年，女命是艮土年，用本年或者出生年减去1864年，除以9，余数对应的上表就是年命。

print('请输入年份')
year=int(input())

a=year-1900

b=a%9

c=nan[b]
d=nv[b]

print(str(year)+'年男命为'+c+'，女命为'+d)
