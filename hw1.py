def getResult():
    alphabet1:List[List[chr]] = [['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
                                ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
                                ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';'],
                                ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/']]
    
    alphabet2:List[List[chr]] = [['!', '@', '#', '$', '%', '^', '&', '*', '(', ')'],
                                ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
                                ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':'],
                                ['Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?']]
    #分開兩個陣列的原因為有些按鍵會有兩種符號，第一個陣列為下排，第二個陣列為上排

    n=int(input())
    #n表示要輸入幾組資料
    repeat=set()
    #此集合是為避免判定不是兩種符號的按鍵時，輸出兩次相同結果
    for i in range(n):
        value,direction=input().split()
        #輸入按鍵,並判斷方向
        direction=int(direction)
        for j in range(len(alphabet1)):
            if value in alphabet1[j]:
                k= alphabet1[j].index(value)
        #判斷value在陣列的位子
                if direction==1:
                    ans=(alphabet1[j-1][k])
                elif direction==2:
                    ans=(alphabet1[j+1][k])
                elif direction==3:
                    ans=(alphabet1[j][k+1])
                elif direction==4:
                    ans=(alphabet1[j][k-1])
                #依照direction的數字來輸出對應方向的按鍵
                print(ans)
                repeat.add(ans)
                #將輸出的值加入集合，避免下一個判定重複輸出
        for j in range(len(alphabet2)):
            if value in alphabet2[j]:
                k= alphabet2[j].index(value)
        #第二次判定，判斷第二個陣列
                if direction==1:
                    ans=(alphabet1[j-1][k])
                elif direction==2:
                    ans=(alphabet1[j+1][k])
                elif direction==3:
                    ans=(alphabet1[j][k+1])
                elif direction==4:
                    ans=(alphabet1[j][k-1])
                if ans not in repeat:
                    print(ans)
                #依照direction的數字來輸出對應方向的按鍵(最後的if判斷第一個陣列是否已經輸出過相同符號)

getResult()