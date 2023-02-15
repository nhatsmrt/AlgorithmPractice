struct chunk {
    int start;
    int size;
    struct chunk *next;
    struct chunk *prev;
};

struct chunk_lst {
    struct chunk *head;
    struct chunk *tail;
};

struct chunk *alloc_chunk() {
    return (struct chunk*)malloc(sizeof(struct chunk));
}

struct chunk_lst *alloc_list() {
    struct chunk_lst *ret =
        (struct chunk_lst *)malloc(sizeof(struct chunk_lst));
    ret->head = alloc_chunk();
    ret->tail = alloc_chunk();

    ret->head->next = ret->tail;
    ret->tail->prev = ret->head;

    return ret;
}

struct chunk *find_prev_chunk(int start, struct chunk_lst *lst) {
    struct chunk *ret = lst->head;
    while (ret->next != lst->tail && ret->next->start < start)
        ret = ret->next;
    return ret;
}

void insert_at(struct chunk *chunk, struct chunk *par) {
    chunk->next = par->next;
    chunk->prev = par;

    par->next->prev = chunk;
    par->next = chunk;
}

void remove(struct chunk *chunk) {
    chunk->next->prev = chunk->prev;
    chunk->prev->next = chunk->next;
}

void remove_and_free(struct chunk *chunk) {
    remove(chunk);
    free(chunk);
}

void lst_insert(struct chunk *chunk, struct chunk_lst *lst) {
    struct chunk *par = find_prev_chunk(chunk->start, lst);

    /* merge consecutive chunks */
    if (par->next != lst->tail && par->next->start == chunk->start + chunk->size) {
        chunk->size += par->next->size;
        remove_and_free(par->next);
    }

    insert_at(chunk, par);

    if (par != lst->head && par->start + par->size == chunk->start) {
        par->size += chunk->size;
        remove_and_free(chunk);
    }
}

class Allocator {
private:
    struct chunk_lst *free_lst;
    unordered_map<int, vector<struct chunk *>> alloced;
public:
    Allocator(int n) {
        struct chunk *first = alloc_chunk();
        first->start = 0;
        first->size = n;

        free_lst = alloc_list();
        insert_at(first, free_lst->head);
    }

    int allocate(int size, int mID) {
        struct chunk *it = free_lst->head->next;

        while (it != free_lst->tail && it->size < size)
            it = it->next;

        if (it == free_lst->tail)
            return -1;

        if (it->size > size) {
            struct chunk *remain = alloc_chunk();
            remain->start = it->start + size;
            remain->size = it->size - size;

            insert_at(remain, it);
            it->size = size;
        }

        remove(it);

        if (alloced.find(mID) == alloced.end()) {
            vector<struct chunk *> vect;
            alloced[mID] = vect;
        }

        alloced[mID].push_back(it);
        return it->start;
    }

    int free(int mID) {
        int freed = 0;

        if (alloced.find(mID) != alloced.end()) {
            vector<struct chunk *> chunks = alloced[mID];

            for (struct chunk *chunk : chunks) {
                freed += chunk->size;
                lst_insert(chunk, free_lst);
            }

            alloced.erase(mID);
        }

        return freed;
    }
};

/**
 * Your Allocator object will be instantiated and called as such:
 * Allocator* obj = new Allocator(n);
 * int param_1 = obj->allocate(size,mID);
 * int param_2 = obj->free(mID);
 */
