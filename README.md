# Basic Calculator GUI

This is a basic calculator GUI application implemented in Python using the tkinter library. The application provides a simple graphical interface for performing basic arithmetic calculations. Users can input numbers and perform operations by clicking on the calculator buttons.

## Features

- Addition, subtraction, multiplication, and division operations are supported.

- Parentheses can be used for grouping expressions.

- User can input by clicking the calculator buttons

## Requirements

- Python 3.x
- Tkinter library (usually comes pre-installed with Python)

## How to Use

1. Make sure you have Python and Tkinter installed on your system.

2. Clone this repository or download the main.py file to your local machine.

3. Run the main.py script using Python:

    ```
    python main.py
    ```

- . The calculator window will open with the title "Basic Calculator."
- . Use the mouse to click on the buttons to input numbers and perform operations.
    - Type numbers 0-9 to input them into the calculation.

    - . Use the following symbols for operations:
        - ' + ' for addition
        - ' - ' for subtraction
        - ' * ' for multiplication
        - ' / ' for division
        - ' ( '  and ' ) ' for grouping expressions.

    - Press the ' = ' key to evaluate the calculation.
    - Press the ' C ' key to clear the calculation.

## Examples

- To calculate 3 + 5, click the buttons 3, +, 5, and = and press =.
- To calculate (4 + 2) * 3, click the buttons (, 4, +, 2, ), *, 3, and =, and press =.
- To calculate 10 / 0, click the buttons 1, 0, /, 0, and =, and press =.

## Error Handling

- If an invalid expression is entered (e.g., division by zero or syntax errors), the calculator will display "Error" in the result field.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and distribute it.