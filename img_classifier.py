import os
import subprocess
import csv
from settings import IMAGE_DIR


class ImageClassifier(object):
    def ask_type_img(self):
        type_image = input('Type image ... please separate with a comma \n')
        img_labels = type_image.split(',')
        print(img_labels)

    def scan_img_dir(self):
        for f in os.listdir(IMAGE_DIR):
            file_name = os.fsencode(f).decode("utf-8")
            p = subprocess.Popen(["display", IMAGE_DIR + file_name])
            self.ask_type_img()
            p.kill()


if __name__ == '__main__':
    img_c = ImageClassifier()
    img_c.scan_img_dir()