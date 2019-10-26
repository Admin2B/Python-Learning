import jieba

#全模式分词
seg_list=jieba.cut('我来到北京的北京大学',cut_all=True,)
print('Full Mode:'+','.join(seg_list))
print('****************************************')
#默认是精确分词模式，适合文本分析
seg_list=jieba.cut('我来到北京的北京大学',cut_all=False,)
print('Default Mode:'+','.join(seg_list))
print('****************************************')
#适合用于搜索引擎分词
seg_list=jieba.cut_for_search('我来到北京的北京大学',HMM=False,)
print('Search Mode:'+','.join(seg_list))

print('****************************************')
#seg_list=jieba.cut('如果放到数据库中将出错')
print('原文档：\t'+'/'.join(jieba.cut('如果放到数据库中将出错')))
print(jieba.suggest_freq(('中','将'),True))
print('改进文档：\t'+'/'.join(jieba.cut('如果放到数据库中将出错')))

print('原文档：\t'+'/'.join(jieba.cut('台中正确应该不会被拆分')))
print(jieba.suggest_freq(('台中'),True))
print('改进文档：\t'+'/'.join(jieba.cut('台中正确应该不会被拆分')))
print('****************************************')
import jieba.analyse

s='此外，公司拟对全资子公司吉林欧亚置业有限公司增资4.3亿元，增资后，吉林欧亚置业注册资本由7000万元增加到5亿元。吉林欧亚置业主要经营范围为房地产开发及百货零售等业务。目前在建吉林欧亚城市商业综合体项目。2013年，实现营业收入0万元，实现净利润-139.13万元。'
for x,w in jieba.analyse.extract_tags(s,10,withWeight=True):
    print('%s%s'%(x,w))

print('****************************************')
for x,w in jieba.analyse.textrank(s,10,withWeight=True):
    print('%s%s' % (x, w))

import jieba.posseg
print('****************************************')
words=jieba.posseg.cut('我爱北京天安门')
for word,flag in words:
    print('%s%s' % (word, flag))

print('****************************************')
result=jieba.tokenize('永和服装饰品有限公司')
for tk in result:
    print('word %s\t\t start:%d\t\t end:%d'%(tk[0],tk[1],tk[2]))

print('****************************************')
result=jieba.tokenize('永和服装饰品有限公司',mode='search')
for tk in result:
    print('word %s\t\t start:%d\t\t end:%d'%(tk[0],tk[1],tk[2]))


