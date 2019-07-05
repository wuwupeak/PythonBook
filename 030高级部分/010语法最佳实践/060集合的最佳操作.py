#1.1 Python的内置集合类型决定了哪一类集合可以作为集合的元素
#set()：一种可变的、无序的、有限的集合，其元素是唯一的、不可变的（可哈希的）对象。
#frozenset()：一种不可变的、可哈希的、无序的集合，其元素是唯一的、不可变的（可哈希的）对象。
#由于frozenset()具有不变性，它可以用作字典的键，也可以作为其他set()和frozenset()的元素。在一个set()或frozenset()中不能包含另一个普通的可变set()
nameSetOne = set(['小明','小李','小江'])
nameSetTwo = set(['小赵','小钱','小孙'])


#使用可变的set()来充当集合的不可变元素，会引发TypeError
nameSet = set([nameSetOne,nameSetTwo])

#使用不可变的frozenset()来充当集合的不可变元素
nameSetOne = frozenset(['小明','小李','小江'])
nameSetTwo = frozenset(['小赵','小钱','小孙'])
nameSet = set([nameSetOne,nameSetTwo])
print(nameSet)


#空的集合对象是没有字面值的。空的花括号{}表示的是空的字典字面值。