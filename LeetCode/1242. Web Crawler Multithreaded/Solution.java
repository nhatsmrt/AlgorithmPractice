/**
 * // This is the HtmlParser's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface HtmlParser {
 *     public List<String> getUrls(String url) {}
 * }
 */
class Solution {
    public List<String> crawl(String startUrl, HtmlParser htmlParser) {
        List<String> outputs = new ArrayList<String>();
        String host = getHostName(startUrl);
        Set<String> visited = new HashSet<String>();
        visited.add(startUrl);

        CrawlerRun run = new CrawlerRun(startUrl, host, visited, outputs, htmlParser);
        Thread main = new Thread(run);
        main.start();

        try {
            main.join();
        } catch (InterruptedException e) {
            System.out.println("fail");
        }

        return outputs;
    }

    private class CrawlerRun implements Runnable {
        private String url;
        private String host;
        private Set<String> visited;
        private List<String> outputs;
        private HtmlParser parser;

        public CrawlerRun(String url, String host, Set<String> visited, List<String> outputs, HtmlParser parser) {
            this.url = url;
            this.host = host;
            this.visited = visited;
            this.outputs = outputs;
            this.parser = parser;
        }

        public void run() {
            synchronized (outputs) {
                outputs.add(url);
            }

            List<String> subUrls = null;

            subUrls = parser.getUrls(url);

            List<Thread> subthreads = new ArrayList<>();

            for (String subUrl : subUrls) {
                boolean toAdd = false;

                if (getHostName(subUrl).equals(host)) {
                    synchronized(visited) {
                        if (!visited.contains(subUrl)) {
                            visited.add(subUrl);
                            toAdd = true;
                        }
                    }

                    if (toAdd) {
                        CrawlerRun newRun = new CrawlerRun(subUrl, host, visited, outputs, parser);
                        subthreads.add(new Thread(newRun));
                    }
                }
            }

            for (Thread t : subthreads)
                t.start();

            try {
                for (Thread t : subthreads)
                    t.join();
            } catch (InterruptedException e) {
                System.out.println("fail");
            }

        }

    }

    private String getHostName(String url) {
        return url.split("/")[2];
    }
}
