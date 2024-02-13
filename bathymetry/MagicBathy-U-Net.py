'''
Initial Pytorch Implementation: Panagiotis Agrafiotis (https://github.com/pagraf/MagicBathyNet_Benchmark)
Email: agrafiotis.panagiotis@gmail.com

Description: bathy-u-net.py is a simplified U-Net model modified for estimating water depth from RGB images. 
The model retains the encoder-decoder structure with reduced layers and channels, using skip connections to 
maintain spatial information during depth prediction. It outputs continuous values, suitable for depth estimation,
even with limited annotated data.

If you use this code please cite: ...

MagicBathy-U-Net.py © 2024 by Panagiotis Agrafiotis is licensed under Attribution-NonCommercial-ShareAlike 4.0 International 

This license requires that reusers give credit to the creator. It allows reusers 
to distribute, remix, adapt, and build upon the material in any medium or format,
for noncommercial purposes only. If others modify or adapt the material, they 
must license the modified material under identical terms.


THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''


import torch
import torch.nn as nn
import torch.nn.functional as F

class UNet_bathy(nn.Module):
    def __init__(self, in_channels, out_channels):
        super(UNet_bathy, self).__init__()
        self.n_channels = in_channels
        self.n_outputs = out_channels

        self.encoder = nn.Sequential(
            DoubleConv(in_channels, 32),
            Down(32, 64),
            Down(64, 128),
            Down(128, 256)
        )

        self.decoder = nn.Sequential(
            Up(256, 128),
            Up(128, 64),
            Up(64, 32),
            nn.Conv2d(32, out_channels, kernel_size=1)
        )

    def forward(self, x):
        x1 = self.encoder[0](x)
        x2 = self.encoder[1](x1)
        x3 = self.encoder[2](x2)
        x4 = self.encoder[3](x3)

        x = self.decoder[0](x4, x3)
        x = self.decoder[1](x, x2)
        x = self.decoder[2](x, x1)
        output = self.decoder[3](x)
        
        return output

class DoubleConv(nn.Module):
    def __init__(self, in_channels, out_channels):
        super(DoubleConv, self).__init__()
        self.double_conv = nn.Sequential(
            nn.Conv2d(in_channels, out_channels, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(out_channels, out_channels, kernel_size=3, padding=1),
            nn.ReLU(inplace=True)
        )

    def forward(self, x):
        return self.double_conv(x)

class Down(nn.Module):
    def __init__(self, in_channels, out_channels):
        super(Down, self).__init__()
        self.maxpool_conv = nn.Sequential(
            nn.MaxPool2d(2),
            DoubleConv(in_channels, out_channels)
        )

    def forward(self, x):
        return self.maxpool_conv(x)

class Up(nn.Module):
    def __init__(self, in_channels, out_channels):
        super(Up, self).__init__()
        self.up = nn.ConvTranspose2d(in_channels, out_channels, kernel_size=2, stride=2)
        self.conv = DoubleConv(in_channels, out_channels)

    def forward(self, x1, x2):
        x1 = self.up(x1)
        # Calculate the difference in shape and pad x2 if needed
        diffY = x2.size()[2] - x1.size()[2]
        diffX = x2.size()[3] - x1.size()[3]
        x1 = F.pad(x1, [diffX // 2, diffX - diffX // 2, diffY // 2, diffY - diffY // 2])
        x = torch.cat([x2, x1], dim=1)
        return self.conv(x)

