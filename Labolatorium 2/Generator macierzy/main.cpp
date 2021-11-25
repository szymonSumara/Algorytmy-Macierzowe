#include <iostream>
#include "gen.hpp"
#include<iostream>
#include<fstream>

#include "Matrix.hpp"
int main() {
    std::ofstream file;
    for(int i=20;i<=24;i++){
        std::string S = std::to_string(i);
        std::string file_name = "../iga/"+ S+".csv";
        file.open(file_name);
        Matrix m =gen(0,i,2,0);
        file<<m;
        file.close();
        m =gen(1,i,2,0);
        std::string fem_name = "fem"+ S+".csv";
        file.open(fem_name);
        file<<m;
        file.close();
    }

    return 0;
}