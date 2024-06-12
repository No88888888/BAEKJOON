package silver4;

import java.io.*;
import java.util.*;

public class treasure {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(new InputStreamReader(System.in));
        int N = sc.nextInt();
        Integer[] A = new Integer[N];
        int[] B = new int[N];
        for (int i=0; i<N; i++) {
            A[i] = sc.nextInt();
        }
        for (int i=0; i<N; i++) {
            B[i] = sc.nextInt();
        }
        HashMap<Integer, Integer> Bmap = new HashMap<>(N); 
        for (int i=0; i<N; i++) {
            Bmap.put(B[i], i);
        }
        Arrays.sort(A, Collections.reverseOrder());
        int[] sortedB = Arrays.copyOf(B, B.length);
        Arrays.sort(sortedB);
        int[] result = new int[N];
        System.out.println(Arrays.toString(A));
        System.out.println(Arrays.toString(sortedB));
        System.out.println(Bmap);
        for (int i=0; i<N; i++) {
            result[Bmap.get(sortedB[i])] = A[i];
        }
        System.out.println(Arrays.toString(result));
        int res = 0;
        for (int i=0; i<N; i++) {
            res += result[i]*B[i];
        }
        System.out.println(res);
    }
}