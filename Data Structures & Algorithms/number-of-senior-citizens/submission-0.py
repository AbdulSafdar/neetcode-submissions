class Solution:
    def countSeniors(self, details: List[str]) -> int:
        age_count = 0
        for name in details:
            age = int((name[11:13]))
            if age > 60:
                age_count +=1
        return(age_count)