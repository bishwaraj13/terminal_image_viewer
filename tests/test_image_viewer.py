import os
import sys
import pytest
from unittest.mock import patch
from io import StringIO

src_path = '../src'
sys.path.append(src_path)

from terminal_image_viewer.image_viewer import ImageViewer

@pytest.fixture
def test_image_path():
    return "test_image.png"

@pytest.fixture
def test_folder_path():
    return "test_folder"

@pytest.fixture
def invalid_path():
    return "invalid_path"

def get_terminal_size():
    return os.terminal_size((80, 24))  # Return a fixed terminal size for testing

def test_display_image(test_image_path, monkeypatch):
    monkeypatch.setattr(os, 'get_terminal_size', get_terminal_size)
    viewer = ImageViewer(test_image_path)
    with patch("sys.stdout", new=StringIO()) as fake_output:
        viewer.run()
        assert "▓" in fake_output.getvalue()  # Check if the image is displayed

def test_display_thumbnails(test_folder_path, monkeypatch):
    monkeypatch.setattr(os, 'get_terminal_size', get_terminal_size)
    viewer = ImageViewer(test_folder_path)
    with patch("sys.stdout", new=StringIO()) as fake_output:
        viewer.run()
        assert "▓" in fake_output.getvalue()  # Check if thumbnails are displayed

def test_invalid_path(invalid_path, monkeypatch):
    monkeypatch.setattr(os, 'get_terminal_size', get_terminal_size)
    viewer = ImageViewer(invalid_path)
    with patch("sys.stdout", new=StringIO()) as fake_output:
        viewer.run()
        assert "Error: 'invalid_path' is not a valid file or directory." in fake_output.getvalue()
        