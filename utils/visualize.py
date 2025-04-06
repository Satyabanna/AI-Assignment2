import imageio
import os

def save_gif(frames, path, filename):
    os.makedirs(path, exist_ok=True)
    output_path = os.path.join(path, filename)
    imageio.mimsave(output_path, frames, fps=1)
    print(f"[+] Saved gif to {output_path}")
