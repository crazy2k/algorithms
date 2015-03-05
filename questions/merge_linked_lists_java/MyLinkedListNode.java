
public class MyLinkedListNode {
	private int item;
	private MyLinkedListNode nextNode;
	
	public MyLinkedListNode(int anItem) {
		setItem(anItem);
		setNextNode(null);
	}

	public int getItem() {
		return item;
	}

	public void setItem(int item) {
		this.item = item;
	}

	public MyLinkedListNode getNextNode() {
		return nextNode;
	}

	public void setNextNode(MyLinkedListNode nextNode) {
		this.nextNode = nextNode;
	}
	
}
