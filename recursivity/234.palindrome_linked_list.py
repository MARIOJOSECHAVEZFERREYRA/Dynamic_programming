from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    #def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #Solucion con punteros left  right y cambiando linked list a array, O(n) tiempo, O(n) espacio.
    #     list_vals = []
    #     while head:
    #         list_vals.append(head.val)
    #         head = head.next
    #     left, right = 0, len(list_vals) - 1
    #     while left < right and list_vals[left] == list_vals[right]:
    #         left += 1
    #         right -= 1
    #     return left >= right


    # def isPalindrome(self, head: Optional[ListNode]) -> bool:
         #Con recursion (sinceramente entendi el algoritmo pero no el codigo lol) O(n) tiempo, O(n) espacio.
    #     self.curr = head
    #     return self.solve(head)
    # def solve(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if head is None:
    #         return True
    #     ans = self.solve(head.next) and head.val == self.curr.val
    #     self.curr = self.curr.next
    #     return ans

   def reverse(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev
   def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow,fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        rev = self.reverse(slow)    #second half of linked list reversed
        while rev:
            if head.val != rev.val:
                return False
            head = head.next
            rev = rev.next
        return True

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(2)
node4 = ListNode(1)

node1.next = node2
node2.next = node3
node3.next = node4

solution = Solution()
print(solution.isPalindrome(node1))




