class Solution {
    public boolean judgeCircle(String moves) {
        int x = 0;
        int y = 0;

        for (int i = 0; i < moves.length(); i++) {
            if (moves.charAt(i) == 'U')
                y += 1;
            else if (moves.charAt(i) == 'D')
                y -= 1;
            else if (moves.charAt(i) == 'L')
                x -= 1;
            else
                x += 1;
        }

        return x == 0 && y == 0;
    }
}
