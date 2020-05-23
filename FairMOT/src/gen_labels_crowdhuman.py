import os.path as osp
import json
import os
import cv2



def mkdirs(d):
    if not osp.exists(d):
        os.makedirs(d)


seq_root = '/home/dl/Data/CrowdHuman/images/train/'
label_root = '/home/dl/Data/CrowdHuman/labels_with_ids/train'

human_root_path = '/home/dl/Data/CrowdHuman'
odgt_path = os.path.join(human_root_path, 'annotation_train.odgt')

mkdirs(label_root)
seqs = [s for s in os.listdir(seq_root)]

for seq in seqs:
    seq_label_root = osp.join(label_root, seq)
    mkdirs(seq_label_root)
    with open(odgt_path, 'r') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            line = json.loads(lines[i])
            name = line['ID'] + '.jpg'
            image_path = os.path.join(seq_root, 'Images', name)
            image = cv2.imread(image_path)
            picture_h = image.shape[0]
            picture_w = image.shape[1]

            allbboxs = line['gtboxes']
            for j in range(len(allbboxs)):
                if allbboxs[j]['tag'] != 'person':
                    continue
                bbox = allbboxs[j]['hbox']
                x, y, w, h = bbox
                if x < 0:
                    x = 0
                if y < 0:
                    y = 0

                x += w / 2
                y += h / 2
                label_fpath = osp.join(seq_label_root, '{}.txt'.format(line['ID']))
                label_str = '0 -1 {:.6f} {:.6f} {:.6f} {:.6f}\n'.format(
                    x / picture_w, y / picture_h, w / picture_w, h / picture_h)
                with open(label_fpath, 'a') as f:
                    f.write(label_str)