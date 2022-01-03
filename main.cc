#include <iostream>
#include "nr3.h"
#include "odeint.h"
#include "ludcmp.h"
#include "stepper.h"
#include "stepperross.h"
#include <fstream>
#include <cmath>
using namespace std;

//==========================================================================================================================

//System of ODEs
struct system_of_ode
    {

	void operator() (const Doub x, VecDoub_I &y, VecDoub_O &dydx)
	{
		dydx[0] = y[1];
		dydx[1] = (2*(y[1])/(1-x)) - y[0]/(pow((1-x),4));
	}

    void jacobian(const Doub x, VecDoub_I &y, VecDoub_O &dfdx,MatDoub_O &dfdy)
    {
	Int n=y.size();
	for (Int i=0;i<n;i++)

	dfdx[i]=0.0;

	dfdy[0][0] = 0;
	dfdy[0][1] = 1;
	dfdy[1][0] = -1/pow((1-x),4);
	dfdy[1][1] = 2/(1-x);

    }
};

// Exact solution of system of ODEs
double f(double x){
    return sin(1/(1-x));
}


int main()
{
	ofstream outFile("data_ode.txt");  // Opens and instantiate a data output file named "data_ode.txt"; in the same directory.

	const Int nvar = 2;  //Number of equations to compute
	const Doub atol=1.0e-16,rtol=1.0e-12, h1=2.9e-11, hmin=0.0, x1=0.0, x2=0.99;  //absolute tolerance (atol), relative tolerance (rtol) , h start (h1) , h minimum (hmin) , integration limits (x1 , x2)
	VecDoub ystart(nvar);

	//Initial conditions
	ystart[0]=0.841470984807897;  // u(0); Sin(1)
	ystart[1]=0.540302305868140;  // v(0); Cos(1)

	Output out(5000);  //the value inside out is the user defined number of points required.
	system_of_ode d;

	Odeint<StepperRoss<system_of_ode> > ode(ystart,x1,x2,atol,rtol,h1,hmin,out,d);
	ode.integrate();

for (Int i=0;i<out.count;i++)
{
	//output to console window
	cout << out.xsave[i] << " " << out.ysave[0][i] << " " << out.ysave[1][i]<< " " << f(out.xsave[i]) - out.ysave[0][i] << " " << endl;
	//write data to data_ode.txt
    outFile << out.xsave[i] << setw(100)<<fixed << setprecision(100) << " " << out.ysave[0][i] << " " << out.ysave[1][i] << " "<< f(out.xsave[i]) - out.ysave[0][i] << " " << endl;

}

cout << endl << out.count << endl;  //displays the number of points output by the program

	outFile.close();  //  Closes the data output file.

	system("Pause");

}
