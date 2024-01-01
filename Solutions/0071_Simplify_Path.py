class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split("/")

        sol_list = []

        for each_path_list in path_list:
            if each_path_list:
                if each_path_list == "..":
                    if sol_list:
                        sol_list.pop()
                elif each_path_list == ".":
                    pass
                else:
                    sol_list.append(each_path_list)

        sol = ""
        for each_sol in sol_list:
            sol += "/" + each_sol
        if not sol:
            return "/"
        return sol