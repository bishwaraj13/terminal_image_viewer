def rgb_to_ansi(r, g, b):
    r, g, b = r // 64, g // 64, b // 64  # Adjust color quantization for sharper edges
    return 16 + 36 * r + 6 * g + b
