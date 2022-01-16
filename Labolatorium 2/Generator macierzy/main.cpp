#include <iostream>
#include "gen.hpp"
#include<iostream>
#include<fstream>

#include "Matrix.hpp"
int main() {
    std::ofstream file;


    std::string file_name = "3a.csv";
    file.open(file_name);
    Matrix m =gen(0,18,2,0);
    file<<m;
    file.close();
    m = gen(1,19,3,0);
    std::string fem_name = "4a.csv";
    file.open(fem_name);
    file<<m;
    file.close();
    return 0;
}
