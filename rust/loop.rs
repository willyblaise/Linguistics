// Import data types for testing
use std::{i8, i16, i32, i64, u8, u16, u32, u64, isize, usize, f32, f64};

//use std::io::stdin;

fn main(){


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

    let mut a = 1;

    loop {

        if ((a % 2) == 0) {
            println!("{}", a);
            a += 1;

            continue;
        }
        a += 1
    }

}
