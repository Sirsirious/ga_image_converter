import pytest
from pytest import raises
from image_convert import edit_image
import os

def test_open():
    image_path = './test_images/1.png'
    assert edit_image(image_path, destination_path='./test_images/test_destination/') == True

def test_resize():
    image_path = './test_images/1.png'
    assert edit_image(image_path, xsize=60, ysize=60, new_name='1resized', destination_path='./test_images/test_destination/') == True

def test_resize_negative():
    image_path = './test_images/1.png'
    assert edit_image(image_path, xsize=-60, ysize=-60, new_name='1resized', destination_path='./test_images/test_destination/') == True

def test_rotate():
    image_path = './test_images/1.png'
    assert edit_image(image_path, rotate_degrees=90, new_name='1rotated', destination_path='./test_images/test_destination/') == True

def test_change_format():
    image_path = './test_images/1.png'
    assert edit_image(image_path, destination_format='jpg', new_name='1reformatted', destination_path='./test_images/test_destination/') == True

def test_convert_all_format():
    image_path = './test_images/2.jpg'
    formats = ['png','jpeg','tiff','gif']
    for format in formats:
        assert edit_image(image_path, destination_format=format, new_name='allformats-'+format, destination_path='./test_images/test_destination/') == True

def test_all_together():
    image_path = './test_images/1.png'
    assert edit_image(image_path,  xsize=60, ysize=60, rotate_degrees=90, destination_format='jpeg', new_name='1all_changed', destination_path='./test_images/test_destination/') == True

def test_empty():
    image_path = ''
    assert raises(AttributeError, edit_image, image_path)

def test_invalid_format():
    image_path = './test_images/3.txt'
    assert raises (OSError, edit_image, image_path)
