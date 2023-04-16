package properties;

import java.util.*;


public class People {


	public String firstName = null;
	public String lastName = null;
	public int age = 0;
	public boolean family = false;
	public String employer = null;


	public People() {

	}

	public People(String fname, String lname, int age, boolean hasFamily, String employer) {
		this.firstName = fname;
		this.lastName = lname;
		this.age = age;
		this.family = hasFamily;
		this.employer = employer;

	}


	public String getFirstName() {
		return this.firstName;
	}

	public void setFirstName(String fname) {
		this.firstName = fname;
	}

	public String getLastName() {
		return this.lastName;
	}

	public void setLastName(String lname) {
		this.lastName = lname;
	}

	public int getAge() {
		return this.age;
	}

	public void setAge(int age) {
		this.age = age;
	}

	public boolean getFamily() {
		return this.family;
	}
	public void setFamily(boolean hasFamily) {
		this.family = hasFamily;
	}

	public String getEmployer() {
		return this.employer;
	}

	public void setEmployer(String employer) {
		this.employer = employer;
	}





}
