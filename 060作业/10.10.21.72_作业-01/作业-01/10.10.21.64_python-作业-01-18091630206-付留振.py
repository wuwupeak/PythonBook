


texs ='''
 'fldkkf edl dlkdl osdjos sjdlsdj skfskd dsjokdl dkwokeow owkod 
dssd wokdod wpeekp wpkdpw wpdsksdkdpw woek wokeo weoe  eoekwo fuliuzhen 
dkdjk ififi osad odoasd dspoad odasdoam odsaod doakdo dasidm kdpas'
'''
 texs = texs.replace(",","")
 texs = texs.replace('.','')
 texs = texs.replace('"',"")
 texs = texs.replace('\n',"")
 print(texs)
 liste = []
 liste = texs.split('')
 number = len(liste)
 print('这段话共有'　+ str(number) + "的单词")
 wordlist = []
 for word in wordlist:
    if word not in wordlist:
         wordlist.append(word)
 newnumber = len(wordlist)
 print('这段话共有' + str(newnumber) + '个独一无二的单词')
 for word in newwordlist:
     wordsnumber = wordlist.count(word)
    print(word + '在文章中出现的次数是：'　+ str(wordsnumber))


# book = texs.replace(',','')
# wordslist = book.split()
# sentence=len(wordslist)
# print("这段话总共有"　+ str(sentence) + '单词')
