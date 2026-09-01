class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = 0 
        seen = set()

        for email in emails:
            splitted_email = email.split('@')
            splitted_email_first = (splitted_email[0].split('.'))
            splitted_email_second = (splitted_email[1])

            result = str(" ".join(splitted_email_first))
            result = result.split('+')[0]

            result = result.replace(' ', '')

            email_list = result + splitted_email_second

            print(email_list)
        
            if email_list in seen:
                pass
            else:
                seen.add(email_list)
                unique += 1
        print(seen)
            
                

        return unique