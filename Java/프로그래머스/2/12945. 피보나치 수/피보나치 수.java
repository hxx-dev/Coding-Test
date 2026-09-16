class Solution {
    public int solution(int n) {
        int prev = 0;  // F(i-2)
        int curr = 1;  // F(i-1)

        for (int i = 2; i <= n; i++) {
            int next = (prev + curr) % 1234567; // 오버플로우 방지
            prev = curr; // 한 칸 씩
            curr = next; // 이동
        }

        return curr;
    }
}