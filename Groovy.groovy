class GroovyTut {
 
// main is where execution starts
static void main(String[] args){
 
  // Print to the screen
  println("Hello World");
 
  // ---------- MATH ----------
  // Everything in Groovy is an object
  // including numbers
 
  // def is used when you define a variable
  // Variables start with a letter and can
  // contain numbers and _
  // Variables are cynamically typed and can
  // hold any value
  def age = "Dog";
  age = 40;
 
    // The basic integer math operators
  println("5 + 4 = " + (5 + 4));
  println("5 - 4 = " + (5 - 4));
  println("5 * 4 = " + (5 * 4));
  println("5 / 4 = " + (5.intdiv(4)));
  println("5 % 4 = " + (5 % 4));
  println("5 - 5 = " + (5.minus(5)));

  // Floating point math operators
  println("5.2 + 4.4 = " + (5.2.plus(4.4)));
  println("5.2 - 4.4 = " + (5.2.minus(4.4)));
  println("5.2 * 4.4 = " + (5.2.multiply(4.4)));
  println("5.2 / 4.4 = " + (5.2 / 4.4));
 
  // Order of operations
  println("3 + 2 * 5 = " + (3 + 2 * 5));
  println("(3 + 2) * 5 = " + ((3 + 2) * 5));
 
  // Increment and decrement
  println("age++ = " + (age++));
  println("++age = " + (++age));
  println("age-- = " + (age--));
  println("--age = " + (--age));
 
  // Largest values
  println("Biggest Int " + Integer.MAX_VALUE);
  println("Smallest Int " + Integer.MIN_VALUE);
 
  println("Biggest Float " + Float.MAX_VALUE);
  println("Smallest Float " + Float.MIN_VALUE);
 
  println("Biggest Double " + Double.MAX_VALUE);
  println("Smallest Double " + Double.MIN_VALUE);
 
  // Decimal Accuracy
  println("1.1000000000000001 + 1.1000000000000001 "
  + (1.1000000000000001111111111111111111111111111111111111 + 1.1000000000000001111111111111111111111111111111111111));
 
  // Math Functions
  def randNum = 2.0;
  println("Math.abs(-2.45) = " + (Math.abs(-2.45)));
  println("Math.round(2.45) = " + (Math.round(2.45)));
  println("randNum.pow(3) = " + (randNum.pow(3)));
  println("3.0.equals(2.0) = " + (3.0.equals(2.0)));
  println("randNum.equals(Float.NaN) = " + (randNum.equals(Float.NaN)));
  println("Math.sqrt(9) = " + (Math.sqrt(9)));
  println("Math.cbrt(27) = " + (Math.cbrt(27)));
  println("Math.ceil(2.45) = " + (Math.ceil(2.45)));
  println("Math.floor(2.45) = " + (Math.floor(2.45)));
  println("Math.min(2,3) = " + (Math.min(2,3)));
  println("Math.max(2,3) = " + (Math.max(2,3)));
 
  // Number to the power of e
  println("Math.log(2) = " + (Math.log(2)));
 
  // Base 10 logarithm
  println("Math.log10(2) = " + (Math.log10(2)));
 
  // Degrees and radians
  println("Math.toDegrees(Math.PI) = " + (Math.toDegrees(Math.PI)));
  println("Math.toRadians(90) = " + (Math.toRadians(90)));
 
  // sin, cos, tan, asin, acos, atan, sinh, cosh, tanh
  println("Math.sin(0.5 * Math.PI) = " + (Math.sin(0.5 * Math.PI)));
 
  // Generate random value from 1 to 100
  println("Math.abs(new Random().nextInt() % 100) + 1 = " + (Math.abs(new Random().nextInt() % 100) + 1));
 
  // ---------- STRINGS ----------
 
  def name = "Derek";
  name = "Champ";
  // A string surrounded by single quotes is taken literally
  // but backslashed characters are recognized
  println("I am ${name}\n");
  println('I am $name\n');
 
  // Triple quoted strings continue over many lines
  def multString = '''I am
  a string
  that goes on
  for many lines''';
 
  println(multString);
 
  // You can access a string by index
  println("3rd Index of Name " + name[3]);
  println("Index of r " + name.indexOf('r'));
 
  // You can also get a slice
  println("1st 3 Characters " + name[0..2]);
 
  // Get specific Characters
  println("Every Other Character " + name[0,2,4]);
 
  // Get characters starting at index
  println("Substring at 1 " + name.substring(1));
 
  // Get characters at index up to another
  println("Substring at 1 to 4 " + name.substring(1,4));
 
  // Concatenate strings
  println("My Name " + name);
  println("My Name ".concat(name));
 
  // Repeat a string
  def repeatStr = "What I said is " * 2;
  println(repeatStr);
 
  // Check for equality
  println("Derek == Derek : " + ('Derek'.equals('Derek')));
  println("Derek == derek : " + ('Derek'.equalsIgnoreCase('derek')));
 
  // Get length of string
  println("Size " + repeatStr.length());
 
  // Remove first occurance
  println(repeatStr - "What");
 
  // Split the string
  println(repeatStr.split(' '));
  println(repeatStr.toList());
 
  // Replace all strings
  println(repeatStr.replaceAll('I', 'she'));
 
  // Uppercase and lowercase
  println("Uppercase " + name.toUpperCase());
  println("Lowercase " + name.toLowerCase());
 
  // <=> returns -1 if 1st string is before 2nd
  // 1 if the opposite and 0 if equal
  println("Ant <=> Banana " + ('Ant' <=> 'Banana'));
  println("Banana <=> Ant " + ('Banana' <=> 'Ant'));
  println("Ant <=> Ant " + ('Ant' <=> 'Ant'));
 
  // ---------- OUTPUT ----------
  // With double quotes we can insert variables
  def randString = "Random";
  println("A $randString string");
 
  // You can do the same thing with printf
  printf("A %s string \n", randString);
 
  // Use multiple values
  printf("%-10s %d %.2f %10s \n", ['Stuff', 10, 1.234, 'Random']);
 
  /*
 
  // ---------- INPUT ----------
  print("Whats your name ");
  def fName = System.console().readLine();
  println("Hello " + fName);
 
  // You must cast to the right value
  // toInteger, toDouble
  print("Enter a number ");
  def num1 = System.console().readLine().toDouble();
  print("Enter another ");
  def num2 = System.console().readLine().toDouble();
  printf("%.2f + %.2f = %.2f \n", [num1, num2, (num1 + num2)]);
 
  */
 
  // ---------- LISTS ----------
  // Lists hold a list of objects with an index
 
  def primes = [2,3,5,7,11,13];
 
  // Get a value at an index
  println("2nd Prime " + primes[1]);
  println("3rd Prime " + primes.get(2));
 
  // They can hold anything
  def employee = ['Derek', 40, 6.25, [1,2,3]];
 
  println("2nd Number " + employee[3][1]);
 
  // Get the length
  println("Length " + primes.size());
 
  // Add an index
  primes.add(17);
 
  // Append to the right
  primes<<19;
  primes.add(23);
 
  // Concatenate 2 Lists
  primes + [29,31];
 
  // Remove the last item
  primes - [31];
 
  // Check if empty
  println("Is empty " + primes.isEmpty());
 
  // Get 1st 3
  println("1st 3 " + primes[0..2]);
 
  println(primes);
 
  // Get matches
  println("Matches " + primes.intersect([2,3,7]));
 
  // Reverse
  println("Reverse " + primes.reverse());
 
  // Sorted
  println("Sorted " + primes.sort());
 
  // Pop last item
  println("Last " + primes.pop());
 
  // ---------- MAPS ----------
  // List of objects with keys versus indexes
 
  def paulMap = [
    'name' : 'Paul',
    'age' : 35,
    'address' : '123 Main St',
    'list' : [1,2,3]
  ];
 
  // Access with key
  println("Name " + paulMap['name']);
  println("Age " + paulMap.get('age'));
  println("List Item " + paulMap['list'][1]);
 
  // Add key value
  paulMap.put('city', 'Pittsburgh');
 
  // Check for key
  println("Has City " + paulMap.containsKey('city'));
 
  // Size
  println("Size " + paulMap.size());

  def greeting = "GoodBye";

  def tellGoodBye = {uName -> println("$greeting $uName")}

  tellGoodBye("Champ");

  def getFactorial = { num -> (num <= 1) ? 1 : num * call(num - 1) }
  println("Factorial 4 : " + getFactorial(8));

  def nameList = ['Doug', 'Sally', 'Sue', 'Champ'];
  def matchEle = nameList.find {item -> item == 'Champ'}
  println(matchEle);

  def randNumList = [1,4,5,4,6,7,8];

  def employees = [
    'Paul' : 34,
    'Sally' : 35,
    'Sam' : 36,
    'Champ' : 38,
    'Nicole' : 39
  ];
 
  employees.each { println("${it.key} : ${it.value}"); }
  }
}