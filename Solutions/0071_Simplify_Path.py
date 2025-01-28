class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split("/")

        sol = []

        for each_path in path_list:
            if each_path == ".":
                continue
            elif each_path == "..":
                if sol:
                    sol.pop()
            elif each_path == "":
                continue
            else:
                sol.append(each_path)
        return "/" + '/'.join(sol)