// Import data types for testing
use std::{i8, i16, i32, i64, u8, u16, u32, u64, isize, usize, f32, f64};

use std::io::stdin;


fn main(){


    println!("Enter total for the Product/Service: ");

    let mut amount = String::new();
    stdin().read_line(&mut amount);

    //convert input to integer
    let num: i32 = amount.trim().parse().expect("what");

    println!("Enter length of time to pay off: ");

    let mut time = String::new();
    stdin().read_line(&mut time);

    //convert input to integer
    let tl: i32 = time.trim().parse().expect("what");

    //cast int to float
    println!("Total after tax = {:.2}", sales_tax(num as f32));

    let mut monthly_payments = installments(num, tl);

    println!("Monthly installments = {:.2}", monthly_payments as f32);

}

fn sales_tax(total: f32) -> f32 {
    return total * 1.0825;

}

fn installments(amount: i32, length: i32) -> f32 {
    return amount as f32 / length as f32;
}
