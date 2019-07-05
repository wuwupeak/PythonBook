# print("1" + "." + "这段话共有50个单词")
# print("2" + "." + "这段话共有")
test= """
"when the aerils are down,and you spirit is covered with snows ofcynism and the ice of pessimism,then you are grown old,even at twenty,but as long as your aerials ae up,to catch the waves of optimism,there is hope you may die young at eight"
"""
test = test.replace(",","")
test = test.replace(".","")
test = test.replace('"',"")
test = test.replace('\n',"")
print(test)
wordlist = []
wordlist = test.split(" ")
wordnumber = len(wordlist)
print("1" + "." + "这段话共有" +str(wordnumber) + "个单词")

newwordlist = []
for word in wordlist:
    if word not in newwordlist:
        newwordlist.append(word)
newwordnumber = len(newwordlist)
print("2" + "." + "这段话共有" + str(newwordnumber) + "个独一无二的单词")


for word in newwordlist:
    wordsnumber = wordlist.count
    print( word + "在文章中出现的次数是：" + str(wordnumber))

