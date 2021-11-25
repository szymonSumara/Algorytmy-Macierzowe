#ifndef GEN_HPP
#define GEN_HPP

#include <cmath>
#include <vector>
#include <tuple>
#include <algorithm>
#include "Matrix.hpp"

std::vector<double> quad_points(double a, double b, int k){
    std::vector<double> _xs;
    std::vector<double> xs;
    
    if(k == 1)
        _xs = {0};
    else if(k == 2)
        _xs = {-1./std::sqrt(3.), 1./std::sqrt(3.)};
    else if(k == 3)
        _xs = {-std::sqrt(3./5.),
             0,
             std::sqrt(3./5.)};
    else if(k == 4)
        _xs = {-std::sqrt((3.+2.*std::sqrt(6./5.))/7.),
             std::sqrt((3.-2.*std::sqrt(6./5.))/7.),
             std::sqrt((3.-2.*std::sqrt(6./5.))/7.),
             std::sqrt((3.+2.*std::sqrt(6./5.))/7.)};
    else if(k == 5)
        _xs = {-1./3.*std::sqrt(5.+2.*std::sqrt(10./7.)),
        -1./3.*std::sqrt(5.-2.*std::sqrt(10./7.)),
        0.,
        1./3.*std::sqrt(5.-2.*std::sqrt(10./7.)),
        1./3.*std::sqrt(5.+2.*std::sqrt(10./7.))};
    else
        _xs = {-1./3.*std::sqrt(5.+2.*std::sqrt(10./7.)),
        -1./3.*std::sqrt(5.-2.*std::sqrt(10./7.)),
        0.,
        1./3.*std::sqrt(5.-2.*std::sqrt(10./7.)),
        1./3.*std::sqrt(5.+2.*std::sqrt(10./7.))};

    std::transform(_xs.begin(), _xs.end(), std::back_inserter(xs), [a, b](double x) -> double{return 0.5 * (a * (1 - x) + b * (x + 1));});
    return xs;
};

std::vector<double> quad_weights(double a, double b, int k){
    std::vector<double> ws;
    
    if(k == 1)
        ws = std::vector<double>{2.};
    else if(k == 2)
        ws = std::vector<double>{1., 1.};
    else if(k == 3)
        ws = std::vector<double>{5./9.,
            8./9.,
            5./9.};
    else if(k == 4)
        ws = std::vector<double>{(18.-std::sqrt(30.))/36.,
            (18.+std::sqrt(30.))/36.,
            (18.+std::sqrt(30.))/36.,
            (18.-std::sqrt(30.))/36.};
    else if(k == 5)
        ws = std::vector<double>{(322-13.0*std::sqrt(70))/900,
            (322+13.0*std::sqrt(70))/900,
            128/225,
            (322+13.0*std::sqrt(70))/900,
            (322-13.0*std::sqrt(70))/900};
    else
        ws = std::vector<double>{(322.-13.0*std::sqrt(70.))/900.,
            (322.+13.0*std::sqrt(70.))/900.,
            128./225.,
            (322.+13.0*std::sqrt(70.))/900.,
            (322.-13.0*std::sqrt(70.))/900.};

    return ws;
};

double compute_spline(std::vector<double>& knot, int p, int nr, double x){
    auto a = knot[nr];
    auto b = knot[nr+p];
    auto c = knot[nr+1];
    auto d = knot[nr+p+1];

    if(p == 0)
        return (int)(a <= x & x <= d);

    auto lp = compute_spline(knot, p-1, nr, x);
    auto rp = compute_spline(knot, p-1, nr+1, x);

    double y1, y2;

    if(a == b)
        y1 = (int)(a <= x & x <= b);
    else
        y1 = (x-a)/(b-a)*(int)(a <= x & x <= b);

    if(c == d)
        y2 = (int)(c < x & x <= d);
    else
        y2 = (d-x)/(d-c)*(int)(c < x & x <= d);

    return lp*y1 + rp*y2;
}

int compute_p(std::vector<double>& knot){
    int p = 0;
    auto initial = knot[p];
    while(p+2 < knot.size() && initial == knot[p+2])
        p++;

    return p+1;
}

int number_of_elements(std::vector<double>& knot){
    int n = 0;
    auto initial = knot[n];

    for(int i=0; i<knot.size()-1; i++){
        if(knot[i] != initial){
            initial = knot[i];
            n++;
        }
    }

    return n;
}

int number_of_dofs(std::vector<double>& knot, int p){
    return knot.size() - p - 1;
}

std::tuple<double, double> element_boundry(std::vector<double>& knot, int p, int nr){
    auto initial = knot[0];
    int k = 0;
    double low = 0;
    double high = 0;
    
    for(int i=0; i<knot.size(); i++){
        if(knot[i] != initial){
            initial = knot[i];
            k++;
        }
        if(k == nr+1){
            low = knot[i-1];
            high = knot[i];
            break;
        }
    }

    return {low, high};
}

