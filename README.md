# MyColorsPy

<img src="https://img.shields.io/badge/MyColorsPy-0.1.3-violet"/> <img src="https://img.shields.io/badge/python-3.10+-blue"/>

## About:

MyColorsPy - python`s module for using color in win command line or terminal.

### Functional:

- Add color for text;
- Add style for text (works differently in different systems);
- Add user`s custom color for text (RGB format).

## Screenshots:

<img src="https://sun9-31.userapi.com/impg/tDyTXun_rzpDzIUwKNBXhH6Ya7xKf7tPAoSV1Q/gynp_Frjf-Y.jpg?size=975x114&quality=95&sign=32cd19b9d59acb26fd5b190a7f03e19d&type=album"/>

> example.py output.

## How to use:
```python
# import module
from MyColorsPy.MyColorsPy import Colors

# init Colors class
color = Colors()

# print red text
print(color.F_RED + "RED TEXT")
# clear formatting
print(color.S_CLEAR)
```
> Using red color in output

- If not use S_CLEAR subsequent lines will also be colored red.

```python
# import module
from MyColorsPy.MyColorsPy import Colors

# init Colors class
color = Colors()

# print custom color in rgb format (white)
print(color.custom(255, 255, 255, False) + "Hello world!")
# clear formatting
print(color.S_CLEAR)
```
> Using custom color in output. 

- You can use S_CLEAR in one line with output content to avoid a space along with clearing formatting.

#### custom(r, g, b, background)

Return custom rgb color in ascii format.

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `r`  | `int` | red |
| `g`  | `int` | green |
| `b`  | `int` | blue |
| `bacground`  | `bool` | If equal True return custom background color, else if equal False return custom foreground color |

## Preseted colors and styles

#### Colors

| Foreground | Bacground | Color | 
| :--------- | :-------- | :---- |
| `F_BLACK` | `B_BLACK` | Black |
| `F_BLUE` | `B_BLUE` | Blue |
| `F_WHITE` | `B_WHITE` |White |
| `F_PURPLE` | `B_PURPLE` | Purple |
| `F_YELLOW` | `B_YELLOW` | Yellow |
| `F_GREEN` | `B_GREEN` | Green |
| `F_AQUA` | `B_AQUA` | Aqua |
| `F_RED` | `B_RED` | Red |

#### Styles

| Value | Description |
| :---- | :---------- |
| `S_CLEAR` | Clear formatting |
| `S_BOLD` | Bold text |
| `S_PALE` | Pale text |
| `S_ITALIC` | Italic text |
| `S_UNDERLINE` | Underlined text |
| `S_FLASH` | Flashed text |
| `S_HIDE` | Hidden text |
| `S_CROSS` | Crossed text |
| `S_DOUBLEUL` | DoubleUL text |
| `S_FRAME` | Framed text |
| `S_SURROUND` | Surrounded text |
| `S_CROSSOUT` | Crossouted text |

> P.S: Depending on the system, styles may or may not work.

## Install:

```bash
pip install MyColorsPy
```
