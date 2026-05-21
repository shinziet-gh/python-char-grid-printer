# Character Grid Printer

## Features
- Reads a CSV file containing three columns that define a character and its specified coordinates
- Prints the grid of characters on the console

## Example CSV Data

| x-coordinate | Characters | y-coordinate |
| -------- | -------- | -------- |
| 87  | ░  | 3  |
| 78  | █  | 6  |


## Requirements
- Python 3.x
- Pandas

## To install dependencies
```pip install -r requirements.txt```

## To run the code
```python main.py```

## Output

```txt
        █ █     █ █    
      █ █ █ █ █ █ █ █  
    █ █ █ █ █ █ █ █ █ █
      █ █ █ █ █ █ █ █  
        █ █ █ █ █ █    
          █ █ █ █      
            █ █        
```

## Project Structure
.
├── main.py
├── requirements.txt
└── data.csv