
import numpy as np
from matplotlib import pyplot as plt
import math
from sklearn import neighbors
import os
import os.path
import pickle
from PIL import Image, ImageDraw
import face_recognition
from face_recognition.face_recognition_cli import image_files_in_folder
import cv2



ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def train(train_dir, model_save_path=None, n_neighbors=None, knn_algo='ball_tree', verbose=False):
    
    X = []
    y = []

    # 读取人员路径
    for class_dir in os.listdir(train_dir):
        if not os.path.isdir(os.path.join(train_dir, class_dir)):
            continue

        # 读取当前人员的人脸图片
        for img_path in image_files_in_folder(os.path.join(train_dir, class_dir)):
            # 加载图片
            image = face_recognition.load_image_file(img_path)
            # 人脸检测
            face_bounding_boxes = face_recognition.face_locations(image)

            if len(face_bounding_boxes) != 1:
                # 没有人就跳过当前图片
                if verbose:
                    print("Image {} not suitable for training: {}".format(img_path, "Didn't find a face" if len(
                        face_bounding_boxes) < 1 else "Found more than one face"))
            else:
                # 保存人脸特征和类别
                X.append(face_recognition.face_encodings(image, known_face_locations=face_bounding_boxes)[0])
                y.append(class_dir)

    # 自定设置n_neighbors
    if n_neighbors is None:
        n_neighbors = int(round(math.sqrt(len(X))))
        if verbose:
            print("Chose n_neighbors automatically:", n_neighbors)

    # 训练KNN分类器
    knn_clf = neighbors.KNeighborsClassifier(n_neighbors=n_neighbors, algorithm=knn_algo, weights='distance')
    knn_clf.fit(X, y)

    # 保存分类器
    if model_save_path is not None:
        with open(model_save_path, 'wb') as f:
            pickle.dump(knn_clf, f)

    return knn_clf


def predict(X_img_path, knn_clf=None, model_path=None, distance_threshold=0.3):
    
    if not os.path.isfile(X_img_path) or os.path.splitext(X_img_path)[1][1:] not in ALLOWED_EXTENSIONS:
        raise Exception("Invalid image path: {}".format(X_img_path))

    if knn_clf is None and model_path is None:
        raise Exception("Must supply knn classifier either thourgh knn_clf or model_path")

    # 加载模型
    if knn_clf is None:
        with open(model_path, 'rb') as f:
            knn_clf = pickle.load(f)

    # 读取图片和进行人脸检测
    X_img = face_recognition.load_image_file(X_img_path)
    X_face_locations = face_recognition.face_locations(X_img)

    # 如果没有检测到人脸就返回空list
    if len(X_face_locations) == 0:
        return []

    # 提取人脸特征
    faces_encodings = face_recognition.face_encodings(X_img, known_face_locations=X_face_locations)

    # 使用K近邻进行分类
    closest_distances = knn_clf.kneighbors(faces_encodings, n_neighbors=1)
    are_matches = [closest_distances[0][i][0] <= distance_threshold for i in range(len(X_face_locations))]

    # 返回预测结果
    return [(pred, loc) if rec else ("unknown", loc) for pred, loc, rec in
            zip(knn_clf.predict(faces_encodings), X_face_locations, are_matches)]


def show_prediction_labels_on_image(img_path, predictions):
    
    pil_image = Image.open(img_path).convert("RGB")
    draw = ImageDraw.Draw(pil_image)

    for students_id, (top, right, bottom, left) in predictions:
        # 画框
        draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

        # 设置名字，需要用uft-8编码
        students_id = students_id.encode("UTF-8")
        # 标注人名
        text_width, text_height = draw.textsize(students_id)
        draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
        draw.text((left + 6, bottom - text_height - 5), students_id, fill=(255, 255, 255, 255))

    del draw

    # jupyter 绘图
    # pil_image.show()
    plt.imshow(pil_image)
    plt.axis('off')
    plt.show()


def capture_image():
    video = cv2.VideoCapture(0)  # 调用摄像头，PC电脑中0为内置摄像头，1为外接摄像头
    judge = video.isOpened()  # 判断video是否打开
    while judge:
        ret, frame = video.read()
        cv2.imshow("frame", frame)
        keyword = cv2.waitKey(1)
        if keyword == ord('s'):  # 按s保存当前图片
            cv2.imwrite('./test_img/knn_examples/test/test.jpg', frame)
        elif keyword == ord('q'):  # 按q退出
            break

    # 释放窗口
    video.release()
    cv2.destroyAllWindows()
