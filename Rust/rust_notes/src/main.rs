use std::{io, string};

fn main() {

    ownership();
}

fn first_three_chapters() {
    /*
        Chapter 3
        
    */
    //mut keyward: by default, a variable is immutable, meaning it cannot be changed later
    //to allow a variable to be changed in the future, a mut keyword must be added before the variable name
    /*
    let mut x = 5;
    println!("x is {x}");
    x = 6;
    println!("x is {x}");

    const SPEED_OF_LIGHT: u64 = 300000000;
    */
    //Shadowing: one may choose to declare and initialize another variable of the same name of a previous variable. When a program uses the name, the compiler will reference the most recent variable being declared. And once the newly declared variable goes out of scope, the compile will reference the most recent one that's still in scope.
    /*
    let x = 5;
    {
        let x = 10;
        println!("x is {x}");
    }
    println!("x is {x}");
    */

    /*
    Char type
    let heart_eyed_cat: char = '😻';
    println!("a heart eyed cat looks like {heart_eyed_cat}");
     */


    /*
    Compound type

    //tuple: values of different types, fixed in size once declared
    let tup: (char, i32, bool) = ('a', 2, true);
    //to retrieve a tuple, one has to deconstruct the tuple
    let (c, i, b) = tup;
    println!("{b}");
    //alternatively, one can index a tuple
    let tupFirst = tup.0;
    println!("{tupFirst}");
    //Array: fixed size, reside in stack (persumably faster retrieval)
    let array: [i32; 3] = [1,2,3];
    println!("{}", array[10]);
    */

    /*
        Statement and expressions
        statement: instructions that perform some actions and do NOT return a value
        expression: evaluate to a resultant value

     */

    /*
        Loops
        break: exit inner most loop
        continue: skip all remaining program in the current loop and begin next iteration immediately
        loop label: mark the loop for a break

        sample loop: both inner and outter loops keep track of time the program arrives
        in inner loop, a number input is received
        if number smaller than 10, the program goes back to inner
        bigger than 10, the program comes out to outter, then goes back to inner
        equal to 10, breaks out of loops
    
    let mut out_count: u32 = 0;
    let mut in_count: u32 = 0;

    'out_loop: loop {
        out_count = out_count +1;
        println!("arrive at outter");
        'in_loop: loop {
            in_count = in_count +1;
            println!("arrive at inner");

            println!("input your number: ");
            let mut text_input = String::new();

            io::stdin().read_line(&mut text_input).ok().expect("failed to read the line");
            
            let num_input: u32 = text_input.trim().parse().expect("input not a number");
            if num_input < 10 {
                continue;
            } else if num_input > 10 {
                break 'in_loop ;
            } else if num_input == 10 {
                break 'out_loop ;
            }
        }
    }
    println!("outside outter!");
    
    for number in (1..4) {
        println!("{number}!");
    }
    println!("LIFTOFF!!!");
    */
}

fn ownership () {

    /*
        Ownership
        Stack: quick access memory. Simple data (size known at compile time) will be stored here during run time.  Each function call will occupy a new disk in the stack. Once function is comolete, it gets popped, resourcs are freed afterwards.
        Heap: slow acces memory. Serving as a data dump. Complext data (size unknown at compile time) is stored here. 
        When a piece of data goes out of scope, Rust automatically frees it by calling drop. This ensures the security of the memory
        

     */

    /*
        Move: transfer of data among variables: when var 1 takes the location of value of var 2 and the value resides in heap, to ensure singular freeing of memory, Rust will invalidate var 2 immediately. As a result, when var 1 goes out of scope, its memory will be freed. But var 2 will not incur freeing of memory, because it's invalide.
    
    let s1 = String::from("hello world");
    let s2 = s1.clone();
    println!("{s1}");
    */

    /*
    Scope and assignment
    when a variable is assigned new data in heap, the original piece of data is immediately freed (goes out of scope).

    let mut str = String::from("hello world");
    str = String::from("Hello kitty");
    println!("{str}");
     */

    /*
        Deep copy: clone
        In the case where we want multiple copies of the same piece of data that reside in heaps, we use clone() method. This will explicitely create a new instance of the data that's separate from the existing data.
     */

    /*
        Copy trait vs. drop trait
        Without understanding what a trait is, I currently treat them as tags. Those data type with drop trait implies that they use memory allocation in heap. Thus when they go out of scope, they will get dropped automatically by Rust
        Thoes data types with copy trait is implied to reside entirely in stack, thus when var2 gets var1's data, the data gets copied entirely without any moving.

     */

    /*
        Ownership and functions

        When passing a variable to a function as argument, the move vs. copy still applies
        As a result, when one passes a variable that has data stored in heap (memory allocated), the data will be moved, effectively invalidate the original variable
        when one passes a variable that has data stored entirely in stack, however, the data will be copied.
     */
    /* 
    let str = String::from("hello world");
    ownnership_argument_drop(str);
    //println!("attempt to use {str}, this cannot be compiled");
    */

    /*
        Reference and borrowing

        To avoid unwanted move, one can use reference (&). When passing
        a variable through 
     */
    println!("hello world");
    
}

fn ownnership_argument_drop (s: String) {
    println!("{s} will be dropped after this function ends");

}
