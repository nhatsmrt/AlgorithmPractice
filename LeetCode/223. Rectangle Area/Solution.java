class Solution {
    public int computeAreaRectangle(int A, int B, int C, int D) {
        return (C - A) * (D - B);
    }
    public int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        int areaI = computeAreaRectangle(A, B, C, D);
        int areaII = computeAreaRectangle(E, F, G, H);

        int M = A > E ? A : E;
        int N = B > F ? B : F;
        int P = C < G ? C : G;
        int Q = D < H ? D : H;

        if (M > P || N > Q)
            return areaI + areaII;
        else
            return areaI + areaII - computeAreaRectangle(M, N, P, Q);
    }
}
