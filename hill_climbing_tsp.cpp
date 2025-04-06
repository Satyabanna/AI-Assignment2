#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <cstdlib>
#include <ctime>
#include <chrono>
#include <fstream>
#include "utils.hpp"

std::tuple<std::vector<int>, int, double, int> hillClimbing(std::vector<std::vector<double>>* distanceMatrix) {
    using namespace std::chrono;
    int numCities = distanceMatrix->size();
    std::vector<int> currentSolution(numCities);
    std::iota(currentSolution.begin(), currentSolution.end(), 0);
    std::random_shuffle(currentSolution.begin(), currentSolution.end());

    int bestDistance = compute_path_len(distanceMatrix, &currentSolution);
    std::vector<int> bestSolution = currentSolution;

    int convergenceIteration = 0;
    int iteration = 0;

    auto startTime = high_resolution_clock::now();
    double timeToBest = 0.0;
    bool improved = true;

    while (improved) {
        improved = false;
        for (int i = 0; i < numCities - 1; ++i) {
            for (int j = i + 1; j < numCities; ++j) {
                std::vector<int> newSolution = currentSolution;
                std::swap(newSolution[i], newSolution[j]);
                int newDistance = compute_path_len(distanceMatrix, &newSolution);

                if (newDistance < bestDistance) {
                    bestDistance = newDistance;
                    currentSolution = newSolution;
                    bestSolution = newSolution;
                    improved = true;
                    convergenceIteration = iteration;

                    auto now = high_resolution_clock::now();
                    timeToBest = duration<double>(now - startTime).count();

                    // Save path to frame file
                    std::ofstream frameOut("frames_hc/frame_" + std::to_string(iteration) + ".txt");
                    for (int city : bestSolution) {
                        frameOut << city << " ";
                    }
                    frameOut.close();
                }
                iteration++;
            }
        }
    }

    return {bestSolution, convergenceIteration, timeToBest, iteration};
}

int main() {
    srand(time(NULL));
    int bestKnown;
    auto distanceMatrix = get_matrix("problems/ch130.tsp", &bestKnown);

    int runs = 5;
    double totalTime = 0.0;
    int totalDistance = 0;
    std::vector<double> convergenceTimes;
    std::vector<double> runTimes;

    std::ofstream outFile("hc_convergence.csv");
    outFile << "Run,ConvergenceTime,BestDistance\n";

    for (int i = 0; i < runs; ++i) {
        auto start = std::chrono::high_resolution_clock::now();

        auto [bestTour, convergenceIteration, convergenceTime, totalIterations] = hillClimbing(distanceMatrix);
        int bestDistance = compute_path_len(distanceMatrix, &bestTour);

        auto end = std::chrono::high_resolution_clock::now();
        std::chrono::duration<double> duration = end - start;

        double totalRunTime = duration.count();

        totalTime += totalRunTime;
        totalDistance += bestDistance;
        runTimes.push_back(totalRunTime);
        convergenceTimes.push_back(convergenceTime);

        std::cout << "\nRun " << i + 1
                  << ": Total Runtime = " << totalRunTime << "s"
                  << ", Time to Reach Optimum = " << convergenceTime << "s"
                  << ", Convergence Iteration = " << convergenceIteration
                  << ", Total Iterations = " << totalIterations
                  << ", Best Distance = " << bestDistance << std::endl;

        outFile << i + 1 << "," << convergenceTime << "," << bestDistance << "\n";

        if (totalRunTime > 600) {
            std::cout << "Terminated due to timeout." << std::endl;
            break;
        }
    }

    outFile.close();

    double avgConvergenceTime = std::accumulate(convergenceTimes.begin(), convergenceTimes.end(), 0.0) / convergenceTimes.size();
    double avgRunTime = std::accumulate(runTimes.begin(), runTimes.end(), 0.0) / runTimes.size();

    std::cout << "\n[Hill Climbing Summary]" << std::endl;
    std::cout << "Average Runtime per Run     : " << avgRunTime << "s" << std::endl;
    std::cout << "Average Time to Convergence : " << avgConvergenceTime << "s" << std::endl;
    std::cout << "Average Reward              : " << -1.0 * (totalDistance / (double)runTimes.size()) << std::endl;

    cleanUpMatrix(distanceMatrix);
    return 0;
}
