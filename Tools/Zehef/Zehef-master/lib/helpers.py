"""
The 'Color' class is made to create a gradient from one color to another predefined one, so here:
- start = #FE0000 ~ Red
- end = #FFFFFF ~ White
"""

class Color:
    red: int
    green: int
    blue: int

    @classmethod
    def from_hex(cls, hex: str):

        # Check if the input is a valid hex color code
        if not (hex.startswith("#") and len(hex) == 7):
            raise ValueError("Invalid hex color code")

        # Extract R, G, B components
        r = int(hex[1:3], 16)
        g = int(hex[3:5], 16)
        b = int(hex[5:7], 16)

        # Ensure the values are in the range 0 to 255
        return cls(
            max(0, min(r, 255)),
            max(0, min(g, 255)),
            max(0, min(b, 255))
        )

    def __init__(self, r: int, g: int, b: int) -> None:
        self.red = r
        self.green = g
        self.blue = b

    # lerp ~ Linear interpolation
    @staticmethod
    def lerp(start, end, alpha: float):

        r = float(start.red)
        g = float(start.green)
        b = float(start.blue)

        r_d = float(end.red) - r
        g_d = float(end.green) - g
        b_d = float(end.blue) - b

        r += (r_d * alpha)
        g += (g_d * alpha)
        b += (b_d * alpha)

        return Color(int(r), int(g), int(b))

def print_banner(banner: str, start: Color, end: Color) -> None:
    banner_split = banner.split('\n')
    lines = []

    for index, banner_line in enumerate(banner_split):

        alpha = float(index) / float(len(banner_split) - 1)

        color = Color.lerp(start=start, end=end, alpha=alpha)
        # print(index, alpha, color.red, color.green, color.blue)

        color = f"\033[38;2;{color.red};{color.green};{color.blue}m"
        line = color + banner_line + "\033[0m" # reset

        lines.append(line)

    banner = '\n'.join(lines)

    print(f"{banner}\n\r")

def show_banner():
    banner = """
               __    ________  _____ 
________ ____ |  |__ \_____  \/ ____\\
\___   // __ \|  |  \  _(__  <   __\ 
 /    /\  ___/|   Y  \/       \  |   
/_____ \\\___  >___|  /______  /__|      
      \/    \/     \/       \/

     ~: 📭 Email OSINT Tool :~
        => Made by @N0rz3
"""

    print_banner(banner, start=Color.from_hex("#FE0000"), end=Color.from_hex("#FFFFFF"))