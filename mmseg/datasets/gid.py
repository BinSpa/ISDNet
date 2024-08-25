import os.path as osp

from .builder import DATASETS
from .custom import CustomDataset


@DATASETS.register_module()
class GIDDataset(CustomDataset):
    """DRIVE dataset.

    In segmentation map annotation for DRIVE, 0 stands for background, which is
    included in 2 categories. ``reduce_zero_label`` is fixed to False. The
    ``img_suffix`` is fixed to '.png' and ``seg_map_suffix`` is fixed to
    '_manual1.png'.
    """

    
    CLASSES = ('unlabeled', 'built-up', 'farmland', 'forest', 'meadow', 'water')

    PALETTE = [[0, 0, 0], [255, 0, 0], [0, 255, 0], [0, 255, 255], [255, 255, 0], [0, 0, 255]]

    def __init__(self, **kwargs):
        super(GIDDataset, self).__init__(
            img_suffix='.tif',
            seg_map_suffix='_5label.png',
            reduce_zero_label=False,
            **kwargs)
        assert osp.exists(self.img_dir)

'''
@DATASETS.register_module()
class GIDDataset(BaseSegDataset):

    METAINFO = dict(
        classes=('unlabeled', 'built-up', 'farmland', 'forest', 'meadow', 'water'),
        palette=[[0, 0, 0], [255, 0, 0], [0, 255, 0], [0, 255, 255], [255, 255, 0], [0, 0, 255]])

    def __init__(self, img_suffix='.tif', seg_map_suffix='_5label.png', **kwargs) -> None:
        super().__init__(img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)
'''