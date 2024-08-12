# DNA-helix

This Python script generates a simple DNA animation in the console, simulating the appearance of a DNA strand. The animation continuously loops, displaying a sequence of characters that represent DNA base pairs.

![cdb7ac74-3969-4e7e-ab46-a82a87aacb06](https://github.com/user-attachments/assets/89d0b81f-800a-4b7d-8c94-354239fad51c)

## Features

- **Cross-platform console clearing**: The script clears the console screen for both Windows and Unix-based systems (Linux, macOS).
- **Adjustable length and delay**: You can customize the length of the DNA strand and the delay between frames to control the speed of the animation.

## Requirements

- Python 3.x

## Usage

1. **Clone or download the repository** containing the script.

2. **Navigate to the directory** where the script is located.

3. **Run the script** using Python:

    ```bash
    python dna_animation.py
    ```

    Replace `dna_animation.py` with the actual name of your script file if it's different.

## Script Parameters

The script contains two optional parameters:

- `length` (default: 20): The number of lines of the DNA pattern to display.
- `delay` (default: 0.1): The delay (in seconds) between each frame of the animation.

You can modify these parameters directly in the script or by passing them as arguments when calling the `print_dna` function.

## Example

Here's an example of how you can call the `print_dna` function with custom parameters:

```python
if __name__ == "__main__":
    print_dna(length=30, delay=0.2)
```

This will display a longer DNA strand (30 lines) and slow down the animation (0.2 seconds delay between frames).

## Code Explanation

### clear_console Function

The `clear_console` function clears the console screen. It checks the operating system and uses the appropriate command:

- For Windows (`os.name == 'nt'`), it uses `cls`.
- For Unix-based systems, it uses `clear`.

### print_dna Function

The `print_dna` function generates the DNA animation:

1. **Pattern Definition**: A list of strings (`pattern`) represents the DNA base pairs.
2. **Infinite Loop**: The animation runs indefinitely.
3. **Frame Update**: For each frame, it:
    - Clears the console.
    - Prints the DNA pattern shifted by one position.
    - Waits for the specified delay before updating the frame.

## Customization

You can modify the `pattern` list to change the appearance of the DNA strand. Each string in the list represents one line of the pattern.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- This script was created as a simple demonstration of console animation in Python.

Feel free to modify and enhance the script according to your needs. Enjoy coding!
