# 주어진 데이터 target이 어디에 저장되어 있는지 index를 반환
def getIndex(num_list, target):
    for i in range(len(num_list)):
        if num_list[i] == target:
            return i
    #없으면 -1반환
    return -1

# 리스트에 저장된 숫자 중 가장 큰 숫자 반환
def getMax(num_list):
    if not num_list:
        return -1
    max = 0
    for num in num_list:
        if max < num: max = num
    return max

# 리스트에 저장된 숫자 중 가장 작은 숫자 반환
def getMin(num_list):
    if not num_list:
        return -1
    min = num_list[0]
    for num in num_list:
        if min > num: min = num
    return min

#  리스트에 저장된 숫자 중 입력된 숫자 target보다 큰 수가 몇 개 있는지 구하여 반환
def countGT(num_list, target):
    count = 0
    for num in num_list:
        if target < num:
            count += 1
    return count

# 정수형 배열에 저장된 모든 값 더하여 반환
def sumList(num_list):
    sum = 0
    for num in num_list:
        sum += num
    return sum

# 배열에 저장된 숫자를 역순으로 저장
def swapList(numList):
    for i in range(len(numList)//2):
        numList[i],numList[-(i+1)] = numList[-(i+1)], numList[i]


number_list = [23, 45, 27, 11, 25, 65, 78]

print(getIndex(number_list, 25))
print(getMax(number_list))
print(getMin(number_list))
print(countGT(number_list, 42))
print(sumList(number_list))
swapList(number_list)
print(number_list)