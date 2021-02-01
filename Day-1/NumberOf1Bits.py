
#Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
#the input will be given as a signed integer type.
#The input must be a binary string of length 32

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        bit = '{0:032b}'.format(n) #convert int into 32 bit
        # print(bit)
        
        counter=0
        for i in range(len(bit)):
            if (int(bit[i])==1):
                counter=counter+1
        return counter