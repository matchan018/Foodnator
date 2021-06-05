# -*- coding: utf-8 -*-
import math
import numpy as np

iarray_A = []
que_list = []
weight_list = []
Q_weight = []
A_list=[]
question = []

while True:
    route = []

    with open("list1.txt",'r') as f:
        iarray_A = f.read().splitlines()
    with open("list2.txt",'r') as f:
        que_list = f.read().splitlines()
    with open("list3.txt",'r') as f:
        weight_list = f.read().splitlines()
    with open("question.txt",'r') as f:
        question = f.read().splitlines()
    
    #print(iarray_A)
    #print(que_list)
    #print(weight_list)
    #print(question)
    
    listcount = sum([1 for _ in open('list1.txt')])
    #print("listcount",listcount)
    kaiso = int(math.log2(listcount+1) - 1)

    count = 0
    print("はい...y/いいえ...nで答えてください")
    
    for i in range(kaiso):
        if que_list[count*2 + 1] == "null":break
        print(que_list[count])
        ans = input()
        weight=weight_list[count].split()
        Y=[(1,int(weight[0])),(2,int(weight[1]))]
        N=[(1,int(weight[2])),(2,int(weight[3]))]
        if ans == "y":
            a,w = zip(*Y)
            w2=np.array(w)/sum(w)
            v=np.random.choice(a,p=w2)
            count = count*2 + v
            A_list.append(0)
        elif ans == "n":
            a,w = zip(*N)
            w2=np.array(w)/sum(w)
            v=np.random.choice(a,p=w2)
            count = count*2 + v
            A_list.append(1)
        if count != 0:route.append(count)
        
    print(que_list[count])
        
    print("この料理はどうですか？これにする！...y/気分に合わない...n")
    value = input()
    
    if value == "y":
        rev = count
        for i in range(len(A_list)):
            YNcheck=(rev+1)%2
            rev = (rev+1)//2-1
            #print(rev)
            select = YNcheck+A_list[len(A_list)-i-1]*2
            #print(select)
            Q_weight=weight_list[rev].split()
            Q_weight[select]=int(Q_weight[select])+1
            weight_list[rev]=' '.join(map(str,Q_weight))
        
    elif value == "n":
        print("料理リスト")
        for i in range(listcount):
            #print(listcount)
            t = str(i)
            if que_list[i] != "null" and t not in question :print(iarray_A[i],que_list[i])
        print("あなたが今食べたい料理がリストにありますか？はい...y/いいえ...n")
        value = input()
        if value == "y":
            print("その料理の番号を入力してください") 
            number = int(input())
            rev1 = count
            rev2 = number
            for i in range(len(A_list)):
                #YNcheck1=(rev1+1)%2
                YNcheck2=(rev2+1)%2
                rev1 = (rev1+1)//2-1
                rev2 = (rev2+1)//2-1
                if rev1==rev2:
                    select = YNcheck2+A_list[len(A_list)-i-1]*2
                    #print(select)
                    Q_weight=weight_list[rev2].split()
                    Q_weight[select]=int(Q_weight[select])+1
                    weight_list[rev2]=' '.join(map(str,Q_weight))
                        
            
            
        elif value == "n":
            print("今他に食べたい料理はありますか？はい...y/いいえ...n")
            other = input()
            if other == "y":
                print("食べたい料理を教えてください")
                tabetai = input()
                print("あなたの今の気分を教えてください")
                newque = input()
                if count < 2 ** (kaiso + 1) - 1:
                    for i in range(2 ** (kaiso + 2) - 1-(2 ** (kaiso + 1) - 1)):
                        iarray_A.append(listcount)
                        listcount = listcount + 1
                        que_list.append("null")
                        weight_list.append("1 1 1 1")
                    kaiso = kaiso + 1
                    que_list[(count*2)+1] = tabetai
                    que_list[(count*2)+2] = que_list[count]
                    que_list[count] = newque
                    question.append(count)

    arr1 = iarray_A
    arr1 = [str(i) for i in arr1]
    arr4 = question
    arr4 = [str(i) for i in arr4]
    str_1 = '\n'.join(arr1)
    with open("list1.txt",'wt') as f:
        f.write(str_1)

    str_2 = '\n'.join(que_list)
    with open("list2.txt",'wt') as f:
        f.write(str_2)
    
    str_3 = '\n'.join(weight_list)
    with open("list3.txt",'wt') as f:
        f.write(str_3)
        
    str_5 = '\n'.join(arr4)
    with open("question.txt",'wt') as f:
        f.write(str_5)
    
    #print(weight_list)
    #print(question)
    #print(route)
    print("ご利用ありがとうございました。")
    print("続けますか？YES...y/NO...n")
    con = input()
    if con == "n":break


 
