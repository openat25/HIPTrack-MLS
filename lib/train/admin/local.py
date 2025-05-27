class EnvironmentSettings:
    def __init__(self):
        self.workspace_dir = '/home/lsw/LSW/2024/CVPR/HIPTrack-MLS'    # Base directory for saving network checkpoints.
        self.tensorboard_dir = '/home/lsw/LSW/2024/CVPR/HIPTrack-MLS/tensorboard'    # Directory for tensorboard files.
        self.pretrained_networks = '/home/lsw/LSW/2024/CVPR/HIPTrack-MLS/pretrained_networks'
        self.lasot_dir = '/media/lsw/data/LaSOT/lasot'
        self.got10k_dir = '/media/lsw/data/GOT-10k/train'
        self.got10k_val_dir = '/media/lsw/data/GOT-10k/val'
        self.lasot_lmdb_dir = '/media/lsw/LaSOT/lasot_lmdb'
        self.got10k_lmdb_dir = '/media/lsw/data/got10k_lmdb'
        self.trackingnet_dir = '/media/lsw/data/trackingnet'
        self.trackingnet_lmdb_dir = '/media/lsw/data/trackingnet_lmdb'
        self.coco_dir = '/media/lsw/data/coco/coco'
        self.coco_lmdb_dir = '/media/lsw/data/coco/coco_lmdb'
        self.lvis_dir = ''
        self.sbd_dir = ''
        self.imagenet_dir = '/home/lsw/LSW/2024/CVPR/HIPTrack-MLS/data/vid'
        self.imagenet_lmdb_dir = '/home/lsw/LSW/2024/CVPR/HIPTrack-MLS/data/vid_lmdb'
        self.imagenetdet_dir = ''
        self.ecssd_dir = ''
        self.hkuis_dir = ''
        self.msra10k_dir = ''
        self.davis_dir = ''
        self.youtubevos_dir = '/media/lsw/data/GOT-10k/train/list.txt'
