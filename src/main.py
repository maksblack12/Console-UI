import ctypes;ctypes.windll.kernel32.SetConsoleMode(ctypes.windll.kernel32.GetStdHandle(-11),7)


class Style:
	def __init__(self, top_left_corner, top_right_corner, bottom_left_corner, bottom_right_corner, vertical_line, horizontal_line):
		self.top_left_corner=top_left_corner
		self.top_right_corner=top_right_corner
		self.bottom_left_corner=bottom_left_corner
		self.bottom_right_corner=bottom_right_corner
		self.vertical_line=vertical_line
		self.horizontal_line=horizontal_line

class Pixel:
	def __init__(self, char, color, bg_color):
		self.char=char
		self.color=color
		self.bg_color=bg_color
	def __repr__(self):
		return f"\x1b[38;2;{self.color[0]};{self.color[1]};{self.color[2]}m\x1b[48;2;{self.bg_color[0]};{self.bg_color[1]};{self.bg_color[2]}m{self.char}"

class Canvas:
	def __init__(self, w, h):
		self.w=w
		self.h=h
		self.pixels=[[Pixel(" ", (255, 255, 255), (0, 0, 0)) for _ in range(w)] for _ in range(h)]

	def print(self):
		for row in self.pixels:
			print("".join(map(str,row))+"\x1b[0m")

	def rectangle(self, offset_x, offset_y, w, h, color, bg_color, style):
		self.pixels[offset_y][offset_x]=Pixel(style.top_left_corner, color, bg_color)
		self.pixels[offset_y][offset_x+w-1]=Pixel(style.top_right_corner, color, bg_color)
		self.pixels[offset_y+h-1][offset_x]=Pixel(style.bottom_left_corner, color, bg_color)
		self.pixels[offset_y+h-1][offset_x+w-1]=Pixel(style.bottom_right_corner, color, bg_color)
		for x in range(offset_x+1, offset_x+w-1):
			self.pixels[offset_y][x]=Pixel(style.horizontal_line, color, bg_color)
			self.pixels[offset_y+h-1][x]=Pixel(style.horizontal_line, color, bg_color)
		for y in range(offset_y+1, offset_y+h-1):
			self.pixels[y][offset_x]=Pixel(style.vertical_line, color, bg_color)
			self.pixels[y][offset_x+w-1]=Pixel(style.vertical_line, color, bg_color)

# ─ ━ │ ┃ ┄ ┅ ┆ ┇ ┈ ┉ ┊ ┋ ┌ ┍ ┎ ┏
# ┐ ┑ ┒ ┓ └ ┕ ┖ ┗ ┘ ┙ ┚ ┛ ├ ┝ ┞ ┟
# ┠ ┡ ┢ ┣ ┤ ┥ ┦ ┧ ┨ ┩ ┪ ┫ ┬ ┭ ┮ ┯
# ┰ ┱ ┲ ┳ ┴ ┵ ┶ ┷ ┸ ┹ ┺ ┻ ┼ ┽ ┾ ┿
# ╀ ╁ ╂ ╃ ╄ ╅ ╆ ╇ ╈ ╉ ╊ ╋ ╌ ╍ ╎ ╏
# ═ ║ ╒ ╓ ╔ ╕ ╖ ╗ ╘ ╙ ╚ ╛ ╜ ╝ ╞ ╟
# ╠ ╡ ╢ ╣ ╤ ╥ ╦ ╧ ╨ ╩ ╪ ╫ ╬ ╭ ╮ ╯
# ╰ ╱ ╲ ╳ ╴ ╵ ╶ ╷ ╸ ╹ ╺ ╻ ╼ ╽ ╾ ╿

STYLE_SINGLE_STROKE=Style(
	"┌",
	"┐",
	"└",
	"┘",
	"│",
	"─"
)

STYLE_SINGLE_ROUNDED_STROKE=Style(
	"╭",
	"╮",
	"╰",
	"╯",
	"│",
	"─"
)

STYLE_SINGLE_THICK_STROKE=Style(
	"┏",
	"┓",
	"┗",
	"┛",
	"┃",
	"━"
)

STYLE_DOUBLE_STROKE=Style(
	"╔",
	"╗",
	"╚",
	"╝",
	"║",
	"═"
)


canvas=Canvas(24, 12)
canvas.rectangle(2, 1, 10, 8, (255, 255, 0), (0, 0, 0), STYLE_SINGLE_ROUNDED_STROKE)
canvas.rectangle(4, 2, 6, 6, (255, 0, 0), (0, 0, 0), STYLE_SINGLE_THICK_STROKE)
canvas.print()