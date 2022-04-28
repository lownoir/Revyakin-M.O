// Дан массив b (n). Переписать в массив C (n) положительные элементы массива b (n) умноженные на 5

import java.util.Random;

public class Focus {
    public static void main(String[] args) {

        int n = 10;
        int[] b = new int [n];

        for (int i = 0; i < b.length; i++) {
            b[i] = new Random().nextInt(40) + (-20);
            System.out.print(b[i] + " ");
        }
        System.out.println(" ");

        int new_size = 0;
        for (int k : b) {
            if (k > 0) {
                new_size++;
            }
        }

        int[] new_b = new int[new_size];
        n = 0;
        for (int j : b) {
            if (j > 0) {
                new_b[n] = j * 5;
                System.out.print(new_b[n] + " ");
                n++;
            }
        }

    }
}

