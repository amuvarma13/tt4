from scipy.io.wavfile import write
import ljinference
import torch
text = 'Hello world!'
noise = torch.randn(1,1,256).to('cuda' if torch.cuda.is_available() else 'cpu')
wav = ljinference.inference(text, noise, diffusion_steps=7, embedding_scale=1)
write('result.wav', 24000, wav)