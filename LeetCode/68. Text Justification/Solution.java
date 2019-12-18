class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        int start = 0;
        int end = 0;
        int length = 0;

        List<String> ret = new ArrayList<String>();

        while (start < words.length) {
            end = start + 1;
            StringBuilder sentence = new StringBuilder();
            int curLength = words[start].length();
            int totalLength = curLength;

            while (end < words.length && words[end].length() + 1 + curLength <= maxWidth) {
                curLength += words[end].length() + 1;
                totalLength += words[end].length();
                end += 1;
            }

            if (end == words.length) {
                for (int i = start; i < end; i++) {
                    sentence.append(words[i]);
                    if (i < end - 1) {
                        sentence.append(" ");
                        totalLength += 1;
                    }
                }

                for (int i = 0; i < maxWidth - totalLength; i++)
                    sentence.append(" ");
            }
            else {
                int[] spaces = generateSpace(
                    maxWidth - totalLength,
                    Math.max(end - start - 1, 1)
                );

                for (int i = start; i < end; i++) {
                    sentence.append(words[i]);
                    if (i < end - 1 || i == start) {
                        for (int j = 0; j < spaces[i - start]; j++)
                            sentence.append(" ");
                    }
                }

            }

            ret.add(sentence.toString());
            start = end;
        }

        return ret;
    }

    private int[] generateSpace(int numSpaces, int numSpots) {
        int[] ret = new int[numSpots];
        int spacePerSpot = numSpaces / numSpots;
        int numSpotWithExtra = numSpaces % numSpots;

        for (int i = 0; i < numSpots; i++) {
            if (i < numSpotWithExtra)
                ret[i] = spacePerSpot + 1;
            else
                ret[i] = spacePerSpot;
        }

        return ret;
    }
}
