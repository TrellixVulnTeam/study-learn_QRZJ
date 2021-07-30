import matplotlib.pyplot as plt
f = open('scored.txt', 'w')  # 结果输出文件
L = [['学号', '平时成绩', '期末成绩'],
     ['10153450101', '82', '78'],
     ['10153450102', '72', '71'],
     ['10153450103', '82', '32'],
     ['10153450104', '62', '72'],
     ['10153450105', '62', '70'],
     ['10153450106', '85', '90'],
     ['10153450107', '65', '69'],
     ['10153450108', '74', '50'],
     ['10153450109', '80', '28'],
     ['10153450110', '80', '60']]
l1, l2, l3, l4, l5 = 0, 0, 0, 0, 0  # 统计各分数段人数的初值
ave = 0   # 总成绩平均分初值
N = len(L)-1  # 总人数
del L[0]

for s in L:  # 遍历二维列表各行元素
    sum = 0
    '''
    要求1：请在24行填充代码，取每行第2个和第3个成绩元素，按照平时成绩*0.4+期末成绩*0.6
    计算个人成绩，赋值给sum，注意进行元素类型转换
    '''
    sum = int(s[1]) * 0.4 + int(s[2]) * 0.6
    ave += sum
    '''
    要求2：写代码，利用分支结构，对个人成绩所属分数段进行讨论，相应分数段总人数加1
    '''
    if sum >= 90:
        l1 += 1
    elif 80 <= sum < 90:
        l2 += 1
    elif 70 <= sum < 80:
        l3 += 1
    elif 60 <= sum < 70:
        l4 += 1
    else:
        l5 += 1
    f.write("%s\t%s\n" % (s[0], str(sum)))  # 将每人的学号、总成绩输出到f文件
ave /= N  # 计算平均分
print("学生总人数：", N, end='\n')
print("90分以上人数：", l1, end='\n')
print("80-89分人数：", l2, end='\n')
print("70-79分人数：", l3, end='\n')
print("60-69分人数：", l4, end='\n')
print("60分以下人数：", l5, end='\n')
print("平均分：%.2f" % ave)

x=["90分","80-90分","70-80分","60-70分"]
y=[11,12,13,14]

plt.bar(x,y)
plt.show()




