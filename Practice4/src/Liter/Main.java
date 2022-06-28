package Liter;
import java.util.ArrayList;

public class Main {
    private ArrayList<Literature> fileOfLiterature;
    public Main(ArrayList<Literature> ListOfLiterature){
        this.fileOfLiterature = ListOfLiterature;
    }

    public void addLiterature(Literature literature){
        fileOfLiterature.add(literature);
    }

    public ArrayList<Literature> ToLiterature(){
        return fileOfLiterature;
    }
}
