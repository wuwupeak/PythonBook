def fileRead(fileName): 
    '''
    本函数将打开与本文件同一文件夹路径下的文件进行读取
    传入参数为文件的全名[string]
    传出参数为读取的文件内容[string]
    '''
    import os
    fileFolderDir = os.path.dirname(__file__) #使用os模块的函数拿到正在当前文件所在文件夹的绝对路径
    fileFullPath = fileFolderDir + fileName #使用字符串拼接，得到需要打开文件的绝对路径
    with open(fileFullPath,encoding = 'utf-8') as fileObject: #使用绝对路径打开文件，并将文件作为一个对象fileObject
        fileContent = fileObject.read() #读取文件对象的内容，并赋值给变量fileContent
    return fileContent

def fileClean(fileContent):
    '''
    本函数将读取的文件内容形成清洗后的单词列表
    传入参数为读取的文件内容[string]
    传出的内容为单词列表[list]
    '''
    #将标点符号替换为空格
    fileContent = fileContent.replace('?',' ')
    fileContent = fileContent.replace(';',' ')
    fileContent = fileContent.replace('.',' ')
    fileContent = fileContent.replace(',',' ')
    fileContent = fileContent.replace(':',' ')
    fileContent = fileContent.replace('"',' ')
    fileContent = fileContent.replace("'",' ')
    fileContent = fileContent.replace('(',' ')
    fileContent = fileContent.replace(')',' ')
    fileContent = fileContent.replace("’",' ')
    fileContent = fileContent.replace("“",' ')
    fileContent = fileContent.replace("”",' ')
    wordsCleaned = fileContent.lower().split() #split方法使用空格作为分隔符将字符串fileContent拆分成列表
    for word in wordsCleaned:
        if len(word) == 1 and word != "i": #去除单词长度为1，且不是大写I的单词
            wordsCleaned.remove(word)
    return wordsCleaned

def fileWordsUnique(wordsCleaned):
    '''
    本函数将从单词列表获得单词列表中出现的单词
    传入参数为读取的单词列表[list]
    传出的内容为单词列表中出现的不重复单词列表[list]
    '''
    #第一代获取不重复单词列表的处理代码
    wordsUnique = [] #初始化空列表wordsUnique，用于存储words列表中出现的不重复单词
    for word in wordsCleaned:
        if wordsUnique.count(word) == 0: #如果在wordsUnique列表中找不到单词word就加入该列表
            wordsUnique.append(word)

    # #第二代获取不重复单词列表的处理代码
    # wordsUniqueSet = set(wordsCleaned)
    # wordsUnique = list(wordsUniqueSet)
    return wordsUnique

def fileWordsCount(wordsCleaned,wordsUnique):
    '''
    本函数将单词列表中的单词进行计数
    传入参数为读取的单词列表wordsCleaned[list]，不重复单词列表wordsUnique[list]
    传出的内容为单词及计数的字典[dict]
    '''
    wordsCount = {}
    for word in wordsUnique:
        wordsCount[word] = wordsCleaned.count(word) #将words列表中出现word的次数作为值，word作为键加入字典wordsCount
    wordsCountOrder = sorted(wordsCount.items(),key = lambda item:item[1]) #对字典的value进行排序
    wordsCountDict = dict(wordsCountOrder) #将元祖转换为字典
    return wordsCountDict

def fileWordsCountAll(fileName):
    fileContent = fileRead(fileName)
    wordsCleaned = fileClean(fileContent)
    wordsUnique = fileWordsUnique(wordsCleaned)
    wordsCountDict = fileWordsCount(wordsCleaned,wordsUnique)
    return wordsCountDict