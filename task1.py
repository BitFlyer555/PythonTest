'''输入
按照题目要求
输入应该为不带引号的字符串
'''
source=input()
target=input()
'''建立source列表字典
key为字符
value为一个list，里面记录了该字符所在的所有位置
'''
chardic={}
for index, i in enumerate(source):
    if i in chardic.keys():
        chardic[i].append(index)
    else:
        chardic[i]=[index]
'''在target里匹配子串
分为子串第一个字符和普通字符
子串第一个字符只需要匹配到原串中第一次出现的位置
若子串第一个字符无法匹配，则整个匹配失败
若子串第一个字符可以匹配，则判断下一个字符是否存在
    在判断第n+1个字符时，需要保证该字符在原串中位置晚于第n个字符使用的位置
    即第一个字符位置在3，第二个需大于3，例如在5
    第三个需要大于5
    所以此处需要一个位置指针flag来保证子串的前后顺序
'''
count = 0 #构成子串数量
location = 0 #target的匹配进度
balabala = 1 #匹配成功标志
while location<len(target):
    if target[location] in chardic.keys():#第一字符可以匹配
        flag=chardic[target[location]][0]#flag移动到第一字符在原串的最早位置
        location+=1
        while(location<len(target)):
            if target[location] in chardic.keys():#若第n+1字符在原串中有
                enable = 0#记录是否存在n字符后面的n+1字符
                for i in chardic[target[location]]:
                    if i > flag:#若有，flag移动到新的位置
                        flag=i
                        enable=1
                        location+=1
                        break
                if enable==0:
                    break # 第n+1个字符不再n的后面
            else: break  # 第n+1个字符不存在
        count+=1
    else:#第一字符不匹配，匹配失败
        print(-1)
        balabala=0
        break
if balabala==1:
    print(count)
