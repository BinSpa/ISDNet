import os.path as osp

from .builder import DATASETS
from .custom import CustomDataset


@DATASETS.register_module()
class URURDataset(CustomDataset):
    """DRIVE dataset.

    In segmentation map annotation for DRIVE, 0 stands for background, which is
    included in 2 categories. ``reduce_zero_label`` is fixed to False. The
    ``img_suffix`` is fixed to '.png' and ``seg_map_suffix`` is fixed to
    '_manual1.png'.
    """

    
    CLASSES = ("background", "building", "farmland", "greenhouse", "woodland", "bareland", "water", "road")

    PALETTE = [[0, 0, 0], [255, 0, 0], [0, 255, 0], [0, 255, 255], [255, 255, 0], [0, 0, 255], [255, 0, 255], [123, 123, 123]]

    def __init__(self, **kwargs):
        super(URURDataset, self).__init__(
            img_suffix='.png',
            seg_map_suffix='.png',
            reduce_zero_label=False,
            **kwargs)
        assert osp.exists(self.img_dir)
'''
from mmseg.registry import DATASETS
from .basesegdataset import BaseSegDataset

@DATASETS.register_module()
class URURDataset(BaseSegDataset):

    METAINFO = dict(
        classes=("background", "building", "farmland", "greenhouse", "woodland", "bareland", "water", "road"),
        palette=[[0, 0, 0], [255, 0, 0], [0, 255, 0], [0, 255, 255], [255, 255, 0], [0, 0, 255], [255, 0, 255], [123, 123, 123]])

    def __init__(self, img_suffix='.png', seg_map_suffix='.png', **kwargs) -> None:
        super().__init__(img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)
'''