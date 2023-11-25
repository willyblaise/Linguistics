public class Division implements MathOperation {
   @Override
   public int operate(int a, int b) {
        
    if (b != 0) {
        return a / b;
    } else {
        throw new ArithmeticException("Cannot Divide by Zero....");
    }

   } 
}
