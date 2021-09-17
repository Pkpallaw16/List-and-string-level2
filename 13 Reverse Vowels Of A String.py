class Solution(object):
    def reverseVowels(self, str1):
        """
        :type s: str
        :rtype: str
        """
        vov=[]
        for i in range(len(str1)):
            if str1[i] in ('a','e','i','o','u','A','E','I','O','U'):
                vov.append(i)
        if len(vov)<=1:
            return str1
        else:
            i=0
            j=len(vov)-1
            while i<j:
                p=vov[i]
                q=vov[j]
                str1=str1[:p]+str1[q]+str1[p+1:q]+str1[p]+str1[q+1:]
                i+=1
                j-=1
        return str1
print(Solution.reverseVowels("leetcode"))