# 1.2 分词的基本清洗
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
print(words)
print(len(words))