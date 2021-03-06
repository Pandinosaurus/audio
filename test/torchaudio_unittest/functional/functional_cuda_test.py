import torch

from torchaudio_unittest import common_utils
from .functional_impl import Lfilter, Spectrogram


@common_utils.skipIfNoCuda
class TestLFilterFloat32(Lfilter, common_utils.PytorchTestCase):
    dtype = torch.float32
    device = torch.device('cuda')


@common_utils.skipIfNoCuda
class TestLFilterFloat64(Lfilter, common_utils.PytorchTestCase):
    dtype = torch.float64
    device = torch.device('cuda')


@common_utils.skipIfNoCuda
class TestSpectrogramFloat32(Spectrogram, common_utils.PytorchTestCase):
    dtype = torch.float32
    device = torch.device('cuda')


@common_utils.skipIfNoCuda
class TestSpectrogramFloat64(Spectrogram, common_utils.PytorchTestCase):
    dtype = torch.float64
    device = torch.device('cuda')
