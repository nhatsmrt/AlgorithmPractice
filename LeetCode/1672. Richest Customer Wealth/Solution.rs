impl Solution {
    pub fn maximum_wealth(accounts: Vec<Vec<i32>>) -> i32 {
        return accounts.iter().map(|acc| acc.iter().sum()).max().unwrap()
    }
}
