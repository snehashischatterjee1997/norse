import torch

from .lif import LIFState, LIFFeedForwardState
from .lif_mc import lif_mc_step, lif_mc_feed_forward_step


def lif_mc_step_test():
    x = torch.ones(20)
    s = LIFState(z=torch.zeros(10), v=torch.zeros(10), i=torch.zeros(10))
    input_weights = torch.randn(10, 20).float()
    recurrent_weights = torch.randn(10, 10).float()
    g_coupling = torch.randn(10, 10).float()

    for _ in range(100):
        _, s = lif_mc_step(x, s, input_weights, recurrent_weights, g_coupling)


def lif_mc_feed_forward_step_test():
    x = torch.ones(10)
    s = LIFFeedForwardState(v=torch.zeros(10), i=torch.zeros(10))
    g_coupling = torch.randn(10, 10).float()

    for _ in range(100):
        _, s = lif_mc_feed_forward_step(x, s, g_coupling)
