package bronze1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class SortNumber3_10989 {

    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int num = Integer.parseInt(br.readLine());
        int[] n = new int[num];
        StringBuilder sb = new StringBuilder();

        for(int i = 0 ; i < n.length ; i++) {
            n[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(n);

        for(int i = 0 ; i < num ; i ++)
            sb.append(n[i]).append("\n");

        System.out.println(sb);
    }
}
