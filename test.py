from scipy.io.wavfile import write
import msinference
import torch
text = 'Hello world!'
voice = msinference.compute_style('result.wav')
wav = msinference.inference(text, voice, alpha=0.3, beta=0.7, diffusion_steps=7, embedding_scale=1)
write('result.wav', 24000, wav)