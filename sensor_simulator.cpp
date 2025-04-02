#include <iostream>
#include <fstream>
#include <chrono>
#include <thread>   
#include <cstdlib>
#include <ctime>

int main() {
    std::ofstream file("sensor_data.txt");
    std::srand(std::time(nullptr));

    if (!file.is_open()) {
        std::cerr << "Failed to open file.\n";
        return 1;
    }

    for (int i = 0; i < 100; ++i) {
        int sensor_value = std::rand() % 100; // Simulate vvalue 0-99
        file << sensor_value << std::endl;
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
    }

    file.close();
    return 0;
}