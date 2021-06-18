import os
import torch
import numpy as np
from skimage.color import lab2rgb
from torchvision import transforms
from torchvision.models.resnet import resnet18
from fastai.vision.learner import create_body
from fastai.vision.models.unet import DynamicUnet

def pretrained_generator(size, in_channels, out_channels, backbone, cut):
    body = create_body(backbone, in_channels, True, cut)

    return DynamicUnet(body, out_channels, (size, size))

def lab_to_rgb(L, ab):
    L = (L + 1.) * 50
    ab = ab * 110.

    Lab = torch.cat([L, ab], 1).permute(0, 2, 3, 1).cpu().numpy()

    rgb_imgs = []
    for lab_img in Lab:
        rgb_img = lab2rgb(lab_img)
        rgb_imgs.append(rgb_img)

    return np.stack(rgb_imgs, 0)

def image_to_tensor(img):
    tensor_img = 2 * (transforms.ToTensor()(img))[0] - 1
    tensor_img = tensor_img.view(1, 1, *tensor_img.shape)

    return tensor_img

def predict(tensor):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    g = pretrained_generator(256, 1, 2, resnet18, -2)
    g.load_state_dict(torch.load(os.path.join(os.path.dirname(os.path.dirname(__file__)),"main\\g.pt"), map_location=device))

    return g(tensor)