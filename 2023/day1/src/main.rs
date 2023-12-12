use std::fs::File;
use std::io::{self, prelude::*, BufReader};

fn find_num_word(substring: String, rev: bool) -> Option<char> {
    let num_words: [String; 9] =   ["one".to_string(), 
                                    "two".to_string(), 
                                    "three".to_string(), 
                                    "four".to_string(), 
                                    "five".to_string(), 
                                    "six".to_string(), 
                                    "seven".to_string(), 
                                    "eight".to_string(), 
                                    "nine".to_string()];

    let mut first: bool = true;
    let (mut index, mut value): (u8, u8) = (0, 0);

    //  Looks for each word in string
    for (key, word) in num_words.iter().enumerate() {
        let a;
        match rev {
            false => a = substring.find(word),
            true => a = substring.rfind(word),
        }

        if a != None {
            if first {
                value = key as u8;
                index = a.unwrap() as u8;
                first = false;
            } else if rev {
                if a.unwrap() > index.into() {
                    value = key as u8;
                    index = a.unwrap() as u8;
                }
            } else if a.unwrap() < index.into() {
                value = key as u8;
                index = a.unwrap() as u8;
            }
        }
    }

    if first {
        return None
    } else {
        return Some((value + 1 + b'0') as char)
    }
}

fn main() -> io::Result<()> {
    let file = File::open("input.txt")?;
    let reader = BufReader::new(file);

    let mut sum: u32 = 0;
    
    //  Goes line by line
    for line_read in reader.lines() {
        let (mut first, mut second): (char, char) = ('\0', '\0');
        let mut num_str: String = "".to_string();

        let line = line_read?;
        
        //  Looks for digit from the beginning
        for (key, ch) in line.chars().enumerate() { 
            if ch.is_ascii_digit() {
                first = ch;
                if key > 0 {
                    match find_num_word((&line[..key]).to_string(), false) {
                        Some(val) => first = val,
                        _ => (),
                    }
                }
                break;
            }
        }
        
        //  If no digit was found then looks for number words and goes to next line
        if first == '\0' {
            first = find_num_word((&line).to_string(), false).unwrap();
            second = find_num_word((&line).to_string(), true).unwrap();
        } else {
            //  Looks for digit from the end
            for (key, ch) in line.chars().rev().enumerate() { 
                if ch.is_ascii_digit() {
                    second = ch;
                    if key > 0 {
                        match find_num_word((&line[&line.len()-key..]).to_string(), true) {
                            Some(val) => second = val,
                            _ => (),
                        }
                    }
                    break;
                }
            }
        }
        
        //  Combines digits into a whole number and adds to sum
        num_str.push(first);
        num_str.push(second);
        sum += num_str.parse::<u32>().unwrap();
    }
    
    println!("Sum: {}", sum);
    
    Ok(())
}
