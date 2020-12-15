use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn unique_occurrences(arr: Vec<i32>) -> bool {
        let cnter = get_counter(&arr);
        let counts : Vec<&i32> = cnter.values().collect();
        let mut unique_counts : HashSet<&i32> = HashSet::new();

        for val in counts.iter() {
            unique_counts.insert(val);
        }

        counts.len() == unique_counts.len()
    }
}

fn get_counter(arr: &Vec<i32>) -> HashMap<i32, i32> {
    arr.iter().fold(HashMap::new(), |mut cnter, x| {
        let cnt = *cnter.get(x).get_or_insert(&(0 as i32));
        cnter.insert(*x, cnt + 1);
        cnter
    })
}
