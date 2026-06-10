class Solution:
    def countSeniors(self, details: List[str]) -> int:
        age_count = 0
        for name in details:
            if int((name[11:13])) > 60:
                age_count +=1
        return(age_count)