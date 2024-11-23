class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m = len(box)
        n = len(box[0])
        sol = [[""] * m for _ in range(n)]
        stone_list = []

        for index_m, each_m in enumerate(box):
            for index_n, each_n in enumerate(each_m):
                if not each_n == "#":
                    sol[index_n][m - index_m - 1] = each_n
                else:
                    sol[index_n][m - index_m - 1] = "."
                    stone_list.append((index_n, m - index_m - 1))
        for s_m, s_n in stone_list:
            if sol[s_m][s_n] == "#":
                while sol[s_m][s_n] == "#":
                    s_m -= 1
                sol[s_m][s_n] = "#"
            else:
                while sol[s_m][s_n] == ".":
                    if s_m == n-1:
                        sol[s_m][s_n] = "#"
                        break
                    elif sol[s_m+1][s_n] == "*" or sol[s_m+1][s_n] == "#":
                        sol[s_m][s_n] = "#"
                        break
                    else:
                        s_m += 1
        return sol