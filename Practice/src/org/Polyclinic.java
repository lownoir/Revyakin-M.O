// Название поликлиники, адрес, фамилия пациента, номер полиса, дата осмотра, фамилия врача, должность врача, диагноз

package org;

public class Polyclinic {

    public static void main(String[] args) {

        Data Data = new Data("Андрей", "Путилина, д. 125", "Зубко", 30670899, "12.11.2002", "Реченко", "Хирург", "Грыжа");
        System.out.println(Data);

    }

}
