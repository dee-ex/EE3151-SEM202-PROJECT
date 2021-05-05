import torch
from PIL import Image
import matplotlib.pyplot as plt

img = Image.open("input_image_name")

t = 2*(transforms.ToTensor()(img))[0] - 1
t = torch.unsqueeze(torch.unsqueeze(t, 0), 0).to(device)


output = G(t)

out_img = lab_to_rgb(t, output.detach())

plt.axis("off")
plt.imshow(out_img[0])