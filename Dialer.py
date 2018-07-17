import re
class Solution:
    
    def letterCombinations(self, digits):
        if not digits:
            return []

        lookup, result = ["", "", "abc", "def", "ghi", "jkl", "mno", \
                          "pqrs", "tuv", "wxyz"], [""]
        for digit in reversed(digits):
            choices = lookup[int(digit)]
            m, n = len(choices), len(result)
            result += [result[i % n] for i in xrange(n, m * n)]
            for i in xrange(m * n):
                result[i] = choices[i / n] + result[i]

        return result

class Solution2:
    
    def letterCombinations(self, digits):
        if not digits:
            return []
        lookup, result = ["", "", "abc", "def", "ghi", "jkl", "mno", \
                          "pqrs", "tuv", "wxyz"], []
        self.letterCombinationsRecu(result, digits, lookup, "", 0)
        return result

    def letterCombinationsRecu(self, result, digits, lookup, cur, n):
        if n == len(digits):
            result.append(cur)
        else:
            for choice in lookup[int(digits[n])]:
                self.letterCombinationsRecu(result, digits, lookup, cur + choice, n + 1)

if __name__ == "__main__":

	list1=[]
	list2=[]
	list3=[]
	list4=[]
	#print Solution().letterCombinations("234")

	x=raw_input('Enter the Digits ')	
	Solution().letterCombinations(x)
	for a in Solution().letterCombinations(x):
		if re.match("^[aeiou][aeiou][aeiou]$|^[aeiou][aeiou][aeiou][aeiou]$ ",a):
        	       	list1.append(a)
      		    
                elif re.match("^.?[aeiou][aeiou]$|^[aeiou].?[aeiou]$|[aeiou][aeiou].?$|^.?[aeiou][aeiou][aeiou]$|^[aeiou].?[aeiou][aeiou]$|[aeiou][aeiou].?[aeiou]$|[aeiou][aeiou][aeiou].? ",a):
			list2.append(a)
                elif re.match("^.?.?[aeiou]$|^[aeiou].?.?$|.?[aeiou].?$|^.?.?[aeiou][aeiou]$|^[aeiou].?.?[aeiou]$|[aeiou][aeiou].?.?$|[aeiou].?[aeiou].?|^.?[aeiou][aeiou].?$",a):
			list3.append(a)
		else:                
			list4.append(a)
                
	
        l1=list1+list2+list3
        l2=list1+list2+list3+list4

	l3=[]
	l3.append(list1)
	l3.append(list2)
        l3.append(list3)
		
        for j in l3:
		
		if j!=[]:
			print '\nBest Match :: ',j
			break 
	print '\n============================================\n'
        print 'Other Vowel Matches :: ',l1,'\n'
        print '============================================\n'
	print 'All Matches   :: ',l2
