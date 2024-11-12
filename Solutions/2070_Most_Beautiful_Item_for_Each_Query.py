class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda x: x[0])

        items_list = []
        prev_price = 0
        max_beauty = 0
        prev_min_price = 0
        prev_max_beauty = 0

        for price, beauty in items:
            if not prev_price == price:
                max_beauty = max(max_beauty, beauty)
                if prev_max_beauty < max_beauty:
                    items_list.append((prev_min_price, price, prev_max_beauty))
                    prev_min_price = price
                    prev_max_beauty = max_beauty
            else:
                max_beauty = max(max_beauty, beauty)
        items_list.append((prev_min_price, float('inf'), prev_max_beauty))

        sol = []
        for each_queries in queries:
            left = 0
            right = len(items_list) - 1

            isAdded = False
            while left < right:
                mid = (left + right) // 2
                min_price, max_price, max_beauty = items_list[mid]

                if min_price <= each_queries and each_queries < max_price:
                    sol.append(max_beauty)
                    isAdded = True
                    break
                
                if min_price > each_queries:
                    right = mid
                else:
                    left = mid + 1
            if not isAdded:
                sol.append(items_list[left][2])
        return sol