class Solution {
    public int solution(int n) {
        int answer = 0;
        
        if(n % 7 == 0){
            n /= 7;
            answer = n;
        }
        else{
            n /= 7;
            answer = n + 1;
        }
        
        return answer;
    }
}