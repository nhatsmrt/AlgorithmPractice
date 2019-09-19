class SkipList {
    private int maxLevel;
    private Column head;
    private Column tail;
    private Random random;
    private int size;

    public SkipList(int maxLevel) {
        this.maxLevel = maxLevel;
        size = 0;
        random = new Random();
        head = new Column(null);

        tail = new Column(null);

        for (int i = 0; i < maxLevel; i++) {
            head.cells.add(new Cell(null, tail));
            tail.cells.add(new Cell(head, null));
        }
    }

    public boolean isEmpty() {
        return head.cells.get(0).next == tail;
    }

    public Column tailList(int value) {
        // find sublist of numbers >= value
        Column it = head;
        for (int level = maxLevel - 1; level >= 0; level--) {
            while (
                it.cells.get(level).next != null && // not end
                it.cells.get(level).next != tail && // not tail
                it.cells.get(level).next.value < value // still less
            )
                it = it.cells.get(level).next;
        }

        return it.cells.get(0).next;
    }

    public int rank(int value) {
        Column tailList = tailList(value);
        Column it = head;

        int ret = 0;
        while(it.cells.get(0).next != tailList) {
            ret += 1;
            it = it.cells.get(0).next;
        }

        return ret;
    }

    public void insert(int value) {
        Column newColumn = new Column(value);
        newColumn.cells.add(new Cell(null, null));

        while(newColumn.cells.size() < maxLevel && random.nextInt(2) == 0)
            newColumn.cells.add(new Cell(null, null));


        Column it = head;
        for (int level = maxLevel - 1; level >= 0; level--) {
            while (
                it.cells.get(level).next != null && // not end
                it.cells.get(level).next != tail && // not tail
                it.cells.get(level).next.value < value
            ) {
                it = it.cells.get(level).next;
            }
            if (level < newColumn.cells.size()) {
                newColumn.cells.get(level).next = it.cells.get(level).next;
                newColumn.cells.get(level).previous = it;
                it.cells.get(level).next = newColumn;
            }
        }
        size += 1;
    }

    public boolean remove(int value) {
        Column tailList = tailList(value);
        if (tailList.value == value) {
            for (int level = 0; level < tailList.cells.size(); level ++) {
                tailList.cells.get(level).previous.cells.get(level).next =
                    tailList.cells.get(level).next;
                tailList.cells.get(level).next.cells.get(level).previous =
                    tailList.cells.get(level).previous;
            }
            size -= 1;
            return true;
        }
        else
            return false;
    }

    public int size() {
        return size;
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

    private class Column {
        Integer value;
        List<Cell> cells;

        public Column(Integer value) {
            this.value = value;
            cells = new ArrayList<Cell>();
        }
    }

    private class Cell {
        Column previous;
        Column next;

        public Cell(Column previous, Column next) {
            this.previous = previous;
            this.next = next;
        }
    }
}
