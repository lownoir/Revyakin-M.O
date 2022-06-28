package Liter;

public class Directories extends Literature {
    private String direction;
    private int tom;
    private int part;

    public Directories(int code, String type, String name, int year, String namePublic, int numberPages, String writer, String direction, int tom, int part) {
        super(code, type, name, year, namePublic, numberPages, writer);
        this.direction = direction;
        this.tom = tom;
        this.part = part;
    }

    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }

    public int getTom() {
        return tom;
    }

    public void setTom(int tom) {
        this.tom = tom;
    }

    public int getPart() {
        return part;
    }

    public void setPart(int part) {
        this.part = part;
    }

    public String toString() {
        return "\n"+super.toString()+"\nНаправление - "+direction+"\nТом - "+tom+"\nЧасть - "+part+"\n";
    }
}
