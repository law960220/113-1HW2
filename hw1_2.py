num=input()
#依題目輸入，例:nums = [3, 0, 1]
nums=eval(num.split('=')[1].strip())
#只取數組的部分
n=len(nums)
#判斷數組長度
sum1=n*(n+1)/2
#計算0加到n的總和
sum2=sum(nums)
#計算數組內數字總和
miss=sum1-sum2
#相減來得知缺少的數字
print(int(miss))