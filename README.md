# List Optimizer

List Fix is a Python script that allows you to optimize a list of URLs or domains by stripping or adding the 'http://' and 'https://' prefixes.

## Features

- Strips 'http://' and 'https://' from URLs
- Adds 'http://' to domains
- Adds 'https://' to domains

## Requirements

- Python 3.x
- Requests library (`pip install requests`)
- Colorama library (`pip install colorama`)

## Usage

1. Clone the repository:

   ```
   git clone https://github.com/your-username/list-optimizer.git
   ```
Change to the project directory:
```
cd list-optimizer
```
Run the script:

```
python list_optimizer.py
```
Follow the menu prompts to select the desired option and provide the input file.

The modified URLs or domains will be saved in separate output files.

# Examples
Stripping 'http://' and 'https://' from URLs Input File (urls.txt):

```
http://example.com
https://google.com
```
run script
```
python list_optimizer.py
Output File (rslt.txt):
```
Output:
```
example.com
google.com
```
Adding 'http://' to domains
Input File (domains.txt):
```
example.com
google.com
```
run script
```
python list_optimizer.py
Output File (rslt2.txt):
```
Output:
```
http://example.com
http://google.com
```
Adding 'https://' to domains
Input File (domains.txt):

```
example.com
google.com
```
run script
```
python list_optimizer.py
Output File (rslt3.txt):
```
Output:
```
https://example.com
https://google.com
```
# Contributing
Contributions are welcome. If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.


