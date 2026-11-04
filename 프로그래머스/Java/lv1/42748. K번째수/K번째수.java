import java.util.Arrays;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        
        for(int n = 0 ; n < commands.length ; n++){
            int i = commands[n][0]; // 시작
            int j = commands[n][1]; // 종료
            int k = commands[n][2]; // 몇 번째
            
            int[] copyArray = Arrays.copyOfRange(array, i - 1, j);
            // i - 1 => 인덱스는 0부터, 시작 포함 끝 미포함
            Arrays.sort(copyArray);
            answer[n] = copyArray[k - 1]; //마찬가지로 k번째는 인덱스 k-1
        }
        
        return answer;
    }
}