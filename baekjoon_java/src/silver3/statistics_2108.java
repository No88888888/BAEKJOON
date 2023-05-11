package silver3;

import java.util.*;
import java.util.stream.Collectors;

public class statistics_2108 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);    // 스캐너로 한줄씩 읽는다
        int N = sc.nextInt();
        int[] arr = new int[N];                 // N개 요소 배열 선언
        int summ = 0;                           // 전체 합 구할 summ
        int max = Integer.MIN_VALUE;            // 최대값 max
        int min = Integer.MAX_VALUE;            // 최소값 min
        int choibinmax = 1;                     // 최빈값이 나온 횟수 구할 변수
        Map<Integer, Integer> choibin = new HashMap<>();    // 정수들 나온 횟수 기록할 map

        for (int i = 0; i < N; i++) {
            int a = sc.nextInt();

            if (choibin.get(a) == null) {       // 한번도 나온적 없는 정수면
                choibin.put(a, 1);              // 새로 map에 저장
            } else {                            // 아니라면
                choibin.put(a, choibin.get(a) + 1); // 기존 횟수에 1 더함
                if (choibin.get(a) > choibinmax) {  // 방금 나온 숫자 등장횟수가 최빈값 나온 획수 최대값보다 크다면
                    choibinmax = choibin.get(a);    // 그 수를 최빈값 최대값으로 저장
                }
            }

            if (a > max) {                      // 지금 숫자가 최대값보다 크다면 최대값에 저장
                max = a;
            }

            if (a < min) {                      // 지금 숫자가 최소값보다 작다면 최소값에 저장
                min = a;
            }

            summ += a;                          // 누적합에 더함
            arr[i] = a;                         // 배열에 저장

        }
        Arrays.sort(arr);                       // 배열 정렬
        int midd = arr[N / 2];                  // 중간값은 배열의 중간 인덱스의 값
        float sansul = (float) summ / N;        // 산술평균은 소숫점 첫쨰자리에서 반올림이기 떄문에 float로 형변환하여 계산
        int chai = max - min;                   // 최대값과 최솟값의 차이 저장

        List<Integer> keys = new ArrayList<>(); // 최빈값을 구할 배열
        for (Map.Entry<Integer, Integer> entry : choibin.entrySet()) { //choibin map의 키-값 쌍을 가져와서
            if (Objects.equals(choibinmax, entry.getValue())) { // 값이 choibinmax와 같다면
                keys.add(entry.getKey());                       // 그 키값을 keys배열에 저장
            }
        }

        int maxKey = 0;
        if (keys.size() != 1) {         // 최빈값이 2개 이상이면
            Collections.sort(keys);     // 정렬 후
            maxKey = keys.get(1);       // 2번떄로 작은 값 가져온다
        } else {                        // 1개라면
            maxKey = keys.get(0);       // 해당 값 가져온다
        }
        System.out.println(Math.round(sansul));
        System.out.println(midd);
        System.out.println(maxKey);
        System.out.println(chai);
    }
}
