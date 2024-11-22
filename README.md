# Word Count Script

This repository contains a Python script that counts the occurrences of each word in a given text file. The script can optionally count words in a case-insensitive manner and exclude common stop words from the count.

## Features

- Counts the occurrences of each word in a text file.
- Optionally counts words in a case-insensitive manner.
- Optionally excludes common stop words from the count.
- Displays a progress bar while processing the file.

## Requirements

- Python 3.x
- `tqdm` library

You can install the `tqdm` library using pip:

```bash
pip install tqdm
```

## Usage

To run the script, use the following command:

```bash
python script.py <filename> [--case-insensitive] [--exclude-stop-words]
```

### Arguments

- `<filename>`: The path to the text file to be processed.
- `--case-insensitive`: (Optional) Count words in a case-insensitive manner.
- `--exclude-stop-words`: (Optional) Exclude common stop words from the count.

### Example

```bash
python script.py example.txt --case-insensitive 
```

## Output

The script will print the total word count and the top 10 most common words along with their counts.

### Example Output

```plaintext
Total word count: 17,005,207
the: 1,061,396
of: 593,677
and: 416,629
one: 411,764
in: 372,201
a: 325,873
to: 316,376
zero: 264,975
nine: 250,430
two: 192,644
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

[Rasheed Alqobbaj](https://github.com/Rasheed-Al-Qobbaj)
