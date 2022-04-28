/* Дан двумерный массив A, размером (n*n). Найти сумму положительных элементов параллели побочной диагонали,
расположенной под диагональю (ниже побочной диагонали) */

import java.util.Random;

public class Positive {
    public static void main(String args[]) {

        int width = 5;
        int height = 5;
        int[][] matrix = new int[width][height];

        for (int i = 0; i < width; i++) {
            for (int j = 0; j < height; j++) {
                matrix[i][j] = new Random().nextInt(20) + (-10);
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }

        int sum = 0;
        for (int j = 1; j < height; j++) {
            for (int i = 1; i < width; i++) {
                if ((j == width - i) & (matrix[i][j] > 0)) {
                    sum += matrix[i][j];
                }
            }
        }
        System.out.println("Сумма элементов: " + sum);

    }
}
