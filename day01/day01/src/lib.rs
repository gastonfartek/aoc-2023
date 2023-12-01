pub fn part_a(input: &str) -> u32 {
    let mut result: u32 = 0;

    for line in input.lines() {
        let mut i: usize = 0;
        let mut j: usize = line.len() - 1;
        while i <= j {
            let c1 = line.chars().nth(i).unwrap();
            let c2 = line.chars().nth(j).unwrap();

            if !c1.is_digit(10) {
                i += 1;
            }

            if !c2.is_digit(10) {
                j -= 1;
            }

            if c1.is_digit(10) && c2.is_digit(10) {
                result += (c1.to_digit(10).unwrap() * 10) + c2.to_digit(10).unwrap();
                break;
            }
        }
    }
    result
}

pub fn part_b(input: &str) -> u32 {
    let mut result: u32 = 0;
    for line in input.lines() {
        let mut new_line = line.replace("one", "o1e");
        new_line = new_line.replace("two", "t2o");
        new_line = new_line.replace("three", "t3ree");
        new_line = new_line.replace("four", "f4ur");
        new_line = new_line.replace("five", "f5ve");
        new_line = new_line.replace("six", "s6x");
        new_line = new_line.replace("seven", "s7ven");
        new_line = new_line.replace("eight", "8ight");
        new_line = new_line.replace("nine", "9ine");

        for character in new_line.chars() {
            if character.is_digit(10) {
                result += character.to_digit(10).unwrap() * 10;
                break;
            }
        }

        for character in new_line.chars().rev() {
            if character.is_digit(10) {
                result += character.to_digit(10).unwrap();
                break;
            }
        }
    }
    return result;
}

#[cfg(test)]
mod tests {
    use super::*;

    const SAMPLE_INPUT_A: &str = "1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet";

    const SAMPLE_INPUT_B: &str = "two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
";

    #[test]
    fn test_sample_parta() {
        let result: u32 = part_a(SAMPLE_INPUT_A);
        assert_eq!(result, 142);
    }

    #[test]
    fn test_sample_partb() {
        let result: u32 = part_b(SAMPLE_INPUT_B);
        assert_eq!(result, 281);
    }

    #[test]
    fn test_sample_partb_1() {
        let result: u32 = part_b("two1nine");
        assert_eq!(result, 29);
    }

    #[test]
    fn test_sample_partb_2() {
        let result: u32 = part_b("eightwothree");
        assert_eq!(result, 83);
    }

    #[test]
    fn test_sample_partb_3() {
        let result: u32 = part_b("abcone2threexyz");
        assert_eq!(result, 13);
    }
    #[test]
    fn test_sample_partb_4() {
        let result: u32 = part_b("xtwone3four");
        assert_eq!(result, 24);
    }
    #[test]
    fn test_sample_partb_5() {
        let result: u32 = part_b("4nineeightseven2");
        assert_eq!(result, 42);
    }
    #[test]
    fn test_sample_partb_6() {
        let result: u32 = part_b("zoneight234");
        println!("top 3 number of calories sum: {}", result);
        assert_eq!(result, 14);
    }

    #[test]
    fn test_sample_partb_7() {
        let result: u32 = part_b("7pqrstsixteen");
        println!("top 3 number of calories sum: {}", result);
        assert_eq!(result, 76);
    }

    #[test]
    fn test_sample_partb_8() {
        let result: u32 = part_b("ppjvndvknbtpfsncplmhhrlh5");
        assert_eq!(result, 55);
    }

    #[test]
    fn test_sample_partb_9() {
        let result: u32 = part_b("eight9fhstbssrplmdlncmmqqnklb39ninejz");
        assert_eq!(result, 89);
    }

    #[test]
    fn test_sample_partb_10() {
        let result: u32 = part_b("kdkjqdkvgs2");
        assert_eq!(result, 22);
    }

    #[test]
    fn test_sample_partb_11() {
        let result: u32 = part_b("sixsix18six");
        assert_eq!(result, 66);
    }

    #[test]
    fn test_sample_partb_12() {
        let result: u32 = part_b("cc8one");
        assert_eq!(result, 81);
    }

    #[test]
    fn test_parta() {
        let result: u32 = part_a(include_str!("input.txt"));
        println!("max number of calories: {}", result);
        assert_eq!(result, 53080);
    }

    #[test]
    fn test_partb() {
        let result: u32 = part_b(include_str!("input.txt"));
        println!("top 3 number of calories sum: {}", result);
        assert_eq!(result, 195625);
    }
}
