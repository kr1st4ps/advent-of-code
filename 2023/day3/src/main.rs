use std::fs::File;
use std::io::{self, prelude::*, BufReader};

#[derive(PartialEq)]
#[derive(Debug)]
struct Point {
    row: i16,
    col: i16,
}

struct Number {
    num: String,
    points: Vec<Point>,
}

struct Gear {
    point: Point,
    nums: Vec<u32>,
}

fn part_one() -> io::Result<()> {
    let file = File::open("input.txt")?;
    let reader = BufReader::new(file);

    let mut result: u32 = 0;
    let mut symbols: Vec<Point> = vec![];
    let mut num: Number = Number { num: "".to_string(), points: vec![] };
    let mut nums: Vec<Number> = vec![];
    
    //  Goes row by row
    for (row_u, line_read) in reader.lines().enumerate() {
        let row = row_u as i16;

        let line = line_read?;

        //  Saves number if it ended with last line
        if num.num.len() > 0 {
            nums.push(num);
            num = Number { num: "".to_string(), points: vec![] };
        }

        for (col_u, ch) in line.chars().enumerate() {
            let col = col_u as i16;
            
            if ch.is_ascii_digit() {
                num.num += &ch.to_string();

                if num.points.contains(&Point {row: row as i16, col: col as i16}) {
                    num.points.retain(|x| x != &Point {row: row as i16, col: col as i16});
                }

                for x in -1i16..=1 {
                    for y in -1i16..=1 {
                        if (x == 0 && y == 0) || (row + x) < 0 || (col + y) < 0 || num.points.contains(&Point {row: row+x as i16, col: col+y as i16}) {
                            continue;
                        } else {
                            num.points.push(Point {row: row+x, col: col+y});
                        }
                    }
                }
            } else {
                if num.num.len() > 0 {
                    nums.push(num);
                    num = Number { num: "".to_string(), points: vec![] };
                }

                if ch != '.' {
                    symbols.push(Point {row: row as i16, col: col as i16});
                }
            }
        }

    }
    
    'start: for nr in &nums {
        for nr_point in &nr.points {
            if symbols.contains(&nr_point) {
                match nr.num.parse::<u32>() {
                    Ok(parsed) => {result += parsed; continue 'start;}
                    Err(_) => {}
                }
            }
        }
    }

    println!("{}", result);
    
    Ok(())
}

fn part_two() -> io::Result<()> {
    let file = File::open("input.txt")?;
    let reader = BufReader::new(file);

    let mut result: u32 = 0;
    let mut num: Number = Number { num: "".to_string(), points: vec![] };
    let mut nums: Vec<Number> = vec![];
    let mut gears: Vec<Gear> = vec![];
    
    //  Goes row by row
    for (row_u, line_read) in reader.lines().enumerate() {
        let row = row_u as i16;

        let line = line_read?;

        //  Saves number if it ended with last line
        if num.num.len() > 0 {
            nums.push(num);
            num = Number { num: "".to_string(), points: vec![] };
        }

        for (col_u, ch) in line.chars().enumerate() {
            let col = col_u as i16;
            
            if ch.is_ascii_digit() {
                num.num += &ch.to_string();

                if num.points.contains(&Point {row: row as i16, col: col as i16}) {
                    num.points.retain(|x| x != &Point {row: row as i16, col: col as i16});
                }

                for x in -1i16..=1 {
                    for y in -1i16..=1 {
                        if (x == 0 && y == 0) || (row + x) < 0 || (col + y) < 0 || num.points.contains(&Point {row: row+x as i16, col: col+y as i16}) {
                            continue;
                        } else {
                            num.points.push(Point {row: row+x, col: col+y});
                        }
                    }
                }
            } else {
                if num.num.len() > 0 {
                    nums.push(num);
                    num = Number { num: "".to_string(), points: vec![] };
                }

                if ch == '*' {
                    gears.push(Gear {point: Point {row: row as i16, col: col as i16}, nums: vec![]});
                }
            }
        }

    }

    for gear in &mut gears {
        for nr in &nums {
            if nr.points.contains(&gear.point) {
                match nr.num.parse::<u32>() {
                    Ok(parsed) => { gear.nums.push(parsed) }
                    Err(_) => {}
                }
            }
        }
    }

    for gear in &gears {
        if gear.nums.len() == 2 {
            result += gear.nums[0] * gear.nums[1];
        }
    }
    println!("{}", result);
    
    Ok(())
}


fn main() {
    // let _ = part_one();
    let _ = part_two();
}
