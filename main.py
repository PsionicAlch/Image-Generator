from PIL import Image
from datetime import datetime

import numpy as np

import os
import json


class ImageGenerator:
    ROW, COLUMN, BATCH_SIZE = 600, 800, 100

    def __init__(self) -> None:
        self.pixel_array = list()
        for i in range(0, self.ROW * self.COLUMN):
            self.pixel_array.append(0)

        self.batch_dict = dict()

    def run(self) -> None:
        file_counter = 1
        dir_counter = 1
        current_batch = 0

        while True:
            if current_batch != dir_counter:
                self.log(f"Starting batch {dir_counter}")
                current_batch = dir_counter

            self.pixel_array[0] += 1
            if self.pixel_array[0] > 255:
                for i in range(0, len(self.pixel_array)):
                    if self.pixel_array[i] > 255:
                        self.pixel_array[i] -= 255
                        self.pixel_array[i + 1] += 1

            if self.pixel_array[-1] > 255:
                break

            pa_counter = 0
            img_matrix = np.empty((self.ROW, self.COLUMN))

            for row in range(0, self.ROW):
                for column in range(0, self.COLUMN):
                    img_matrix[row][column] = self.pixel_array[pa_counter]
                    pa_counter += 1

            img = Image.fromarray(img_matrix, "L")
            self.batch_dict[str(file_counter)] = self.pixel_array.copy()

            self.save_img(img, str(file_counter), str(dir_counter))

            img.close()

            file_counter += 1
            if file_counter > self.BATCH_SIZE:
                self.save_batch_dump(dir_counter)
                self.log(f"Finished batch {dir_counter}")
                file_counter = 1
                dir_counter += 1

    def save_img(self, img, name, dir) -> None:
        if not os.path.exists(f"./{dir}"):
            os.makedirs(f"./{dir}")

        img.save(f"./{dir}/{name}.png", format="PNG")

    def save_batch_dump(self, dir) -> None:
        self.log("Starting batch dump.")

        batch_json = json.dumps(self.batch_dict, indent=4)
        with open(f"./{dir}/batch_dump.json", "w") as f:
            f.write(f"{batch_json}\n")

        self.batch_dict = dict()
        self.log("Finished batch dump.")

    def log(self, msg) -> None:
        message = f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S')} - {msg}"

        with open("./log.txt", "a") as f:
            f.write(f"{message}\n")

        print(message)


if __name__ == "__main__":
    img_gen = ImageGenerator()
    img_gen.run()
