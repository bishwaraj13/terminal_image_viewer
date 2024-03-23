import os, sys
from PIL import Image
from terminal_image_viewer.utils import rgb_to_ansi

class ImageViewer:
    def __init__(self, path):
        self.path = path

    def display_image(self, image_path, max_width, max_height):
        try:
            with Image.open(image_path) as image:
                # Resize the image to fit the terminal size
                image.thumbnail((max_width, max_height))

                # Display the image with colored pixels using Unicode block characters
                for y in range(0, image.height, 2):
                    for x in range(0, image.width, 2):
                        pixel1 = image.getpixel((x, y))
                        pixel2 = image.getpixel((x + 1, y)) if x + 1 < image.width else pixel1
                        pixel3 = image.getpixel((x, y + 1)) if y + 1 < image.height else pixel1
                        pixel4 = image.getpixel((x + 1, y + 1)) if x + 1 < image.width and y + 1 < image.height else pixel1

                        ansi_color1 = rgb_to_ansi(*pixel1[:3])
                        ansi_color2 = rgb_to_ansi(*pixel2[:3])
                        ansi_color3 = rgb_to_ansi(*pixel3[:3])
                        ansi_color4 = rgb_to_ansi(*pixel4[:3])

                        # Use different Unicode characters for sharper edges
                        print(f"\033[38;5;{ansi_color1}m\033[48;5;{ansi_color2}m▓\033[0m\033[38;5;{ansi_color3}m\033[48;5;{ansi_color4}m▓\033[0m", end="")
                    print()
        except IOError:
            print(f"Error: Unable to open the image file '{image_path}'.")

    def display_thumbnails(self, folder_path):
        # Get the list of image files in the folder
        image_files = [file for file in os.listdir(folder_path) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

        if not image_files:
            print(f"No image files found in the folder '{folder_path}'.")
            return

        # Calculate the terminal size
        terminal_size = os.get_terminal_size()
        max_width = terminal_size.columns // 2  # Divide by 2 to display two thumbnails per row
        max_height = terminal_size.lines // 2  # Divide by 2 to display two rows of thumbnails

        # Display the thumbnails
        for i in range(0, len(image_files), 4):
            for j in range(4):
                if i + j < len(image_files):
                    image_path = os.path.join(folder_path, image_files[i + j])
                    self.display_image(image_path, max_width, max_height)
                else:
                    print()
            print()

    def run(self):
        if os.path.isfile(self.path):
            # Display a single image
            terminal_size = os.get_terminal_size()
            max_width = terminal_size.columns * 2  # Double the width for block characters
            max_height = terminal_size.lines - 2  # Reserve 2 lines for prompt
            self.display_image(self.path, max_width, max_height)
        elif os.path.isdir(self.path):
            # Display thumbnails of images in the folder
            self.display_thumbnails(self.path)
        else:
            print(f"Error: '{self.path}' is not a valid file or directory.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python image_viewer.py <image_file|folder>")
        sys.exit(1)

    path = sys.argv[1]
    viewer = ImageViewer(path)
    viewer.run()

if __name__ == '__main__':
    main()
