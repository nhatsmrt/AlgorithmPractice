class TicketMap {
    private Map<String, Map<String, Integer>> data;
    private boolean sort;

    public TicketMap(boolean sort) {
        data = new HashMap<String, Map<String, Integer>>();
        this.sort = sort;
    }

    public int getCount(String city, String destination) {
        if (!data.containsKey(city) || !data.get(city).containsKey(destination))
            return 0;
        return data.get(city).get(destination);
    }

    public void addTicket(String from, String to) {
        if (!data.containsKey(from)) {
            if (sort)
                data.put(from, new TreeMap<String, Integer>());
            else
                data.put(from, new HashMap<String, Integer>());
        }

        Map<String, Integer> countMap = data.get(from);
        countMap.put(to, countMap.getOrDefault(to, 0) + 1);
    }

    public void removeTicket(String from, String to) {
        if (data.containsKey(from) && data.get(from).containsKey(to)) {
            Map<String, Integer> countMap = data.get(from);
            countMap.put(to, countMap.get(to) - 1);
        }
    }

    public boolean containsKey(String key) {
        return data.containsKey(key);
    }

    public Set<String> get(String key) {
        return data.get(key).keySet();
    }
}


class Solution {
    public List<String> findItinerary(List<List<String>> tickets) {
        TicketMap adjLists = new TicketMap(true);
        TicketMap usedTickets = new TicketMap(false);

        for (List<String> ticket : tickets) {
            String from = ticket.get(0);
            String to = ticket.get(1);
            adjLists.addTicket(from, to);
        }

        List<String> ret = new ArrayList<String>();
        dfs(adjLists, ret, usedTickets, "JFK", tickets.size());
        return ret;
    }

    private void dfs(
        TicketMap adjLists, List<String> ret,
        TicketMap usedTickets, String city, int nTickets
    ) {
        ret.add(city);
        if (adjLists.containsKey(city)) {
            for (String candidate : adjLists.get(city)) {
                if (usedTickets.getCount(city, candidate) < adjLists.getCount(city, candidate)) {
                    usedTickets.addTicket(city, candidate);
                    dfs(adjLists, ret, usedTickets, candidate, nTickets);
                    if (ret.size() == nTickets + 1)
                        break;
                    else {
                        ret.remove(ret.size() - 1);
                        usedTickets.removeTicket(city, candidate);
                    }
                }
            }
        }
    }
}
