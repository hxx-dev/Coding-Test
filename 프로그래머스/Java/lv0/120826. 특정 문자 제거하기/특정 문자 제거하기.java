class Solution {
    public String solution(String myString, String letter) {
        String answer = "";
        //.split -> 배열로
        String[] myStringArr = myString.split("");
        for(int i = 0 ; i < myStringArr.length ; i++){
            //.equals -> false면 answer에 해당 문자 추가
            if(!myStringArr[i].equals(letter)){
                answer += myStringArr[i];
            }
        }
        return answer;
    }
}