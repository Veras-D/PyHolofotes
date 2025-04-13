# PyHolofotes

A Python program to control an Arduino RELE system, injecting pulses into surfaces for thermal analysis with a thermal imaging camera. Implemented at the UEMA Heat Transfer Laboratory, providing an efficient platform for thermal data collection.


## How to Download and Run

To download the executable, check `Releases` and look for the latest version of the `.zip` file compatible with **your operating system**. After downloading, **extract the file** and run the program.

## Requirements

### From the Computer
Before running the program, **make sure** you have installed the following packages:
- pyserial
- CustomTkinter
- packaging
- pyFirmata

These packages can be installed using pip:

```bash
pip install requirements.txt
```

### From Arduino
The Arduino must be loaded with the `arduino_code.ino` script for the code to be usable. Loading can be done using the **Arduino IDE** software.

## Licence

This project is licensed under the **MIT license**. For more details, see the `LICENSE` file.

## Contributions

Contributions are welcome! If you find a bug or have a suggestion for improvement, please create an issue or submit a pull request (make sure to **run the tests** before submitting a pull request).

## Project Screenshots

| SetUp | Configure | About |
| -------- | -------- | -------- |
| ![SetUp](https://i.imgur.com/YKO19bX.png) | ![Configure](https://i.imgur.com/DqAc6Ir.png) | ![About](https://i.imgur.com/oMBqqiV.png) |
| ![SetUp](https://i.imgur.com/weQR1al.png) | ![Configure](https://i.imgur.com/AWbjtwn.png) | ![About](https://i.imgur.com/EB8vFol.png) |


## Source Code

The source code for this project is available on GitHub. To clone the repository, use the following command:

```bash
git clone git@github.com:Veras-D/PyHolofotes.git
```
