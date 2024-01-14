# NxN Grid Puzzle Solver

![Alt text](/images/8tile.png)

## Overview
This repository contains a Python implementation for solving an NxN grid puzzle using various search algorithms. The puzzle is a variant of the classic sliding tile puzzle, where the goal is to arrange the tiles in a specific order.

## Features
- **Dynamic Puzzle Size**: Supports puzzles of sizes ranging from 3x3 to 6x6.
- **Multiple Algorithms**: Includes implementations of Breadth-First Search (BFS) and Depth-First Search (DFS) algorithms.
- **Performance Metrics**: Generates reports on the performance of the algorithms, including solution depth and maximum states stored.

## How to Run
1. Ensure Python is installed on your system.
2. Clone the repository: git clone https://github.com/AbdullahAlzeid/NxN-Grid-Puzzle.git
3. Run the `Driver.py` script: python Driver.py
4. Follow the on-screen prompts to select the puzzle size and the algorithm.

## Report Generation
- **Example Algorithm Reports**: Detailed reports of algorithm performance generated by the driver. ([BFS Report](https://github.com/AbdullahAlzeid/NxN-Grid-Puzzle/blob/main/algorithm_report_BFS.txt), [DFS Report](https://github.com/AbdullahAlzeid/NxN-Grid-Puzzle/blob/main/algorithm_report_DFS.txt))
- You can modify the puzzle size and choose the desired algorithm for custom reports

## Algorithms
- **BFS (Breadth-First Search)**: Explores the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.
- **DFS (Depth-First Search)**: Explores as far as possible along each branch before backtracking.
- **IDDFS (Iterative Deepining Depth-First Search)**: is an algorithm that combines the depth-limited searches of DFS with an increasing depth limit until a solution is found.

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/AbdullahAlzeid/NxN-Grid-Puzzle/blob/main/LICENSE) file for details.


