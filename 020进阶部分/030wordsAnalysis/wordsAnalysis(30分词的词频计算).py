# 1.3 基本单词列表词频计算
fileFullPath = './pythonStudy/020进阶部分/030wordsAnalysis/wordsAnalysis.txt'
wordsProcessed = []
wordsUnique = []
wordsCount = {}
with open(fileFullPath,'r',encoding='UTF-8') as fileObject:
        contents = fileObject.read()
        words = contents.split()
        for word in words:
                wordProcessed = word.strip()
                wordProcessed = wordProcessed.replace('.','')
                wordProcessed = wordProcessed.replace(',','')
                wordProcessed = wordProcessed.replace('"','')
                wordProcessed = wordProcessed.replace(':','')
                wordProcessed = wordProcessed.replace('”','')
                wordProcessed = wordProcessed.replace('“','')
                wordProcessed = wordProcessed.replace('?','')
                wordProcessed = wordProcessed.replace(';','')
                wordProcessed = wordProcessed.lower()
                # wordProcessed = word.strip().replace('.','').replace(',','').replace('"','').replace(':','').replace('”','').replace('“','').replace('?','').replace(';','').lower()
                wordsProcessed.append(wordProcessed)
for wordProcessed in wordsProcessed:
        if wordProcessed not in wordsUnique:
                wordsUnique.append(wordProcessed)
for wordUnique in wordsUnique:
        wordCount = wordsProcessed.count(wordUnique)
        wordsCount[wordUnique] = wordCount
# for word,count in wordsCount.items():
# 如果写作key=lambda item:item[0]的话则是选取第一个元素作为比较对象
# 也就是key值作为比较对象。lambda x:y中x表示输出参数，y表示lambda 函数的返回值
for word,count in sorted(wordsCount.items(),key = lambda item:item[1]):
        print('单词"{0}"出现在文章中的次数为{1}次。'.format(word,str(count)))

print(len(wordsProcessed))
print(len(wordsUnique))