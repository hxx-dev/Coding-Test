class Solution {
    public int solution(int n, int k) {
        int answer = 0;
        // 양꼬치 인분을 10으로 나눈 몫만큼 서비스
        int service = (n / 10) * 2000; 
        
        answer = n * 12000 + k * 2000 - service;
        
        return answer;
    }
}