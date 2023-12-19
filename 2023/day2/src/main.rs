use std::fs::File;
use std::collections::HashMap;
use std::io::{self, prelude::*, BufReader};

fn part_one() -> io::Result<()> {
    let file = File::open("input.txt")?;
    let reader = BufReader::new(file);

    let mut result: i32 = 0;

    let mut bag: HashMap<String, i32> = HashMap::new();
    bag.insert(String::from("red"), 12);
    bag.insert(String::from("green"), 13);
    bag.insert(String::from("blue"), 14);
    
    //  Goes line by line
    'games: for line_read in reader.lines() {

        let line = line_read?;

        let mut game_data = line.split(":");
        let game_id = game_data.next().expect("Expected game info").split(" ").collect::<Vec<_>>()[1];
        let data: Vec<&str> = game_data.next().expect("Expected game data").trim_start().split(";").collect();

        for handful in data {
            let dices: Vec<&str> = handful.trim_start().split(",").flat_map(|obj| obj.trim_start().split(" ")).collect();
            for i in (0..=dices.len()-1).step_by(2) {
                match dices[i].parse::<i32>() {
                    Ok(parsed) => {
                        match bag.get(dices[i+1]) {
                            Some(amount) => { if amount < &(parsed) { continue 'games; } },
                            None => (),
                        }
                    }
                    Err(_) => {}
                }
            }
        }

        match game_id.parse::<i32>() {
            Ok(parsed) => {
                result += parsed;
            }
            Err(_) => {}
        }
    }
    
    println!("{}", result);
    
    Ok(())
}

fn part_two() -> io::Result<()> {
    let file = File::open("input.txt")?;
    let reader = BufReader::new(file);

    let mut result: i32 = 0;
    
    //  Goes line by line
    for line_read in reader.lines() {

        let line = line_read?;

        let mut game_data = line.split(":");
        let game_id = game_data.next().expect("Expected game info").split(" ").collect::<Vec<_>>()[1];
        let data: Vec<&str> = game_data.next().expect("Expected game data").trim_start().split(";").collect();

        let mut max_red = 0;
        let mut max_green = 0;
        let mut max_blue = 0;
        for handful in data {
            let dices: Vec<&str> = handful.trim_start().split(",").flat_map(|obj| obj.trim_start().split(" ")).collect();
            for i in (0..=dices.len()-1).step_by(2) {
                match dices[i].parse::<i32>() {
                    Ok(parsed) => {
                        match dices[i+1] {
                            "red" => { if parsed > max_red { max_red = parsed } },
                            "green" => { if parsed > max_green { max_green = parsed } },
                            "blue" => { if parsed > max_blue { max_blue = parsed } },
                            &_ => (),
                        }
                    }
                    Err(_) => {}
                }
            }
        }

        result += max_red * max_green * max_blue;
    }
    
    println!("{}", result);
    
    Ok(())
}


fn main() {
    // let _ = part_one();
    let _ = part_two();
}
