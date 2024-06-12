package silver5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;

public class sortnumber_2 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());
        ArrayList<Integer> arr = new ArrayList<>();
        
        for (int i = 0; i < N; i++) {
            arr.add(Integer.parseInt(br.readLine()));
        }

        Collections.sort(arr);              // Timsort = 합병 및 삽입정렬 - O(n) ~ O(nlogn)
                                            // 합병 정렬 - O(nlogn) / 삽입정렬 - O(n) ~ O(n^2)
        for (int value : arr) {
            sb.append(value).append('\n');
        }
        System.out.println(sb);
    }
}
//public class sortnumber_2 {
//    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        StringBuilder sb = new StringBuilder();
//        int N = Integer.parseInt(br.readLine());
//        int[] arr = new int[N];
//
//        for (int i = 0; i < N; i++) {
//            int M = Integer.parseInt(br.readLine());
//            arr[i] = M;
//        }
//        int[] ans = bubbleSort(arr, N);
//        for (int j = 0; j < N; j++) {
//            System.out.println(ans[j]);
//        }
//    }
//
//
//    private static int[] bubbleSort(int[] arr, int N) {
//        int[] ans = arr;
//        for (int i = 1; i < N; i++) {
//            for (int j = 0; j < N-i; j++) {
//                if (arr[j] > arr[j + 1]) {
//                    swap(arr, j, j + 1);
//                }
//            }
//        }
//        return ans;
//    }
//
//    private static void swap(int[] a, int i, int j) {
//        int temp = a[i];
//        a[i] = a[j];
//        a[j] = temp;
//    }
//}
