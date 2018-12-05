public class Codec {
    private final String prefix = "http://tinyurl.com/";
    private Map<String, String> database;

    public Codec() {
       database = new HashMap<String, String> ();
    }

    // Encodes a URL to a shortened URL.
    public String encode(String longUrl) {
        int ind = database.keySet().size();
        String ret = prefix + ind;
        database.put(ret, longUrl);

        return ret;
    }

    // Decodes a shortened URL to its original URL.
    public String decode(String shortUrl) {
        return database.get(shortUrl);
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(url));
