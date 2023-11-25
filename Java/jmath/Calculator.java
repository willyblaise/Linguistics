import java.util.HashMap;
import java.util.Map;

// Calculator class using the Open/Closed Principle
public class Calculator {
    private Map<String, MathOperation> operations = new HashMap<>();

    // Add supported operations to the calculator
    public void addOperation(String operationName, MathOperation operation) {
        operations.put(operationName, operation);
    }

    // Calculate using a specific operation
    public int calculate(String operationName, int x, int y) {
        MathOperation operation = operations.get(operationName);
        if (operation != null) {
            return operation.operate(x, y);
        } else {
            throw new IllegalArgumentException("Operation '" + operationName + "' not supported.");
        }
    }
}