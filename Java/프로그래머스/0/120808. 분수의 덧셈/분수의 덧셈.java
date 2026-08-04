class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
      
        int numer = numer1 * denom2 + numer2 * denom1;
        int denom = denom1 * denom2;
        
        //유클리드 호제법
        //두 수를 나눈 나머지가 0이 될 때까지 나머지로 분모를 나눔
        //나머지가 0일 때 분모가 최대공약수
        int tmp1 = numer;
        int tmp2 = denom;
        int gcd;
        while(true){
            gcd = tmp1 % tmp2;
            if(gcd == 0){
                gcd = tmp2;
                break;
            }
            tmp1 = tmp2;
            tmp2 = gcd;
        }
        numer /= gcd;
        denom /= gcd;
        
        int[] answer = {numer, denom};
        
        return answer;
    }
}