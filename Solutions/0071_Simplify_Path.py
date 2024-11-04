class Solution:
    def simplifyPath(self, path: str) -> str:
        split_path = path.split("/")
        
        sol = []
        ignore_set = set(["", "."])
        for each_path in split_path:
            if each_path in ignore_set:
                continue

            elif each_path == "..":
                if sol:
                    sol.pop()
            else:
                sol.append("/" + each_path)
        if sol:
            return "".join(sol)
        else:
            return "/"