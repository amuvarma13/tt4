from scipy.io.wavfile import write
import ljinference
import torch
text = 'Hello this the lj inference test.'
noise = torch.randn(1,1,256).to('cuda' if torch.cuda.is_available() else 'cpu')
wav = ljinference.inference(text, noise, diffusion_steps=7, embedding_scale=1)
write('resultlj.wav', 24000, wav)