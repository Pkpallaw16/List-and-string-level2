class Solution(object):
    def complexNumberMultiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        a1=num1[:num1.index("+")]
        b1=num1[num1.index("+")+1:-1]
        a2=num2[:num2.index("+")]
        b2=num2[num2.index("+")+1:-1]
        a=int(a1)*int(a2)-int(b1)*int(b2)
        b=int(a1)*int(b2)+int(a2)*int(b1)
        return str(a)+"+"+str(b)+"i"