#获得数据
def getNum():
    nums = []
    num = input('请输入数字(回车退出)：')
    while num != '':
        nums.append(eval(num))
        num = input('请输入数字（回车退出）：')
    return nums
#平均值
def mean(nums):
    s = 0
    for num in nums:
        s += num        #累加求和
    return s / len(nums)
#方差
def dev(nums,mean):
    sdev = 0
    for num in nums:
        sdev += (num - mean)**2   #差的平方和
    return pow(sdev / (len(nums)-1),0.5)
#中位数
def median(nums):
    nums.sort()
    size = len(nums)
    if size % 2 == 0:
        med = (nums[size//2-1]+nums[size/2])/2
    else:
        med = nums[size//2]
    return med


def main():
    n = getNum()
    m = mean(n)
    print('平均值：{:.2f}，中位数：{}，方差：{:.2f}'.format(m,median(n),dev(n,m)))

if __name__ == '__main__':
    main()