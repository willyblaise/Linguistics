// Import data types for testing
use std::{i8, i16, i32, i64, u8, u16, u32, u64, isize, usize, f32, f64};

use std::io::stdin;


fn main(){

    println!("Enter total: ");

    let mut name = String::new();
    stdin().read_line(&mut name);

    //convert input to integer
    let num: i32 = name.trim().parse().expect("what");

    //cast int to float
    println!("Total after tax = {}", sales_tax(num as f32));

    println!("Monthly installments = {}", installments(num));
}

fn sales_tax(total: f32) -> f32 {
    return total * 1.0825;

}

fn installments(size: i32)-> i32 {
    return size / 12;
}
