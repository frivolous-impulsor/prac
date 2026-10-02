use std::{io, string};

fn main() {
    //ownership();
    Using_Structs_Related_Data();
}

fn Using_Structs_Related_Data(){
    /*
        Define and instantiate a struct
     */
    struct  User {
        active: bool,
        username: String,
        email: String
    }

    let mut bob:User = User {
        active: true,
        username: String::from("bobTheBuilder"),
        email: String::from("bob@gmail.com"),
    };

    bob.email = String::from("bobNew@gmail.com");
    println!("bob's email: {}",bob.email);
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
        a variable to a function through parameter, pass the reference instead.
        This way, a location of the data is used, and that will only trigger
        a copy, not a move. And when the reference goes out of scope, the address
        value gets crapped, but the data itself remains valid, because the variable 
        that still owns the data is still valid (in scope).

    let str:String = String::from("abc");
    let num: usize = length_of_string(&str);
    println!("{str} is of length {num}");
     */
    /*
        Modifying a variable through a function

        Have to ensure that the types are marked mutable in all places,
        including var declaration, passing to function, and function definition
    let mut str: String = String::from("hello ");
    append_to_string(&mut str);
    println!("appended str: {str}");
     */

    /*
        Scope of a reference
        The scope of a reference starts at declaration and ends at the last use.
        One cannot declare an mutable reference after an immutable reference of the same variable.
        This is to prevent data racing: one reference is used to read the data WHILE the 
        other reference is used to write the data
    let mut s: String = String::from("hello");
    let s_ref: &String = &s;
    let s_ref_mut: &mut String = &mut s;
    println!("{s_ref}");
     */

    /*
        Dangling Reference
        A reference that points to freed memory cannot be returned. It will be reported at compile time.
        We can, instead, return a String. Returning a value to another variable will
        effectively transfer the ownership of the value, thus spare it from being
        dropped once the previous owner goes out of scope.
    
    let s: String = return_a_string();
    println!("{s}");
    */

    /*
        Slice
        A reference to a variable with starting index and the length of valid reference.
        In the example of a String slice, it can reference a substring with specified starting and ending idnex.
        in 
     */
    let str: String = String::from("Helloooo world");
    let str_slice = first_word_in_string(&str);

    println!("first word: {str_slice}");

    /*
        Index out of bound: 
        Here we attempt to read memory outside the string, thus, index out of bounds.
        Compiler won't recognize this, as it only check statically. As a result, run time error.
     */
    let str_short: String = String::from("hi");
    let first_byte: u8 = str_short.as_bytes()[3];
    println!("{first_byte}");

}

fn first_word_in_string(arg: &String) -> &str {
    /*
        The argument is a reference, since we don't want to copy the String object entirely.
        The return is of type &str: a String Slice (a type of reference)
        traversing through the String, we mark the the space as the ending of the first word.
        Thus, when we find the first space, we return the reference slice from begining to the space
     */
    let bytes = arg.as_bytes();
    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &arg[..i];
        }
    }
    return &arg[..];
}

fn return_a_string() -> String {
    let str: String = String::from("hello world");
    str
}

fn append_to_string(arg: &mut String) {
    arg.push_str("appended");
}


fn length_of_string(arg: &String) -> usize {
    arg.len()
}


fn ownnership_argument_drop (s: String) {
    println!("{s} will be dropped after this function ends");

}
