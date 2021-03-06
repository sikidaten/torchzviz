import torch

from zviz import Zviz


# Your model can handle multiple in/out!
class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.conv = torch.nn.Conv2d(3, 3, 3)
        self.conv1 = torch.nn.Conv2d(3, 3, 3)

    def forward(self, x,y):
        return [self.conv(x), self.conv1(y)]


conv0 = Model()
criteorion = torch.nn.MSELoss()
criteorion1 = torch.nn.MSELoss()
zviz = Zviz({'conv0': conv0, 'mseloss': criteorion, 'mseloss1': criteorion1})
zviz.setoptimizer(torch.optim.Adam(conv0.parameters()), 'conv0')
data0 = torch.randn(3, 3, 256, 256)
data1 = torch.randn(3, 3, 256, 256)
out, out1 = conv0(data0,data1)
loss = criteorion(out, torch.zeros(1)) + criteorion1(out1, torch.zeros(1))
zviz.backward(loss)
zviz.step('conv0')
zviz.zero_grad('conv0')
