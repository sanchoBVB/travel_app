class AHP_class:
    def matrix(self, l1, N):
        M = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(N):
            x = l1[i]
            for j in range(N):
                y = l1[j]
                if x > y:
                    M[i][j] = 1/(((x-y)*2)+1)
                else:
                    M[i][j] = (((y-x)*2)+1)
        return M

    def weight(self, l2, size):
        cnt = []
        for i in l2:
            line = 1
            for j in range(size):
                line *= i[j]
            line = round(line**(1/size), 3)
            cnt.append(line)
        ans = [c/sum(cnt) for c in cnt]
        return ans

    def final(self, li0, li1, li2, li3, li4, li5):
        res = []
        for n in range(13):
            a1 = li0[0]*li1[n]
            a2 = li0[1]*li2[n]
            a3 = li0[2]*li3[n]
            a4 = li0[3]*li4[n]
            a5 = li0[4]*li5[n]
            res.append(a1+a2+a3+a4+a5)
        return res
