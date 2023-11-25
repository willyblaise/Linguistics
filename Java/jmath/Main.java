public class Main {
    public static void main(String[] args) {
        // Create an instance of the Calculator class
        Calculator calculator = new Calculator();

        // Add supported operations to the calculator
        calculator.addOperation("add", new Addition());
        calculator.addOperation("subtract", new Subtraction());
        calculator.addOperation("multiply", new Multiplication());
        calculator.addOperation("divide", new Division());
        calculator.addOperation("mod", new Modulus());

        // Use the calculator to perform operations
        int resultAddition = calculator.calculate("add", 5, 3);
        int resultSubtraction = calculator.calculate("subtract", 8, 2);
        int resultMultiplication = calculator.calculate("multiply", 10, 55);
        int resultDivision = calculator.calculate("divide", 100, 9);
        int resultModulus = calculator.calculate("mod", 25, 9);
        
        // Display the results
        System.out.println("Result of addition: " + resultAddition);
        System.out.println("Result of subtraction: " + resultSubtraction);
        System.out.println("Result of multiplication: " + resultMultiplication);
        System.out.println("Result of division: " + resultDivision);
        System.out.println("Results of remainder: " + resultModulus);

    }
}
