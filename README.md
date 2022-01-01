# A Numerical Recipes Project
Solving a Stiff System of ODEs using Rosenbrock Method.

*By [Amirhossein Rezaei](https://www.researchgate.net/profile/Amirhossein-Rezaei-2?ev=hdr_xprf&_sg=QEXFYpE24Sa1_XWjefMs8mb3F8TnZVp0Abqt0MAtKbsNDbPvvFEcCKXxU4pw3NrLhBWN-s2al6MeUOsBC3kvD8Cd)*

*Advisor: [Prof. Siamak Gousheh](https://www.researchgate.net/profile/S-Gousheh?_sg=WoqxMgpDwczLNu4HdADavg55gAD44iEgchW-FHcMt4k9-hMptQsGIovVpgQ1tr1Z1_AwsrfjS6RaNYs_vunikRrerJaR7fnt)*
   
### A note on header files and compiling:
1. Install the latest version of [Microsoft Visual Studio C/C++](https://visualstudio.microsoft.com/vs/features/cplusplus/).
2. Open headers and copy all the files into the include directory of VS under "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.30.30705\include\"
3. Now open Microsoft Visual Studio: Continue without code > Tools > Command Line > Developer Command Prompt
4. Go to the directory of main.cc file (or whatever you name your new editted file) using cd command (path is the full name of the main.cc directory): ``` cd "path" ```
5. Compile the file using CL command: ``` CL main.cc``` 
6. Run the file: ```main```

### NR (Rosenbrock method)

<p align="middle">
   <img src=https://github.com/amirh0ss3in/A-Numerical-Recipes-Project---Solving-a-Stiff-system-of-ODEs-using-Rosenbrock-method/blob/main/Images/NR/u.svg width="350" title="hover text">
   <img src=https://github.com/amirh0ss3in/A-Numerical-Recipes-Project---Solving-a-Stiff-system-of-ODEs-using-Rosenbrock-method/blob/main/Images/NR/v.svg width="350" title="hover text">
   <img src=https://github.com/amirh0ss3in/A-Numerical-Recipes-Project---Solving-a-Stiff-system-of-ODEs-using-Rosenbrock-method/blob/main/Images/NR/difference.svg width="350" title="hover text">
</p>


### Python (SciPy's LSODA Method)
   
<p align="middle">
   <img src=https://github.com/amirh0ss3in/A-Numerical-Recipes-Project---Solving-a-Stiff-system-of-ODEs-using-Rosenbrock-method/blob/main/Images/Python/u.svg width="350" title="hover text">
   <img src=https://github.com/amirh0ss3in/A-Numerical-Recipes-Project---Solving-a-Stiff-system-of-ODEs-using-Rosenbrock-method/blob/main/Images/Python/v.svg width="350" title="hover text">
   <img src=https://github.com/amirh0ss3in/A-Numerical-Recipes-Project---Solving-a-Stiff-system-of-ODEs-using-Rosenbrock-method/blob/main/Images/Python/difference.svg width="350" title="hover text">
<p>

 ### Equations
   <p align="middle">
<img src="https://latex.codecogs.com/svg.image?\inline&space;\\&space;f(x)&space;=&space;sin(\frac{1}{1-x})&space;\\\\&space;f'(x)&space;=&space;\frac{cos(\frac{1}{1-x})}{(1-x)^2}&space;\\&space;&space;\\&space;f''(x)&space;=&space;\frac{2&space;cos(\frac{1}{1-x})}{(1-x)^3}&space;-&space;\frac{sin(\frac{1}{1-x})}{(1-x)^4}&space;\\&space;\\\left\{\begin{matrix}&space;u(x)&space;=&space;f'(x)&space;\\&space;v(x)&space;=&space;f''(x)\end{matrix}\right.\to&space;\left\{\begin{matrix}&space;u(0)&space;=&space;sin(1)&space;\\&space;v(0)&space;=&space;cos(1)\end{matrix}\right.\\\\\boxed{&space;&space;\!\begin{aligned}&space;&space;&u'(x)&space;=&space;v\\&space;&space;&v'(x)&space;=&space;\frac{2v}{1-x}&space;-&space;\frac{u}{(1-x)^4}&space;&space;\end{aligned}}" title="\inline \\ f(x) = sin(\frac{1}{1-x}) \\\\ f'(x) = \frac{cos(\frac{1}{1-x})}{(1-x)^2} \\ \\ f''(x) = \frac{2 cos(\frac{1}{1-x})}{(1-x)^3} - \frac{sin(\frac{1}{1-x})}{(1-x)^4} \\ \\\left\{\begin{matrix} u(x) = f'(x) \\ v(x) = f''(x)\end{matrix}\right.\to \left\{\begin{matrix} u(0) = sin(1) \\ v(0) = cos(1)\end{matrix}\right.\\\\\boxed{ \!\begin{aligned} &u'(x) = v\\ &v'(x) = \frac{2v}{1-x} - \frac{u}{(1-x)^4} \end{aligned}}" />
      
<\p>
