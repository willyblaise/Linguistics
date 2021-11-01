// Import data types for testing
use std::{i8, i16, i32, i64, u8, u16, u32, u64, isize, usize, f32, f64};

use std::io::stdin;


fn main(){

    println!("Enter total: ");


    let mut name = String::new();
    let mut months = String::new();

    //reading in value from keyboard
    stdin().read_line(&mut name);

    //convert keyboard input to integer
    let num: i32 = name.trim().parse().expect("what");

    println!("How many months for pay off?");

    //reading in value from keyboard
    stdin().read_line(&mut months);

    //convert keyboard input to integer
    let months: i32 = months.trim().parse().expect("number of months to pay off");

    //cast int to float
    println!("Total after tax = {}", sales_tax(num as f32));

    println!("Monthly installments over {} months = {}", months, installments(num, months));

    let mut fact = factorial(5);

    println!("Factorial of 5 = {}", fact);

    println!("Factorial of 4 = {}", factorial2(4));

//    'outer: loop {

        let mnum: i32 = 22;
        println!("Enter a numba: ");

        loop {

                let mut line = String::new();
                let input = stdin().read_line(&mut line);

                let guess: Option<i32> = input.ok().map_or(None, |_| line.trim().parse().ok());

                match guess {
                    None => println!("Enter a number: "),
                    Some(n) if n == mnum => {
                        println!("{} is the magic number.", n);
                        break;
                    }
                    Some(n) if n > mnum => println!("This number is larger"),
                    Some(n) if n < mnum => println!("This number is less than"),
                    Some(_) => println!("Error")
                }

        }

        let mut subtotal: f32 = 3000.00;

        //binding variable to method
        let tax = sales_tax;

        println!("{} + tax = {}", subtotal, tax(subtotal));

        //below is a Closure which is an alternative to writing a function
        let add = |a: i32, b: i32| a + b;

        println!("111 + 222 = {}", add(111,222));

}

fn sales_tax(total: f32) -> f32 {
    return total * 1.0825;

}

fn installments(size: i32, time: i32)-> i32 {
    return size / time;
}

fn factorial(i: u64) -> u64 {
    match i {
        0 => 1,
        n => n * factorial(n-1)
    }

}

fn factorial2(i: u64) -> u64 {
    (2..=i).product()
}
