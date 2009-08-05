from pyslic.features.lbp import lbp, _roll_left
import numpy as np
import pyslic
from os.path import dirname
basedir = dirname(__file__)

def test_shape():
    A = np.arange(32*32).reshape((32,32))
    B = np.arange(64*64).reshape((64,64))
    features0 = lbp(A, 3, 12)
    features1 = lbp(B, 3, 12)
    assert features0.shape == features1.shape

def test_nonzero():
    A = np.arange(32*32).reshape((32,32))
    features = lbp(A, 3, 12)
    assert features.sum() > 0

def test_histogram():
    A = np.arange(32*32).reshape((32,32))
    w,h = A.shape
    for r in (2,3,4,5):
        assert lbp(A,r,8).sum() == (w-2*r)*(h-2*r)

def test_roll_left():
    y = 1232
    values = []
    for i in xrange(12):
        y = _roll_left(y, 12)

    assert y == 1232

def test_computefeatures():
    imgdata = basedir+'/data/protimg.jp2'
    imgdata = pyslic.image.io.readimg(imgdata)
    img = pyslic.Image()
    img.channeldata[img.protein_channel] = imgdata
    img.loaded = True
    img.channels[img.protein_channel]='<special>'
    features = pyslic.computefeatures(img,['lbp(8,12)'])
    assert type(features) is np.ndarray