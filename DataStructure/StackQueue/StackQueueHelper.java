import java.util.*;

public class StackQueueHelper {

  public void q2s(Queue<Integer> q, Stack<Integer> s) {
    while (!q.isEmpty())
      s.push(q.remove());
  }

  public void s2q(Stack<Integer> s, Queue<Integer> q) {
    while (!s.isEmpty())
      q.add(s.pop());
  }

}
