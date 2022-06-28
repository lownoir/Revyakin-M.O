package Liter;
import java.util.ArrayList;

public class Constructor {
    public static void main(String[] args) {
        ArrayList<Literature> fileOfLiterature = new ArrayList<>();
        Main allBooks = new Main(fileOfLiterature);

        int bookCode = 1;
        String bookType = "Компьютерный";
        String bookName = "JS для начинающих";
        int bookYear = 2021;
        String bookNamePublic = "JetBrains";
        int bookNumberPages = 234;
        String bookWriter = "Лиам";
        String bookFieldScience = "Научная";
        int bookNumberInstances = 5647;
        SciTechLiterature bookJS = new SciTechLiterature(bookCode, bookType, bookName, bookYear, bookNamePublic, bookNumberPages, bookWriter, bookFieldScience, bookNumberInstances);

        allBooks.addLiterature(bookJS);

        int book1Code = 2;
        String book1Type = "Компьютерный";
        String book1Name = "Java для начинающих";
        int book1Year = 2021;
        String book1NamePublic = "JetBrains";
        int book1NumberPages = 267;
        String book1Writer = "Лиам";
        String book1TypePeriodicals = "Ежегодная";
        String book1PeriodPublishing = "С 2010 по настоящее время";
        Periodicals bookJava = new Periodicals(book1Code, book1Type, book1Name, book1Year, book1NamePublic, book1NumberPages, book1Writer, book1TypePeriodicals, book1PeriodPublishing);

        allBooks.addLiterature(bookJava);

        int bookPythonCode = 3;
        String bookPythonType = "Компьютерный";
        String bookPythonName = "Python для начинающих";
        int bookPythonYear = 2008;
        String bookPythonNamePublic = "JetBrains";
        int bookPythonNumberPages = 279;
        String bookPythonWriter = "Конел";
        String bookPythonDirection = "Научная";
        int bookPythonTom = 2;
        int bookPythonPart = 1;
        Directories bookPython = new Directories(bookPythonCode, bookPythonType, bookPythonName, bookPythonYear, bookPythonNamePublic, bookPythonNumberPages, bookPythonWriter, bookPythonDirection, bookPythonTom, bookPythonPart);

        allBooks.addLiterature(bookPython);

        System.out.println(allBooks.ToLiterature());
    }
}
