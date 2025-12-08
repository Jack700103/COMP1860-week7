import matplotlib.pyplot as plt
import numpy as np


def draw_segments(segments):
    fig, ax = plt.subplots()
    ax.axis('off')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)

    segment_coords = {
        'a': [(0.5, 0.5), (-0.5, 0.5)],
        'b': [(0.5, 0.5), (0.5, -0.5)],
        'c': [(0.5, -0.5), (0.5, -1)],
        'd': [(-0.5, -1), (0.5, -1)],
        'e': [(-0.5, -0.5), (-0.5, -1)],
        'f': [(-0.5, -0.5), (-0.5, 0.5)],
        'g': [(-0.5, 0), (0.5, 0)]
    }

    for i, seg in enumerate(['a', 'b', 'c', 'd', 'e', 'f', 'g']):
        if segments[i]:
            x = [coord[0] for coord in segment_coords[seg]]
            y = [coord[1] for coord in segment_coords[seg]]
            ax.plot(x, y, linewidth=5, color='black')


def read_output_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        last_line = lines[-1].strip()
        segments = [int(bit) for bit in last_line.split(' ')[1:]]
        return segments


if __name__ == "__main__":
    output_file_path = "simulator_output.txt" 
    segments = read_output_file(output_file_path)
    draw_segments(segments)
    plt.show()
