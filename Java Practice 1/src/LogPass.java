import java.util.Objects;

public class LogPass {
    public static void main(String[] args) {
        String correct_login = "qwerty";
        String correct_pass = "123456";
        if ((Objects.equals(args[0], correct_login)) & (Objects.equals(args[1], correct_pass))) {
            System.out.println("Вас узнали. Добро пожаловать");
        }
        else {
            System.out.println("Логин и пароль не распознаны. Доступ запрещён");
        }
    }
}

// Ввести в качестве параметров имя пользователя и пароль. Проверить в методе main() соответствие введенных значений
// заранее определенным значениям. В случае полного соответствия вывести сообщение "Вас узнали. Добро пожаловать",
// в противном случае вывести сообщение "Логин и пароль не распознаны. Доступ запрещен"