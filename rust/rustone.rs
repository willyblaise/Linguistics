// Import data types for testing
use std::{i8, i16, i32, i64, u8, u16, u32, u64, isize, usize, f32, f64};

//use std::io::stdin;

fn main(){

    let name = "Champ";
    println!("Hello {}", name);

    let vect1 = vec![1,2,3,4,5];

    for i in vect1{
        println!("i is {}", i);
        //Some(x) => println!("{}",x),
        //None => break,
    }

    for i in 20..30 {
        println!("i is: {}", i);
    }

    let rand_string3 = "Champ Pitts I am a random string There are other strings like it\nThis string is the best";
    let mut iter = rand_string3.split_whitespace();

    let mut indiv_word = iter.next();

    loop {
        match indiv_word {
            Some(x) => println!("X: {}", x),
            None => break,
        }
        indiv_word = iter.next();
    }
    // Iterate over lines of string
    let rand_string2 = "Champ\nPitts\nI am a random string\nThere are other strings like it\nThis string is the best";


    let mut lines = rand_string2.lines();

    let mut indiv_line = lines.next();

    loop {
        match indiv_line {
            Some(b) => println!("b: {}", b),
            None => break,
        }
        indiv_line = lines.next();
    }

    let mut k = 10;

    loop {
        if k > 1 {
            println!("Current number is: {}", k);
        }
        if k == 1{
            break;
        }
        k -= 1;
        //:continue;
    }
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

}
