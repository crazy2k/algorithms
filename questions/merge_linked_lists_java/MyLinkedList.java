
public class MyLinkedList {
	
	private MyLinkedListNode head;
	private MyLinkedListNode tail;
	
	public MyLinkedList() {
		head = null;
		tail = null;
	}
	
	public void append(int item) {
		MyLinkedListNode node = new MyLinkedListNode(item);
		if (this.head == null) {
			this.head = node;
		}
		else {
			this.tail.setNextNode(node);
		}
		this.tail = node;
		this.tail.setNextNode(null);
	}
	
	public MyLinkedList merge(MyLinkedList other) {
		MyLinkedList merged = new MyLinkedList();
		
		MyLinkedListNode selfNode = getHead();
		MyLinkedListNode otherNode = other.getHead();
		
		while (selfNode != null && otherNode != null) {
			if (selfNode.getItem() < otherNode.getItem()) {
				merged.append(selfNode.getItem());
				selfNode = selfNode.getNextNode();
			}
			else {
				merged.append(otherNode.getItem());
				otherNode = otherNode.getNextNode();
			}
		}
		
		if (otherNode == null) {
			while (selfNode != null) {
				merged.append(selfNode.getItem());
				selfNode = selfNode.getNextNode();
			}
		}
		else {
			while (otherNode != null) {
				merged.append(otherNode.getItem());
				otherNode = otherNode.getNextNode();
			}
		}
		
		return merged;
	}
	
	public MyLinkedListNode getHead() {
		return head;
	}

	public void setHead(MyLinkedListNode head) {
		this.head = head;
	}
	
	public MyLinkedListNode getTail() {
		return tail;
	}

	public void setTail(MyLinkedListNode tail) {
		this.tail = tail;
	}
	
	public static void main(String[] args) {
		MyLinkedList l1 = new MyLinkedList();
		l1.append(1);
		l1.append(3);
		l1.append(5);
		
		MyLinkedList l2 = new MyLinkedList();
		l2.append(2);
		l2.append(4);
		l2.append(7);
		l2.append(8);
		l2.append(9);
		
		MyLinkedList l3 = l1.merge(l2);
		MyLinkedListNode node = l3.getHead();
		while (node != null) {
			System.out.println(node.getItem());
			node = node.getNextNode();
		}
	}

}
