from PIL import Image
import warnings

def edit_image(image_path, new_name='', destination_path='./', xsize=0, ysize=0, rotate_degrees=0, destination_format=''):
    if image_path == '':
        raise AttributeError("Input path cannot be empty. Please, verify that the path is correct")
    try:
        img = Image.open(image_path)
        if new_name == '':
            img_name = image_path.split('/')[-1].split('.')[0]
        else:
            img_name = new_name
        if destination_format == '':
            img_format = '.'+image_path.split('/')[-1].split('.')[-1]
        else:
            img_format = destination_format
        if '.' not in img_format:
            img_format='.'+img_format
        img_width, img_height = img.size
        resize = False
        if xsize > 0:
            img_width = xsize
            resize = True
        if ysize > 0:
            img_height = ysize
            resize = True
        if ysize < 0 or xsize < 0:
            warnings.warn("Resize value below zero. Cannot resize to negative. Considering 0 instead. Please verify input later.", SyntaxWarning)
        if resize:
            img = img.resize((img_width, img_height))
        if rotate_degrees > 0:
            img = img.rotate(rotate_degrees)
        file_path = destination_path+img_name+img_format
        if 'jp' in img_format.lower():
            img = img.convert('RGB')
        img.save(file_path)
        return True
    except OSError as e:
        raise OSError("Problems in identifying the format. Please, ensure that the file format is jpeg, png, tiff or gif."+str(e))
    except IOError as e:
        raise IOError("Problems in reading the image form path or writing file, please verify that the permissions and path are correct. Original error: "+str(e))
    except IndexError:
        raise AttributeError("The specified image path is not correct. Please, ensure a correctly named file input, including extension name.")
