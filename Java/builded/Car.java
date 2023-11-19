public class Car {
    private String brand;
    private String model;
    private int year;
    private String color;
    private int horsePower;



    public Car(String brand, String model, int year, String color, int horsePower) {
        this.brand = brand;
        this.model = model;
        this.year = year;
        this.color = color;
        this.horsePower = horsePower;
    }

    // Getters
    public String getBrand() {
        return this.brand;
    }

    public void setBrand(String brand) {
        this.brand = brand;
    }

    public String getModel() {
        return this.model;
    }

    public void setModel(String model) {
        this.model = model;
    }

    public int getYear() {
        return this.year;
    }

    public void setYear(int year) {
        this.year = year;
    }

    public String getColor() {
        return this.color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public int getHorsePower() {
        return this.horsePower;
    }

    public void setHorsePower(int horsePower) {
        this.horsePower = horsePower;
    }
    
}
