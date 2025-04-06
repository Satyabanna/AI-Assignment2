#  TSP Solver: Simulated Annealing & Hill Climbing

This project implements and compares two metaheuristic algorithms for solving the **Travelling Salesman Problem (TSP)**:

-  **Simulated Annealing**
-  **Hill Climbing**

Both algorithms visualize their convergence behavior and generate animated `.gif` files to show how the tour improves over time.

---

## 📁 Project Structure and File Descriptions

| File/Folder            | Description |
|------------------------|-------------|
| `hill_climbing_tsp.cpp`| C++ implementation of the Hill Climbing algorithm for TSP. Saves `.tour` files per iteration to generate frames. |
| `sa_tsp.cpp`           | C++ implementation of the Simulated Annealing algorithm for TSP. Also saves `.tour` files per iteration. |
| `hc_convergence.csv`   | Stores convergence time and best distance for each Hill Climbing run. Used for plotting performance graphs. |
| `sa_convergence.csv`   | Stores convergence time and best distance for each Simulated Annealing run. |
| `plot_time.py`         | Python script to read the CSV files and plot the average time to reach optimum solution. |
| `generate_gif.py`      | Python script to convert saved `.tour` files into images, then create `.gif` animations showing algorithm progress. |
| `frames_sa/`           | Contains `.tour` files generated during Simulated Annealing runs (one per iteration). |
| `frames_hc/`           | Contains `.tour` files from Hill Climbing runs. |
| `images_sa/`           | PNG images of tours for each Simulated Annealing iteration. |
| `images_hc/`           | PNG images for Hill Climbing iterations. |
| `gifs/`                | Contains the final animated `.gif` files showing tour evolution for both algorithms. |

---

##  How to Run
Compile and Run the Algorithms

Ensure every file is in correct directories and the TSP input file (e.g., `tsp_data.txt`) is properly formatted.

1) For Simulated Annealing:

```bash
g++ sa_tsp.cpp -o sa_tsp
./sa_tsp

2) For Hill climbing:

```bash
g++ hill_climbing_tsp.cpp -o hill_climbing_tsp
./hill_climbing_tsp

3) generate_gif.py is for analysing each and every frame of the respective algorithm and then making into gif. 

4) these files are little dependent on the existing files from the cloned repo.

5) Requirements
C++ compiler (e.g., g++)

Python 3.x

Python packages:

matplotlib

pandas

imageio

