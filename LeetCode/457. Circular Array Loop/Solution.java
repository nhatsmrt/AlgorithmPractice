class Solution {
    public boolean circularArrayLoop(int[] nums) {
        if (nums.length <= 1)
            return false;

        int firstPos = 0;
        int i = 0;
        int newI = 0;
        int curLoopNum = nums[firstPos] > 0 ? 1001 : -1001;

        while (firstPos < nums.length) {
            System.out.println(firstPos);
            if (
                (Math.abs(nums[firstPos]) > 1000 &&
                Math.abs(nums[firstPos]) < Math.abs(curLoopNum)) ||
                div(nums[firstPos], nums.length)
            )
            {
                firstPos += 1;
                i = firstPos;
                if (firstPos < nums.length)
                    curLoopNum = nums[firstPos] > 0 ?
                    Math.abs(curLoopNum) : -Math.abs(curLoopNum);
            }
            else {
                newI = mod(i + nums[i], nums.length);
                nums[i] = curLoopNum;

                if (nums[newI] == curLoopNum)
                    return true;
                else if (
                    nums[newI] > 1000 ||
                    nums[newI] < -1000 ||
                    nums[newI] * curLoopNum < 0 ||
                    div(nums[newI], nums.length))
                {

                    firstPos += 1;
                    i = firstPos;

                    if (curLoopNum > 0)
                        curLoopNum += 1;
                    else
                        curLoopNum -= 1;

                    if (firstPos < nums.length)
                        curLoopNum = nums[firstPos] > 0 ? Math.abs(curLoopNum) : -Math.abs(curLoopNum);

                }
                else
                    i = newI;


            }
        }

        return false;
    }


    private int mod (int a, int b) {
            return ((a % b) + b) % b;
    }
    private boolean div(int a, int b) {
        return (a / b) * b == a;
    }
}
