/**
 * Definition for singly-linked list.
 * class ListNode {
 *     public int val;
 *     public ListNode next;
 *     ListNode(int x) { val = x; next = null; }
 * }
 */
import java.util.ArrayList;

public class Solution {
    public ListNode subtract(ListNode A) {
        ArrayList<Integer> arr = new ArrayList<>();
        
        ListNode curr = A;
        ListNode next;
        while (curr != null) {
            next = curr.next;
            arr.add(curr.val);
            curr = next;
        }
        
        int index = 0;
        curr = A;
        next = null;
        while (curr != null && index < arr.size()/2) {
            next = curr.next;
            curr.val = arr.get(arr.size() - 1 - index) - curr.val;
            curr = next;
            index += 1;
        }
        
        return A;
    }
}