   
   // CarBuilder class
    public class CarBuilder {
        private String brand;
        private String model;
        private int year = 2023; // Default value
        private String color = "Black"; // Default value
        private int horsePower = 150; // Default value

        public CarBuilder setBrand(String brand) {
            this.brand = brand;
            return this;
        }

        public CarBuilder setModel(String model) {
            this.model = model;
            return this;
        }

        public CarBuilder setYear(int year) {
            this.year = year;
            return this;
        }

        public CarBuilder setColor(String color) {
            this.color = color;
            return this;
        }

        public CarBuilder setHorsePower(int horsePower) {
            this.horsePower = horsePower;
            return this;
        }

        public Car build() {
            // Validation or handling of default values can be added here
            return new Car(brand, model, year, color, horsePower);
        }
    }