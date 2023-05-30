#FPP:       1: 'Pedestrian', 2: 'Car', 3: 'Cyclist'
import os

def extract_code_from_path(path):
    # 使用os模块的split方法获取文件名和扩展名
    _, filename_ext = os.path.split(path)
    # 使用os模块的splitext方法获取文件名和扩展名的分离形式
    filename, _ = os.path.splitext(filename_ext)
    # 使用split方法根据斜杠/分割路径，获取最后一部分作为通用代码
    code = filename.split('/')[-1]
    return code




def convert_to_kitti_format(input_file,output_path):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip().split(' ')
        image_path = line[0]
        image_idx = extract_code_from_path(image_path)
        with open("{}/{}.txt".format(output_path,image_idx), 'w') as f:
            label_idx = line[1]
            print("label_idx = {} \n".format(label_idx))
            if (label_idx=='1'):
                class_name = 'Pedestrian'
            elif (label_idx=='2'):
                class_name = 'Car'
            elif (label_idx=='3'):
                class_name = 'Cyclist'
            confidence = line[2]
            x_min = line[3]
            y_min = line[4]
            x_max = line[5]
            y_max = line[6]

            kitti_line = f"{class_name} 0 0 0 {x_min} {y_min} {x_max} {y_max} 0 0 0 0 0 0 0 {confidence}"
            f.write(kitti_line)


input_file = 'rgb_detection_train.txt'
output_path = 'fpp_rgbdetct_2_kitti_result/'
convert_to_kitti_format(input_file,output_path)
