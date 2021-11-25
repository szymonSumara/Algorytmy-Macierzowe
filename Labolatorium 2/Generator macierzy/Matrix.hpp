#ifndef MATRIX_HPP
#define MATRIX_HPP

#include <iostream>

struct Index{
    int r;
    int c;

    Index(int r, int c){
        this->r = r;
        this->c = c;
    }
};

struct Matrix{
    double* values;
    int r;
    int c;

    Matrix(int r, int c){
        this->values = new double[r*c];
        for(int i=0; i<r; i++){
            for(int j=0; j<c; j++){
                values[i*c + j] = 0;
            }
        }

        this->r = r;
        this->c = c;
    }

    Matrix(double* values, int r, int c){
        this->values = values;
        this->r = r;
        this->c = c;
    }

    double& operator[](Index index){
        return values[index.r*c + index.c];
    }
};

std::ostream& operator<<(std::ostream& os, Matrix m){
    for(int i=0; i<m.r; i++){
        for(int j=0; j<m.c-1; j++){
            os<<m.values[i*m.c + j]<<",";
            //if(m.values[im.c + j] != 0)
              //  os<<"";
            //else
              //  os<<" ";
        }
        os<<m.values[i*m.c+m.c-1];
        os<<std::endl;
    }

    return os;
}

#endif