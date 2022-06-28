package org;

public class Data {

    private String name;
    private String direction;
    private String patient_ln;
    private int policy_number;
    private String date_inspection;
    private String doctor_ln;
    private String doctor_post;
    private String diagnose;

    public Data(String name, String direction, String patient_ln, int policy_number, String date_inspection, String doctor_ln, String doctor_post, String diagnose) {

        this.name = name;
        this.direction = direction;
        this.patient_ln = patient_ln;
        this.policy_number = policy_number;
        this.date_inspection = date_inspection;
        this.doctor_ln = doctor_ln;
        this.doctor_post = doctor_post;
        this.diagnose = diagnose;
    }

    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }

    public String getDirection() {
        return direction;
    }
    public void setDirection(String direction) {
        this.direction = direction;
    }

    public String getPatient_ln() {
        return patient_ln;
    }
    public void setPatient_ln(String patient_ln) {
        this.patient_ln = patient_ln;
    }

    public int getPolicy_number() {
        return policy_number;
    }
    public void setPolicy_number(int policy_number) {
        this.policy_number = policy_number;
    }

    public String getDate_inspection() {
        return date_inspection;
    }
    public void setDate_inspection(String date_inspection) {
        this.date_inspection = date_inspection;
    }

    public String getDoctor_ln() {
        return doctor_ln;
    }
    public void setDoctor_ln(String doctor_ln) {
        this.doctor_ln = doctor_ln;
    }

    public String getDoctor_post() {
        return doctor_post;
    }
    public void setDoctor_post(String doctor_post) {
        this.doctor_post = doctor_post;
    }

    public String getDiagnose() {
        return diagnose;
    }
    public void setDiagnose(String diagnose) {
        this.diagnose = diagnose;
    }

    public String toString() {
        return "Название поликлиники - "+name+"\nАдрес поликлиники - "+direction+"\nФамилия пациента - "+patient_ln+"\nНомер полис - "+policy_number+"\nДата осмотра - "+date_inspection+"";
    }
}
