import re
import os
# 73.
def write_File1_2_File2(file1,file2):

    with open(file1,'r') as r:
        with open(file2,'w') as w:
            w.write(r.read())

# 74.

def getNum(file):
    # os.makedirs("ResultInts.txt")
    resNum = []
    with open(file,'r') as f:
        f1 = f.read()
        nums = re.findall(r"\d\d*",f1)
        for i in nums:
            num = int(i)
            checkNum = list(i)
            flag = False
            j = 1

            while(j<len(checkNum)):
                flag = False
                # print(checkNum[j])
                if((int(checkNum[j]))%2==1):flag=True
                j = j + 2
            if(flag):resNum.append(num)
        print(resNum)
    with open("ResultInts.txt",'w') as f2:
        k = 1
        for i in resNum:
            x = '%8d'%(i)
            f2.write(x)
            if k == 3:
                f2.write('\n')
                k = 1
            k = k+1
            # print(num)


#75.
def getStudentInfo(data):
    info_all = []
    id = []
    name = []
    grade = []
    with open(data,'r') as d:
        flag = True
        while(flag):
            info = d.readline()
            if info == "":
                flag = False
            else:
                info = info.strip('\n')
                temp = info.split(' ')
                id.append(int(temp[0]))
                name.append(temp[1])
                grade.append(int(temp[2]))
                s = dict(zip(["id","name","grade"],[int(temp[0]),temp[1],int(temp[2])]))
                info_all.append(s)

    # print(info_all)
    for i in range(len(info_all)):
        print('{:<10}{:<15s}{:>5}'.format(info_all[i]["id"], info_all[i]["name"], info_all[i]["grade"]))
        # print('{:<10}{:<15s}{:>5}'.format(id[i],name[i],grade[i]))

    #排序
    info_all = sorted(info_all,key=lambda keys:keys["id"],reverse=False)
    for i in range(len(info_all)):
        print('{:<10}{:<15s}{:>5}'.format(info_all[i]["id"], info_all[i]["name"], info_all[i]["grade"]))

    s1 = int(input())
    info_all = list(filter(lambda key:key["id"]>s1,info_all))
    for i in range(len(info_all)):
        print('{:<10}{:<15s}{:>5}'.format(info_all[i]["id"], info_all[i]["name"], info_all[i]["grade"]))



if __name__ == '__main__':
    file1 = "cat1.txt"
    file2 = "cat2.txt"
    # write_File1_2_File2(file1,file2)

    data = "student_data.txt"
    # getStudentInfo(data)

    getNum("strInts.txt")

