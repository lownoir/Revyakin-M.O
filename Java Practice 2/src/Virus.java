/* Определить матрицу (двумерный массив) и ее заполнить случайными значениями. Построить вектор B, который возвращает
количество положительных элементов в каждом столбце матрицы */

import java.util.Random;
import java.util.Vector;

public class Virus {
    public static void main(String args[]) {

        int height = 5;
        int width = 5;
        int[][] matrix = new int[width][height];
        Vector B = new Vector();

        for (int i = 0; i < width; i++) {
            for (int j = 0; j < height; j++) {
                matrix[i][j] = new Random().nextInt(20) + (-10);
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }

        for (int i = 0; i < height; i++) {
            B.clear();
            for (int j = 0; j < width; j++) {
                if (matrix[j][i] > 0) {
                    B.add(1);
                }
            }
            System.out.println("Количество положительных элементов в " + (i + 1) + " столбце: " + B.size());
        }

    }
}
