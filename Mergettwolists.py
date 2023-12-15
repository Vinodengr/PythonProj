class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        stack =[]
        
        for i in list1:
            print(i)
            for j in list2:
                print(j)
                if j > i:
                    stack.append(i)
                    stack.append(j)
                else:
                    stack.append(j)
                    stack.append(i)
        return stack
    

        for i in range(len(list1)):
            print(i)
            if list1(i)>list2(j):
                list1
            for j in list2:
                print(j)
                if j > i:
                    stack.append(i)
                    stack.append(j)
                else:
                    stack.append(j)
                    stack.append(i)
        return stack
    

x = Solution.mergeTwoLists(None, [1,2,3],[4,5,6])
print(x)
                
