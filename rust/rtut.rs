// Import data types for testing
use std::{i8, i16, i32, i64, u8, u16, u32, u64, isize, usize, f32, f64};

use std::io::stdin;

// The main function executes when you run the program
fn main() {

    // This macro prints to the screen
    println!("Hello World");

    // let defines a variable
    // The data type will be guessed if not provided
    // Variable values are immutable (Can't change)
    let num = 10;

    // Define a 32 bit mutable integer
    let mut age: i32 = 30;

    // There are many number types i8, i16, i32,
    // i64, u8, u16, u32, u64, isize, usize, f32, f64

    println!("Max i8 {}", i8::MAX);
    println!("Min i8 {}", i8::MIN);
    println!("Max i16 {}", i16::MAX);
    println!("Min i16 {}", i16::MIN);
    println!("Max i32 {}", i32::MAX);
    println!("Min i32 {}", i32::MIN);
    println!("Max i64 {}", i64::MAX);
    println!("Min i64 {}", i64::MIN);
    println!("Max isize {}", isize::MAX);
    println!("Min isize {}", isize::MIN);
    println!("Max usize {}", usize::MAX);
    println!("Min usize {}", usize::MIN);
    println!("Max f32 {}", f32::MAX);
    println!("Min f32 {}", f32::MIN);
    println!("Max f64 {}", f64::MAX);
    println!("Min f64 {}", f64::MIN);

    // ---------- MATH ----------
    println!("5 + 4 = {}", 5 + 4);
    println!("5 - 4 = {}", 5 - 4);
    println!("5 * 4 = {}", 5 * 4);
    println!("5 / 4 = {}", 5 / 4);
    println!("5 % 4 = {}", 5 % 4);

    let mut neg_4 = -4i32;

    println!("abs(-4) = {}", neg_4.abs());
    println!("4 ^ 6 = {}", 4i32.pow(6));
    println!("sqrt 9 = {}", 9f64.sqrt());
    println!("cbrt 9 = {}", 27f64.cbrt());
    println!("Round 1.45 = {}", 1.45f64.round());
    println!("Floor 1.45 = {}", 1.45f64.floor());
    println!("Ceiling 1.45 = {}", 1.45f64.ceil());
    println!("e ^ 2 = {}", 2f64.exp());
    println!("log(2) = {}", 2f64.ln());
    println!("log10(2) = {}", 2f64.log10());
    println!("90 to Radians = {}", 90f64.to_radians());
    println!("PI to Degrees = {}", 3.14f64.to_degrees());
    println!("Max 4, 5 = {}", 4f64.max(5f64));
    println!("Min 4, 5 = {}", 4f64.min(5f64));

    // sin, cos, tan, asin, acos, atan, atan2, sinh,
    // cosh, tanh
    println!("Sin 3.14 = {}", 3.14f64.sin());

    // ---------- CONDITIONALS ----------
    //

    let age_old = 6;

    if (age_old == 5) {
        println!("Go to kindergarten");
    } else if (age_old > 5) && (age_old <= 18){
        println!("Go to grade {}", (age_old - 5));
    } else if (age_old <= 25) && (age_old > 18) {
        println!("Go to college");
    } else {
        println!("Do what you want");
    }

    let mut a: i32 = 1;

    loop {
        if a % 2 == 0 {
            println!("a = {}", a);
            a += 1;

            continue;
        }
        a += 1;

        if a == 2000000 {
            break;
        }
   }


}
