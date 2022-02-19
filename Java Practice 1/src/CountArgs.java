public class CountArgs {
    public static void main(String[] args) {
        int count = 0;
        for (int i = 0; i < args.length; i++) {
            count++;
        }
        if (count > 0) {
            System.out.println("Вы ввели " + count + " параметров");
        }
        else {
            System.out.println("Вы не передавали параметров");
        }
    }
}

// Написать программу получающую на вход в качестве аргумента несколько параметров. В программе вывести "Вы ввели" + N
// (количество параметров) + "параметров". Если параметры не передвавались, вывести "Вы не передавали параметров".
