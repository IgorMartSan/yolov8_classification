from ultralytics import YOLO
import os
import numpy as np
import numpy as np

model = YOLO('./runs/classify/train/weights/last.pt')  # load a custom model

image_dir = "C:\\Users\\igor8\\PycharmProjects\\yolov8\\yolov8_classifier_homer_bart\\dados\\test\\bart"

image_files = [file for file in os.listdir(image_dir) if file.endswith('.bmp')]

# Lista todas as imagens no diretório

for image_file in image_files:
    image_path = os.path.join(image_dir, image_file)
    results = model(image_path)
    names_dict = results[0].names
    top1 = results[0].probs.top1
    probs = results[0].probs.data.tolist()
    np.set_printoptions(suppress=True)
    formatted_numbers = np.around(probs, decimals=6)
    print(formatted_numbers)

    print(names_dict)
    print(top1)
    print(formatted_numbers[0])

    # for result in results:
    #     boxes = result.boxes  # Boxes object for bbox outputs
    #     masks = result.masks  # Masks object for segmentation masks outputs
    #     probs = result.probs  # Class probabilities for classification outputs
    #
    #     print(probs.top5)  # The top5 indices of classification, List[Int] * 5.
    #     print(probs.top1[0]) # The top1 indices of classification, a value with Int type.
    #     print(probs.top5conf)  # The top5 scores of classification, a tensor with shape (5, ).
    #     print(probs.top1conf)  # The top1 scores of classification. a value with torch.tensor type.


