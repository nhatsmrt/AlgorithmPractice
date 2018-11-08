import java.util.*;

public class StackQueueHelper {

  public <E> void q2s(Queue<E> q, Stack<E> s) {
    while (!q.isEmpty())
      s.push(q.remove());
  }

  public <E> void s2q(Stack<E> s, Queue<E> q) {
    while (!s.isEmpty())
      q.add(s.pop());
  }

  public <E> void reverseStack(Stack<E> s) {
    Queue<E> q = new LinkedList<E>();
    s2q(s, q);
    q2s(q, s);
  }

  public <E> void reverseQueue(Queue<E> q) {
    Stack<E> s = new Stack<E>();
    q2s(q, s);
    s2q(s, q);
  }

}
