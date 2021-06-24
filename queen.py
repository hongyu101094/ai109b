def queen(n):
    q = [] #q 代表已經排下去的皇后,一開始還沒排,所以是空的
    return queenNext(n, q) #回傳皇后位置

def queenNext(n, q): #已經排好 q[0..y2-1],繼續排下去
    y2 = qlen = len(q) 
    if qlen == n: #全部排好了 
        print(q)  #印出盤面
        return   
    # 還沒排滿，繼續排下去 
    for x2 in range(n): #對本列的每個X去嘗試
        isConflict = False
        for y in range(qlen): #前面已經排下去的皇后，座標為X,Y
            if conflict(q[y],y,x2,y2): #檢查新排的皇后跟前面的有沒有衝突
                isConflict = True
        if not isConflict:  #如果沒有衝突，就繼續排下去
            q.append(x2)    #把(x2,y2)放進盤面
            queenNext(n, q) #繼續遞回尋找下一個皇后位子
            q.pop()         #把(x2,y2)移出盤面
        
def conflict(x1,y1,x2,y2):  #判斷(x1,y1), (x2,y2)是否有衝突
    if x1==x2: return True #檢查直行
    if y1==y2: return True #檢查橫列
    if x1+y1==x2+y2: return True #檢查斜方
    if x1-y1==x2-y2: return True #檢查另一個斜方
    return False
queen(8)#列出八皇后的解答