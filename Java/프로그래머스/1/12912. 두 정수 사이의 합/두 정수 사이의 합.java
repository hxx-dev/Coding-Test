class Solution {
    public long solution(int a, int b) {
        long answer = 0;
        if(b > a){
            for(int i = a ; i < b + 1 ; i++){
                answer += i;
            }
        }
        else{
            for(int i = b ; i < a + 1 ; i ++){
                answer += i;
            }
        }
        
        return answer;
    }
}
// a, b의 대소관계가 정해져 있지 않기 때문에 조건문으로 나누고, 반복문으로 계속 더 함