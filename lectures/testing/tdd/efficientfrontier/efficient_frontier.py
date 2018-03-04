"""
Placeholder for the exercise
"""
class efficient_frontier:

    def calculate_effi_fron(self, return_risk: list) -> list:
        """
        Sort with return and then delete those have same return but higher risk investment
        """
        optimal_dic = {}
        return_set = set()
        result = []
        for return_v, risk in return_risk:
            # if return is negative, then not adding to the result.
            if return_v >= 0:
                if return_v not in return_set:
                    optimal_dic[return_v] = risk
                    return_set.add(return_v)
                else:
                    # update the risk
                    if optimal_dic[return_v] > risk:
                        optimal_dic[return_v] = risk
        for num in optimal_dic:
            result.append((num, optimal_dic[num]))
        result.sort()
        result = result[::-1]
        return result

