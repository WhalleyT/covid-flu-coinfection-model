library(deSolve)
library(pracma)

coinfection_model <- function(Pi_E = 5e7, mu_E = 0.5, beta1 = 2e-8, mu_1 = 1, kappa1 = 5e-4, N1 = 151, theta_x = 100,
                              mu_c = 1.8, Pi_tc= 1e5, r_tc = 0.1, psi_tc = 10, mu_tc= 0.34, r_x = 10, beta2 = 5.4e-9,
                              mu_2 = 0.5, kappa2 = 2e-3, N2 = 1.2e4,mu_i = 1, Pi_ti = 5e5, r_ti = 0.1, psi_ti = 30, 
                              mu_ti = 0.33, psi_x = 1e5, y0 = NULL, start = 0, end = 10) {
  
  f <- function(t, y) {
    as.matrix(c(Pi_E - beta1*y[1]*y[3] - beta2*y[1]*y[5] - mu_E*y[1], 
                beta1*y[1]*y[3] - mu_1*y[2] - kappa1*y[2]*y[6], 
                N1*mu_1*y[2]*(1 - y[8]/(theta_x + y[8])) - mu_c*y[3], 
                beta2*y[1]*y[5]-mu_2*y[4]-kappa2*y[4]*y[7], 
                N2*mu_2*y[4]*(1 - y[8]/(theta_x + y[8])) - mu_i*y[5], 
                Pi_tc + r_tc*y[2]/(psi_tc + y[2]) - mu_tc*y[6], 
                Pi_ti + r_ti* y[4]/(psi_ti + y[4]) - mu_ti*y[7],
                r_x*((y[2] + y[4])/(psi_x + y[2] + y[4]) - y[8])))
  }
  
  sol <- ode78(f, start, end, y0, hmax = 0.01)
  
  T = sol[["t"]] 
  Y = sol[["y"]]  
  sol1=cbind(T, Y)
  sol1 = data.frame(sol1)
  return(sol1)
  
}

covid_model <- function(Pi_E = 5e7, mu_E = 0.5, beta1 = 2e-8, mu_1 = 1, kappa1 = 5e-4, N1 = 151, theta_x = 100,
                        mu_c = 1.8, Pi_tc= 1e5, r_tc = 0.1, psi_tc = 10, mu_tc= 0.34, r_x = 10, beta2 = 5.4e-9,
                        mu_2 = 0.5, kappa2 = 2e-3, N2 = 1.2e4,mu_i = 1, Pi_ti = 5e5, r_ti = 0.1, psi_ti = 30, 
                        mu_ti = 0.33, psi_x = 1e5) {
  
  E0 <- 0.7 * Pi_E * mu_E
  
  f <- function(t, y){
    as.matrix(c(Pi_E-beta1*y[1]*y[3]-mu_E*y[1],
                beta1*y[1]*y[3]- mu_1*y[2]-kappa1*y[2]*y[4],
                N1*mu_1*y[2]*(1-y[5]/(theta_x +y[5])-mu_c*y[4]),
                r_tc* y[2]/(psi_tc +y[2]-mu_tc*y[4]),
                r_x*((y[2])/(psi_x + y[2])-y[5])))
  }
  
  ICc = as.matrix(c(E0, 0, 1, 0, 0))
  
  sol <- ode78(f, 0.0, 10.0, ICc, hmax = 0.01)
  
  T = sol[["t"]] 
  Y = sol[["y"]]  
  
  sol1=cbind(T, Y)
  
  sol1 = data.frame(sol1)
  
  return(sol1)            
}

influenza_model <- function(Pi_E = 5e7, mu_E = 0.5, beta1 = 2e-8, mu_1 = 1, kappa1 = 5e-4, N1 = 151, theta_x = 100,
                            mu_c = 1.8, Pi_tc= 1e5, r_tc = 0.1, psi_tc = 10, mu_tc= 0.34, r_x = 10, beta2 = 5.4e-9,
                            mu_2 = 0.5, kappa2 = 2e-3, N2 = 1.2e4,mu_i = 1, Pi_ti = 5e5, r_ti = 0.1, psi_ti = 30, 
                            mu_ti = 0.33, psi_x = 1e5){
  
  
  E0 <- 0.7 * Pi_E * mu_E
  
  ICi = as.matrix(c(E0, 0, 1, 0, 0))

  f <- function(t, y){
    as.matrix(c(Pi_E - beta2*y[1]*y[3] - mu_E*y[1]),
              beta2*y[1]*y[3] - mu_2*y[2] - kappa2*y[2]*y[4],
              N2*mu_2*y[2]*(theta_x/(theta_x + y[5])) - mu_i*y[3],
              Pi_ti + r_ti* y[2]/(psi_ti +y[2]) - mu_ti*y[4],
              r_x*((y[2])/(psi_x + y[2])-y[5]))
  }
  
  sol <- ode78(f, 0.0, 10.0, ICi, hmax = 0.01)
  
  T = sol[["t"]] 
  Y = sol[["y"]]  
  
  sol1=cbind(T, Y)
  
  sol1 = data.frame(sol1)
  
  return(sol1)    
  
}