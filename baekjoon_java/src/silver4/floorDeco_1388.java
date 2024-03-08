package silver4;

/* 문제
형택이는 건축가이다. 지금 막 형택이는 형택이의 남자 친구 기훈이의 집을 막 완성시켰다. 형택이는 기훈이 방의 바닥 장식을 디자인했고, 이제 몇 개의 나무 판자가 필요한지 궁금해졌다. 나무 판자는 크기 1의 너비를 가졌고, 양수의 길이를 가지고 있다. 기훈이 방은 직사각형 모양이고, 방 안에는 벽과 평행한 모양의 정사각형으로 나누어져 있다.

이제 ‘-’와 ‘|’로 이루어진 바닥 장식 모양이 주어진다. 만약 두 개의 ‘-’가 인접해 있고, 같은 행에 있다면, 두 개는 같은 나무 판자이고, 두 개의 ‘|’가 인접해 있고, 같은 열에 있다면, 두 개는 같은 나무 판자이다.

기훈이의 방 바닥을 장식하는데 필요한 나무 판자의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 방 바닥의 세로 크기N과 가로 크기 M이 주어진다. 둘째 줄부터 N개의 줄에 M개의 문자가 주어진다. 이것은 바닥 장식 모양이고, '-‘와 ’|‘로만 이루어져 있다. N과 M은 50 이하인 자연수이다.

출력
첫째 줄에 문제의 정답을 출력한다. */

import java.io.*;
import java.util.*;

public class floorDeco_1388 {
    static int N, M;
    static int num = 0;
    static char tiles[][];
    static int visited[][];
    static int[][] dir = {{0,1}, {1,0}};
    
    static void checkTile(int x, int y) {
        int dx, dy;
        if (tiles[x][y] == '-') {
            dx = dir[0][0];
            dy = dir[0][1];
        } else {
            dx = dir[1][0];
            dy = dir[1][1];
        }
        int nx = x + dx;
        int ny = y + dy;
        while (nx<N && ny<M && tiles[x][y] == tiles[nx][ny]) {
            visited[nx][ny] = 1;
            nx = nx + dx;
            ny = ny + dy;
        }
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        
        tiles = new char[N][M];
        for (int i=0; i<N; i++) {
            String temp = br.readLine();
            char[] tempArray = temp.toCharArray();
            tiles[i] = tempArray;
        }
        visited = new int[N][M];
        
        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                if (visited[i][j] == 0) {
                    visited[i][j] = 1;
                    checkTile(i, j);
                    num++;
                }
            }
        }
        System.out.println(num);
    }
        
}