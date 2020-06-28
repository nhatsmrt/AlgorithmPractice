import java.util.regex.*;

class Solution {
    public String validIPAddress(String IP) {
        String ipv4GroupPattern =
            "(0|[1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])";
        Pattern ipv4 = Pattern.compile(
            "(" +  ipv4GroupPattern + "\\.){3}" + ipv4GroupPattern
        );

        String ipv6GroupPattern =
            "(([0-9]|[a-f]|[A-F]){1,4})";
        Pattern ipv6 = Pattern.compile(
            "(" +  ipv6GroupPattern + "\\:){7}" + ipv6GroupPattern
        );

        if (ipv4.matcher(IP).matches())
            return "IPv4";

        if (ipv6.matcher(IP).matches())
            return "IPv6";

        return "Neither";
    }
}
