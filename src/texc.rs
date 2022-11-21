use std::env;
use std::path::{PathBuf,Path};
use std::process::Command;
use std::thread;
use std::time::Duration;
use std::process;
use std::fs::File;
use std::io::{BufRead,BufReader};

use clap::Parser;

enum ErrorType {
    Error,
    Warning,
    Overfull,
}

const LATEX_STR_ERROR:    &str = "! LaTeX Error:";
const LATEX_STR_WARNING:  &str = "! LaTeX Warning:";
const LATEX_STR_OVERFULL: &str = "Overfull";

#[derive(Parser)]
#[command(author, version, about, long_about = None)]
struct Cli {
    name: Option<String>,

    #[arg(short, long)]
    clean: bool,
}

fn source_dir() -> PathBuf {
    let mut cwd = env::current_exe().unwrap();
    cwd.pop();
    cwd.pop();
    cwd.pop();
    cwd
}

fn config_path() -> PathBuf {
    source_dir().join(".latexmkrc")
}

fn make_clean() {
    let config = config_path();
    let cmd = "latexmk";
    let args = [
        "-c", "-r", config.to_str().unwrap()
    ];

    let command = Command::new(cmd).args(args).output().ok();

    if let Some(proc) = command {
        if !proc.status.success() {
            print!("[ERROR] latexmk failed with a non-zero exit code: {}\n", proc.status.code().unwrap());
            process::exit(1);
        }
    }
    else {
        print!("[ERROR] latexmk failed to execute\n");
        process::exit(1);
    }
}

fn make_build(filename: &str) {
    let config = config_path();
    let cmd = "latexmk";
    let args = [
        "-silent", "-f", "-r", config.to_str().unwrap(),
        "-bibtex", "-pdf", filename
    ];

    let command = Command::new(cmd).args(args).output().ok();

    if let None = command {
        print!("[ERROR] latexmk failed to execute\n");
        process::exit(1);
    }

    parse_log(filename);
}

fn read_file(filename: &str) -> BufReader<File> {
    let file = File::open(filename);
    BufReader::new(file.unwrap())
}

#[inline(always)]
fn parse_message(string: &str, msg_type: ErrorType) -> String {
    match msg_type {
        ErrorType::Error => {
            let start: usize = LATEX_STR_ERROR.len();
            let msg = &string[start..].trim();
            return msg.to_string()
        }
        ErrorType::Warning => {
            let start: usize = LATEX_STR_WARNING.len();
            let msg = &string[start..].trim();
            return msg.to_string()
        }
        ErrorType::Overfull => {
            let start: usize = LATEX_STR_OVERFULL.len();
            let msg = &string[start..].trim();
            return msg.to_string()
        }
    };
}

fn parse_log(filename: &str) {
    let logfile = &filename.replace(".tex", ".log");

    let path = Path::new(logfile);

    let mut count: u8 = 0;
    while !path.is_file() && count < 3 {
        thread::sleep(Duration::from_secs(1));
        count += 1;
    }

    if !path.is_file() {
        print!("[ERROR] No log file found!\n");
        process::exit(1);
    }

    let mut error:    Vec<String> = Vec::new();
    let mut warning:  Vec<String> = Vec::new();
    let mut overfull: Vec<String> = Vec::new();

    let reader = read_file(logfile);

    for line in reader.lines() {
        let string = line.unwrap();
        if string.starts_with(LATEX_STR_ERROR) {
            error.push(parse_message(&string, ErrorType::Error));
        }
        else if string.starts_with(LATEX_STR_WARNING) {
            warning.push(parse_message(&string, ErrorType::Warning));
        }
        else if string.starts_with(LATEX_STR_OVERFULL) {
            overfull.push(parse_message(&string, ErrorType::Overfull));
        }
    }

    for item in error.iter() {
        print!("[Error] {}\n", item);
    }
    for item in warning.iter() {
        print!("[Warning] {}\n", item);
    }
    for item in overfull.iter() {
        print!("[Overfull] {}\n", item);
    }
}

fn main() {
    let cli = Cli::parse();
    let name: String = cli.name.unwrap_or(String::from("main.tex"));
    let clean: bool = cli.clean;

    if clean {
        make_clean();
    }
    else {
        make_build(&name);
    }
}
