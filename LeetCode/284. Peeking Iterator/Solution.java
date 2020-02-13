// Java Iterator interface reference:
// https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html
class PeekingIterator implements Iterator<Integer> {
    private int buffer;
    private boolean inBuffer;
    private Iterator<Integer> it;

	public PeekingIterator(Iterator<Integer> iterator) {
	    // initialize any member here.
	    inBuffer = false;
        it = iterator;
	}

    // Returns the next element in the iteration without advancing the iterator.
	public Integer peek() {
        if (!inBuffer) {
            buffer = it.next();
            inBuffer = true;
        }
        return buffer;
	}

	// hasNext() and next() should behave the same as in the Iterator interface.
	// Override them if needed.
	@Override
	public Integer next() {
	    if (inBuffer) {
            inBuffer = false;
            return buffer;
        }
        return it.next();
	}

	@Override
	public boolean hasNext() {
	    return inBuffer || it.hasNext();
	}
}
