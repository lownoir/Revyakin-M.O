/* Дан массив b(n). Переписать в массив C(n) корни квадратные из положительных элементов массива b(n) деленные на 5.
Затем упорядочить методом "выбора и перестановки" по возрастанию новый массив */

import java.util.Random;

public class Lonely {
    public static void main(String args[]) {

        int n = 10;
        int[] b = new int[n];

        for (int i = 0; i < b.length; i++) {
            b[i] = new Random().nextInt(40) + (-20);
            System.out.print(b[i] + " ");
        }
        System.out.println();

        int new_size = 0;
        for (int q : b) {
            if (q > 0) {
                new_size++;
            }
        }

        double[] new_b = new double[new_size];
        n = 0;
        for (int w : b) {
            if (w > 0) {
                new_b[n] = Math.sqrt(w) / 5;
                System.out.print(new_b[n] + "   ");
                n++;
            }
        }
        System.out.println();

        for (int i = 0; i < new_b.length; i++) {
            int pos = i;
            double min = new_b[i];
            for (int j = i + 1; j < new_b.length; j++) {
                if (new_b[j] <= min) {
                    pos = j;
                    min = new_b[j];
                }
            }
            new_b[pos] = new_b[i];
            new_b[i] = min;
            System.out.print(new_b[i] + "   ");
        }

    }
}
