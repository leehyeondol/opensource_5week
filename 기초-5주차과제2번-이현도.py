import operator
instr = """널 품기 전 알지 못했다. 내 머문 세상 이토록 찬란한 것을 작은 숨결로 닿은 사랑 겁없이 나를 불러준 사랑.
몸시도 좋 았다 너를 지켜보고 설레고 우습게 지투도 했던 평번한 모든 순간들이 캄캄한 영원 그 오랜 기다림 속으로 햇살처럼 니가 내렸다."""
cdic = {}
clist = []
if __name__ == "__main__":
    for ch in instr:
        if "ㄱ" <= ch and ch <= "힣":
            if ch in cdic:
                cdic[ch]+=1
            else:
                cdic[ch] =1
    clist = sorted(cdic.items(),key = operator.itemgetter(1),reverse = True)
    print("원문\n",instr)
    print("--------------------")
    print("문자 \t 빈도수")
    print("--------------------")
    for i in range(0,len(clist)):
        print(clist[i][0], '\t',clist[i][1])
