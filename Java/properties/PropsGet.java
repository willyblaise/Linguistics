package properties;


import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;

public class PropsGet {

    public static void main(String[] args) {

	People p = new People("Willy", "Pix", 42, true, "Pix Transport");
	People q = new People();

	q = p;


        try (InputStream input = new FileInputStream("/home/champ/code/Linguistics/Java/properties/db.properties")) {

            Properties prop = new Properties();

            // load a properties file
            prop.load(input);

            // get the property value and print it out
            System.out.println(prop.getProperty("db.url"));
            System.out.println(prop.getProperty("db.user"));
            System.out.println(prop.getProperty("db.password"));
            System.out.println(prop.getProperty("db.user2"));
            System.out.println(p.getFirstName());
            System.out.println("This is the name from q: " + q.getLastName());



        } catch (IOException ex) {
            ex.printStackTrace();
        }

    }

}
