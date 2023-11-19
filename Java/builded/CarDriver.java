
public class CarDriver {
    

    public static void main(String[] args) {
        Car car1 = new CarBuilder()
        .setBrand("Volkswagen")
        .setModel("Toareg")
        .setYear(2016)
        .setHorsePower(276)
        .build();

        Car car2 = new CarBuilder()
        .setBrand("GMC")
        .setModel("Yukon")
        .setYear(2021)
        .setColor("Pearl White")
        .setHorsePower(376)
        .build();

        printInfo(car1);

        printInfo(car2);
    }

    public static void printInfo(Car car) {
        System.out.println("Brand: " + car.getBrand());
        System.out.println("Model: " + car.getModel());
        System.out.println("Year: " + car.getYear());
        System.out.println("Color: " + car.getColor());
        System.out.println("Horse Power: " + car.getHorsePower() + "\n");
    }
}