int first_dof_on_element(std::vector<double>& knot, int p, int nr){
    auto [l, h] = element_boundry(knot, p, nr);
    return (knot.rend() - std::find(knot.rbegin(), knot.rend(), l) - 1) - p;
}

std::tuple<int, int> dofs_on_element(std::vector<double>& knot, int p, int nr){
    auto low = first_dof_on_element(knot, p, nr);
    return {low, low+p};
}

Matrix gen(int riga, int nxx, int pxx, int rxx){
    std::vector<double> knot;
    
    if(riga == 0){
        std::vector<double> _knot;

        //simple knot
        for(int i=0; i<pxx; i++)
            _knot.push_back(0);

        for(int i=0; i<=nxx; i++)
            _knot.push_back(i);

        for(int i=0; i<pxx; i++)
            _knot.push_back(nxx);

        std::transform(_knot.begin(), _knot.end(), std::back_inserter(knot), [nxx](double x) -> double{return x/nxx;});
    }else if(riga == 1){
        for(int i=0; i<=pxx; i++)
            knot.push_back(0);
        
        int k = pxx+1;
        for(int i=0; i<nxx; i++){
            knot.push_back(1./nxx*(i+1.));
            knot.push_back(1./nxx*(i+1.));
            k += 2;
        }
        
        for(int i=2*nxx+pxx; i < 2*nxx+2*(pxx+1)-3; i++)
            knot.push_back(1.);
    }else if(riga == 2){
        if(rxx == 0)
            throw std::runtime_error("For riga parameter set to \"2\" the rxx parameter cannot be set to \"0\". Please check parameters passed to \"masslowrank\" function. The function will behave as if the riga parameter was set to \"0\"");
        
        for(int i=0; i<=pxx; i++)
            knot.push_back(0.);

        int k = pxx+1;
        
        for(int i=0; i<nxx; i++){
            knot.push_back(1./nxx*(i+1.));
            k++;
            
            if((i+1) % rxx == 0 && (i+1) != nxx){
                knot.push_back(1./nxx*(i+1.));
                k++;
            }
        }

        for(int i=k-1; i < k+pxx-1; i++)
            knot.push_back(1.);
    }

    auto knot_vectorx = knot;
    auto knot_vectory = knot;

    for(auto& el : knot){
        std::cout<<el<<", ";
    }
    std::cout<<std::endl;

    int px = compute_p(knot_vectorx);
    int py = compute_p(knot_vectory);

    int elementsx = number_of_elements(knot_vectorx);
    int elementsy = number_of_elements(knot_vectory);

    int nx = number_of_dofs(knot_vectorx, px);
    int ny = number_of_dofs(knot_vectory, py);

    Matrix A(nx*ny, nx*ny);
    for(int ex=0; ex<elementsx; ex++){
        auto [xl, xh] = dofs_on_element(knot_vectorx, px, ex);
        auto [ex_bound_l, ex_bound_h] = element_boundry(knot_vectorx, px, ex);

        for(int ey=0; ey<elementsy; ey++){
            auto [yl, yh] = dofs_on_element(knot_vectory, py, ey);
            auto [ey_bound_l, ey_bound_h] = element_boundry(knot_vectory, py, ey);

            auto Jx = ex_bound_h - ex_bound_l;
            auto Jy = ey_bound_h - ey_bound_l;
            auto J = Jx*Jy;

            for(int bi=xl; bi<=xh; bi++){
                for(int bj=yl; bj<=yh; bj++){
                    for(int bk=xl; bk<=xh; bk++){
                        for(int bl=yl; bl<=yh; bl++){
                            auto qpx = quad_points(ex_bound_l, ex_bound_h, 2*px+2*py+1);
                            auto qpy = quad_points(ey_bound_l, ey_bound_h, 2*px+2*py+1);
                            auto qwx = quad_weights(ex_bound_l, ex_bound_h, 2*px+2*py+1);
                            auto qwy = quad_weights(ey_bound_l, ey_bound_h, 2*px+2*py+1);
                        
                            for(int iqx=0; iqx<qpx.size(); iqx++){
                                for(int iqy=0; iqy<qpy.size(); iqy++){
                                    auto funk = compute_spline(knot, px, bi, qpx[iqx]);
                                    auto funl = compute_spline(knot, py, bj, qpy[iqy]);
                                    auto funi = compute_spline(knot, px, bk, qpx[iqx]);
                                    auto funj = compute_spline(knot, py, bl, qpy[iqy]);
                                
                                    auto fun = funi*funj*funk*funl;

                                    auto I = fun*qwx[iqx]*qwy[iqy]*J;
                                    if(I != 0)
                                        A[{bj*nx+bi, bl*nx+bk}] += I;
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    return A;
}

#endif