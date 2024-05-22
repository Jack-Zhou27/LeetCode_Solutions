/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public void deleteNode(ListNode node) {

        //In short, we need to first: override the contents of node to be NextNode (effectively deleting it)
        //second: change the pointer of node to NextNextNode or else we are linking "NextNode" (this is the node we changed to be nextnode) literally to NextNode

        
        node.val = node.next.val; 
        //we override the node that we were given by making the previous node link up to the "NEXT" node in the line
        node.next = node.next.next;
        //if we didn't add this line, this node will link back onto itself because it was originally set up to link up to the "NEXT" node in the line, so in order to stop it from linking up to itself, we need to link it up to the "NEXT NEXT" node in the line
    }
}
