# Chapter 5: Integrals and Derivatives

##### Exercise 5.1
This program creates an object called `TrapeziumRuleIntegration`, this object has two methods:
`function_integration`: this method performs an integration on a user-defined global method `f(x)` define before the execution of this object's method.
Within the parameters of this method, one must provide the limits of integration and the number of slices for integration. the more slices the more accurate but the longer it will take to solve. 
`data_integration`: this method performs an integral over the given dataset. Besides providing the dataset, one must specify the number of slices. The maximum amount of slices is the number of data points themselves, this choice then gives the maximum accuracy for the data provided but may take the longest, one may, in turn, provide a smaller amount of slices but accuracy will be sacrificed in the interest of expediency.
##### Exercise 5.2
This program creates a version of Simpson's Rule of integration to compare its accuracy with that of the Trapezoidal/Trapezium integration method. (this program calls in the Integration_Method file to make use of the Trapezium integration method for comparizon.) This object for Simpson's rule behaves in an identical manner to `TrapesiumRuleIntegration`
##### Exercise 5.3
This program calculates and plots the specified integral using Simpsons Rule
##### Exercise 5.4
This program calculates the Bessel function as well as the intensity of light defraction pattern using Simpson's Rule, then creates a grid of values and these are then plotted using the value to image rendering tool `np.imshow()`.
##### Exercise 5.5
This is a pen and paper derivation of the Simpsons Rule error. Thus it is not featured here.
##### Exercise 5.6
This program illustrateas a way to result of calculating the error from integration methods. most of the work was done on the file IntegrationMethods.py to make every object be able to calculate its own error. Note that this error is not the totality of the error in the calculation since rounding error also should be taken into account. The changes made for this exercise calculate the integration error only.
##### Exercise 5.7
This program makes use of an adaptive method of integration that has been built into the `TrapeziumRuleIntegration` object from the IntegrationMethods file in the form of the `adaptive_function_integration` method; as well as the `romberg_function_integration` method from the same object. It demonstrates how the Romberg integration method (an extension of the Trapezium method) becomes more accurate in smaller amount of slices than the regular Trapezium method, if and only if the function is well behaved.
##### Exercise 5.8
This program is an extension of the provious one but instead it uses an adaptive method based on Simpson's Rule of integration. The amount of slices nessesary for this method falls in between Romberg and regular Trapezium. 
##### Exercise 5.9
This program makes use of the Gaussian Quadrature integration method to calculate the heat capacity of a solid and makes a graph of the heat capacity change from 5 to 500 kelvin.
##### Exercise 5.10
This program solves the period for an enharmonic oscilator. it uses the gaussian quadrature method and graphs it.
##### Exercise 5.11
This program solves for the intensity of a wave after it has passed a corner and it has been changed. It uses a gaussian quadrature to calculate it before graphing it.
##### Exercise 5.12
The program solves for the radiation per unit area by a black body and it uses the gaussian quadrature to solve. once this is done, the solution is checked by calculating the Stefan Boltzmann constant and judge the accuracy of the program and the method.
##### Exercise 5.13
This program calculates solutions to the the quantum well problem and graphs them. The way this program goes about calculating using regression is not optimal and could be improved. It also shows at this point and time the limitations of my personal library `IntegrationMethods` since it cannot take in functions such as `quatum_well()` as it is nessesary for this type of problems.

### Disclaimer
The Exercises remaining in this chapter have been put on hold. It has become obvious to me that `IntegrationMethods` is in need of being refactored and re-writen, and I will take the opportunity to add the possibility of being able to do multi-variable integrals as well as derivatives. Since this will take a while, (and it has taken a while) I have decided to revisit this section later on. As of this writing, the new file housing the integration objects and future derivation objects will be `integralsandderivatives`. 
##### Exercise 5.14
##### Exercise 5.15
##### Exercise 5.16
##### Exercise 5.17
##### Exercise 5.18
##### Exercise 5.19
##### Exercise 5.20
##### Exercise 5.21
##### Exercise 5.22
##### Exercise 5.23



##### IntegrationMethods
I created this file to house the integration methods I code from the mathematical definitions found in the book.
It uses the external package "Equations" by glenfletcher, that can be found [here](https://pypi.org/project/Equation/#description), to support the use of equations to be evaluated. 

NOTE: The original versions for these integration methods only work in their respective files while the versions written in this file can be imported and used externally.

Update: The objects housed in this file are:
- `TrapesiumRuleIntegration`: Its maximum accuracy before rounding error is dominant is 10^8 slices. If the function is well behaved, the best estimates will be given by `romberg_function_integration`.
- `SimpsonsRuleIntegration`: Its maximum accuracy before rounding error is dominant is 10,000 slices and requires an even number of slices.
- `GaussianQuadrature`: it can estimate polynomial exactly and can have really good estimates quickly with a small amount of points of integration, it is especially useful when calculating an answer and cannot afford to use large numbers of points. It cannot be used for adaptive integration due to its nature of having non-uniform weighted points as the bases for the aproximation.

It also includes the global method `equation` which is used to house the functions before being pased to the integrating objects.


###### Link to all exercise questions in this chapter can be found [here](http://www-personal.umich.edu/~mejn/cp/exercises.html)