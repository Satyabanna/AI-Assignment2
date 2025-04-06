import matplotlib
matplotlib.use("Agg")  

import matplotlib.pyplot as plt
from matplotlib import collections as mc
from PIL import Image
import os
import glob


# Load coordinates from .tsp file
def load_coordinates(filepath):
    coords = {}
    with open(filepath, 'r') as file:
        for line in file:
            if line.strip().isdigit():
                continue
            parts = line.strip().split()
            if len(parts) == 3:
                try:
                    index = int(parts[0])
                    x, y = float(parts[1]), float(parts[2])
                    coords[index - 1] = (x, y)
                except:
                    continue
    return coords

# Plot tour
def plot_tour(tour, coords, save_path):
    lines = []
    for i in range(len(tour)):
        a = coords[tour[i]]
        b = coords[tour[(i + 1) % len(tour)]]
        lines.append([a, b])

    lc = mc.LineCollection(lines, linewidths=2, colors='blue')
    fig, ax = plt.subplots()
    ax.add_collection(lc)
    ax.autoscale()
    ax.margins(0.1)
    plt.axis('off')
    plt.savefig(save_path, bbox_inches='tight')
    plt.close()

# Generate images from tour files
def generate_images(frames_dir, output_dir, tsp_file):
    coords = load_coordinates(tsp_file)
    os.makedirs(output_dir, exist_ok=True)

    for frame_file in sorted(os.listdir(frames_dir), key=lambda x: int(x.split('_')[1].split('.')[0])):
        with open(os.path.join(frames_dir, frame_file), 'r') as f:
            tour = list(map(int, f.read().strip().split()))
            save_path = os.path.join(output_dir, frame_file.replace('.txt', '.png'))
            plot_tour(tour, coords, save_path)
    print(f"Images saved to {output_dir}")

# Create GIF from images
def create_gif(image_dir, output_path, duration=100):
    image_files = sorted(glob.glob(f"{image_dir}/*.png"), key=os.path.getmtime)
    images = [Image.open(img) for img in image_files]
    images[0].save(output_path, save_all=True, append_images=images[1:], duration=duration, loop=0)
    print(f"GIF saved to {output_path}")

# MAIN
if __name__ == "__main__":
    tsp_file = "problems/ch130.tsp"

    # For Simulated Annealing
    generate_images("frames_sa", "images_sa", tsp_file)
    create_gif("images_sa", "gifs/sa.gif")

    # For Hill Climbing
    generate_images("frames_hc", "images_hc", tsp_file)
    create_gif("images_hc", "gifs/hc.gif")
