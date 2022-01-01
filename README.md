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
  <img src="https://latex.codecogs.com/svg.image?\bg_black&space;f(x)&space;=&space;sin(\frac{1}{1-x})&space;" title="\bg_black f(x) = sin(\frac{1}{1-x}) " />
