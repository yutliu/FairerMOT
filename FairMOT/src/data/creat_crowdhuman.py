import os.path as osp
import os

path_root = '/home/dl/Data/CrowdHuman/images/train/Images'
data_root = '/home/liuyuting/Code/FairMOT_single/src/data/'
path2 = 'CrowdHuman/images/train/Images/'

for filename in os.listdir(path_root):
    datafile_path = osp.join(data_root, '{}'.format('crowdhuman.train'))
    with open(datafile_path, 'a') as f:
        f.write(path2 + filename+'\n')
