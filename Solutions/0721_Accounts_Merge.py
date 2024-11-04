class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        #{key: str(name), value: [set(email)]}
        name_dict = {}

        for each_accounts in accounts:
            name = each_accounts[0]
            email_list = each_accounts[1:]

            if name in name_dict:
                name_dict_email_list = name_dict[name]
                index = 0
                isMerge = False
                isMerge_index = None
                while index < len(name_dict[name]):
                    for each_email_list in email_list:
                        if each_email_list in name_dict_email_list[index]:
                            name_dict[name][index] = name_dict_email_list[index].union(email_list)
                            if isMerge:
                                name_dict_email_list[isMerge_index] = name_dict_email_list[isMerge_index].union(name_dict[name].pop(index))
                                index -= 1
                            else:
                                isMerge = True
                                isMerge_index = index
                            break
                    index += 1
                if not isMerge:
                    name_dict[name].append(set(email_list))
            else:
                name_dict[name] = [set(email_list)]

        sol = []
        for name, email_list in name_dict.items():
            for each_email_list in email_list:
                sol.append([name] + sorted(list(each_email_list)))

        return sol
        