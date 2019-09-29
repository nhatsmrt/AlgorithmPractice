class Skiplist {
    private int max_level;
    private Column head;
    private Column tail;
    private Random random;
    private int size;

    public Skiplist() {
        this(16);
    }

    public Skiplist(int maxLevel) {
        this.max_level = maxLevel;
        random = new Random();
        head = new Column(-1);
        tail = new Column(-1);

        for (int i = 0; i < max_level; i++) {
            head.cells.add(new Cell(null, tail));
            tail.cells.add(new Cell(head, null));
        }
    }


    public boolean search(int target) {
        Column tailList = tailList(target);
        return tailList != tail && tailList.value == target;
    }

    public Column tailList(int target) {

        Column it = head;
        for (int level = max_level - 1; level >= 0; level--) {
            while (
                it.cells.get(level).next != tail &&
                it.cells.get(level).next.value < target
            )
                it = it.cells.get(level).next;
        }

        return it.cells.get(0).next;
    }

    public void add(int num) {
        size += 1;

        Column newColumn = new Column(num);
        newColumn.cells.add(new Cell(null, null));

        while (newColumn.cells.size() < max_level && random.nextInt(2) != 0)
            newColumn.cells.add(new Cell(null, null));

        Column it = head;
        for (int level = max_level - 1; level >= 0; level--) {
            while (
                it.cells.get(level).next != tail
                && it.cells.get(level).next.value < num
            )
                it = it.cells.get(level).next;
            if (level < newColumn.cells.size()) {
                newColumn.cells.get(level).next = it.cells.get(level).next;
                it.cells.get(level).next.cells.get(level).previous = newColumn;
                newColumn.cells.get(level).previous = it;
                it.cells.get(level).next = newColumn;
            }
        }
    }

    public boolean erase(int num) {
        Column tailList = tailList(num);

        if (tailList != tail && tailList.value == num) {
            size -= 1;
            for (int level = tailList.cells.size() - 1; level >= 0; level--) {
                Cell cell = tailList.cells.get(level);
                cell.previous.cells.get(level).next = cell.next;
                cell.next.cells.get(level).previous = cell.previous;
            }

            return true;
        }

        return false;
    }

    public String toString() {
        StringBuilder ret = new StringBuilder("[");
        Column it = head;
        while (it.cells.get(0).next != tail) {
            if (ret.length() > 1)
                ret.append(", ");
            it = it.cells.get(0).next;
            ret.append(it.value);
        }
        ret.append("]");

        return ret.toString();
    }

    private void toStringFull() {
        for (int i = max_level - 1; i >= 0; i--) {
            StringBuilder ret = new StringBuilder("[-1");
            Column it = head;
            while (it.cells.get(i).next != tail) {
                // if (ret.length() > 1)
                    ret.append(", ");
                it = it.cells.get(i).next;
                ret.append(it.value);
            }
            ret.append("]");
            System.out.println(ret.toString());
        }
    }

    private class Column {
        int value;
        List<Cell> cells;

        public Column(int value) {
            this.value = value;
            cells = new ArrayList<Cell>();
        }
    }

    private class Cell {
        Column next;
        Column previous;

        public Cell(Column previous, Column next) {
            this.next = next;
            this.previous = previous;
        }
    }
}

/**
 * Your Skiplist object will be instantiated and called as such:
 * Skiplist obj = new Skiplist();
 * boolean param_1 = obj.search(target);
 * obj.add(num);
 * boolean param_3 = obj.erase(num);
 */
