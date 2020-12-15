use std::collections::HashMap;


impl Solution {
    pub fn anagram_mappings(a: Vec<i32>, b: Vec<i32>) -> Vec<i32> {
        let mut ret = Vec::new();
        let mut index = get_index(&b);

        for val in a.iter() {
            let mut occs = index.get_mut(val).unwrap();
            ret.push(occs.pop().unwrap() as i32);
        }

        ret
    }
}

fn get_index(a: &Vec<i32>) -> HashMap<i32, Vec<usize>> {
    let mut ret = HashMap::new();

    for (i, &val) in a.iter().enumerate() {
        if !ret.contains_key(&val) {
            ret.insert(val, Vec::new());
        }

        let mut occs = ret.get_mut(&val).unwrap();
        occs.push(i);
    }

    ret
}
