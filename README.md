# Terminal Image Viewer

A terminal-based image viewer that displays images and thumbnails in terminal using colored Unicode characters.

![alt text](https://github.com/bishwaraj13/terminal_image_viewer/blob/main/results/sample_result.png?raw=true)

## Motivation
I work in remote servers for development purpose. And I work with just terminal. So, its hard to visualise images. The only way to visualise images is to download them locally. The project is an attempt to help with that.

## Steps to setup the project
1. Clone the repository
2. Open a terminal or command prompt and navigate to the root directory of the project.
3. Create a new virtual environment by running the following command:
```bash
python -m venv myenv
```
4. Activate the virtual environment:
For Windows:
```bash
myenv\Scripts\activate
```

For Mac/Linux:
```bash
source myenv/bin/activate
```

After activating the virtual environment, you should see the name of the virtual environment in your terminal prompt, indicating that you are now working within the virtual environment.

5. Install the project dependencies using the requirements.txt file:
```bash
pip install -r requirements.txt
```

6. To use the image viewer, run the following command:

```bash
cd src
python -m terminal_image_viewer.image_viewer <image-path or directory>
```

E.g,
```bash
cd src
python -m terminal_image_viewer.image_viewer ../tests/test_image.png
```

## How This Really Works?

### The image viewer uses the following algorithm to display images in the terminal:

1. Resize the image to fit the terminal size while maintaining the aspect ratio.
2. Iterate over the image pixels in steps of 2 in both the x and y directions.
3. For each 2x2 block of pixels, retrieve the color values of the four pixels.
4. Convert the RGB color values to ANSI color codes using color quantization.
5. Use Unicode block characters ('▓') to represent each 2x2 block of pixels.
6. Print the Unicode characters with their corresponding ANSI color codes to display the image in the terminal.

### For displaying thumbnails, the algorithm follows these steps:

1. Get the list of image files in the specified folder.
2. Calculate the terminal size and determine the maximum width and height for each thumbnail.
3. Iterate over the image files and display them as thumbnails in a grid layout.

