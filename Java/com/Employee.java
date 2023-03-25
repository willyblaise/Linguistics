import java.util.*;


public class Employee {

	public static void main(String[] args) {

		EmployeeRecord employee = new EmployeeRecord("Champ", 2673);
		System.out.println("Employee name: " + employee.getName());
		System.out.println("Employee number: " + employee.getEmployeeNumber());
	}
}
