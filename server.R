library(ggplot2)
library(dplyr)

source("R/models.R")

function(input, output, session) {
  solution <- reactive({
    
    covid_solution <- covid_model(Pi_E = input$Pi_E, mu_E = input$Mu_E, beta1 = input$Beta_1, mu_1 = input$mu_Ec,
                                  kappa1 = input$Kappa_1,N1 = input$N1, theta_x = input$Theta_x, mu_c = input$Mu_c, 
                                  Pi_tc = input$Pi_Tc, mu_tc = input$Mu_Tc, psi_tc = input$Psi_Tc, r_x=input$Rx, 
                                  psi_x = input$Psi_X, beta2 =input$Beta_2,  mu_2 = input$Mu_Ei, kappa2 =input$Kappa2,
                                  N2 = input$N2, mu_i = input$Mu_i, Pi_ti = input$Pi_Ti, psi_ti = input$Psi_Ti, 
                                  mu_ti =  input$Mu_Ti)
    
    influenza_solution <- influenza_model(Pi_E = input$Pi_E, mu_E = input$Mu_E, beta1 = input$Beta_1, mu_1 = input$mu_Ec,
                                          kappa1 = input$Kappa_1,N1 = input$N1, theta_x = input$Theta_x, mu_c = input$Mu_c, 
                                          Pi_tc = input$Pi_Tc, mu_tc = input$Mu_Tc, psi_tc = input$Psi_Tc, r_x=input$Rx, 
                                          psi_x = input$Psi_X, beta2 =input$Beta_2,  mu_2 = input$Mu_Ei, kappa2 =input$Kappa2,
                                          N2 = input$N2, mu_i = input$Mu_i, Pi_ti = input$Pi_Ti, psi_ti = input$Psi_Ti, 
                                          mu_ti =  input$Mu_Ti)
    
    
    
    if(input$coinfection_delay == "covid"){
      eps <- 0.7
      
      E0=eps*input$Pi_E/input$Mu_E
      
      Ec0=0
      C0=0
      Tc0=0
      H0=0
      Ei0=0
      I0=1
      Ti0=0
      y0 <- as.matrix(c(E0, Ec0, C0, Tc0, H0, Ei0, I0, Ti0))
      
      monoinfection_solution <-     coinfection_model(Pi_E = input$Pi_E, mu_E = input$Mu_E, beta1 = input$Beta_1, mu_1 = input$mu_Ec,
                                                      kappa1 = input$Kappa_1,N1 = input$N1, theta_x = input$Theta_x, mu_c = input$Mu_c, 
                                                      Pi_tc = input$Pi_Tc, mu_tc = input$Mu_Tc, psi_tc = input$Psi_Tc, r_x=input$Rx, 
                                                      psi_x = input$Psi_X, beta2 =input$Beta_2,  mu_2 = input$Mu_Ei, kappa2 =input$Kappa2,
                                                      N2 = input$N2, mu_i = input$Mu_i, Pi_ti = input$Pi_Ti, psi_ti = input$Psi_Ti, 
                                                      mu_ti =  input$Mu_Ti, y0 = y0, start = 0, end = 3)
      
      y0[3,] <- 1
      
      coinfection_solution  <-     coinfection_model(Pi_E = input$Pi_E, mu_E = input$Mu_E, beta1 = input$Beta_1, mu_1 = input$mu_Ec,
                                                     kappa1 = input$Kappa_1,N1 = input$N1, theta_x = input$Theta_x, mu_c = input$Mu_c, 
                                                     Pi_tc = input$Pi_Tc, mu_tc = input$Mu_Tc, psi_tc = input$Psi_Tc, r_x=input$Rx, 
                                                     psi_x = input$Psi_X, beta2 =input$Beta_2,  mu_2 = input$Mu_Ei, kappa2 =input$Kappa2,
                                                     N2 = input$N2, mu_i = input$Mu_i, Pi_ti = input$Pi_Ti, psi_ti = input$Psi_Ti, 
                                                     mu_ti =  input$Mu_Ti, y0 = y0, start = 3, end = 10)
      
      solution <- rbind(monoinfection_solution, coinfection_solution)
      
    }
    if(input$coinfection_delay == "flu"){
      eps <- 0.7
      
      E0=eps*input$Pi_E/input$Mu_E
      
      Ec0=0
      C0=1
      Tc0=0
      H0=0
      Ei0=0
      I0=0
      Ti0=0
      
      y0 <- as.matrix(c(E0, Ec0, C0, Tc0, H0, Ei0, I0, Ti0))
      
      
      
      monoinfection_solution <-     coinfection_model(Pi_E = input$Pi_E, mu_E = input$Mu_E, beta1 = input$Beta_1, mu_1 = input$mu_Ec,
                                                      kappa1 = input$Kappa_1,N1 = input$N1, theta_x = input$Theta_x, mu_c = input$Mu_c, 
                                                      Pi_tc = input$Pi_Tc, mu_tc = input$Mu_Tc, psi_tc = input$Psi_Tc, r_x=input$Rx, 
                                                      psi_x = input$Psi_X, beta2 =input$Beta_2,  mu_2 = input$Mu_Ei, kappa2 =input$Kappa2,
                                                      N2 = input$N2, mu_i = input$Mu_i, Pi_ti = input$Pi_Ti, psi_ti = input$Psi_Ti, 
                                                      mu_ti =  input$Mu_Ti, y0 = y0, start = 0, end = 3)
      
      y0[5,] <- 1
      
      coinfection_solution  <-     coinfection_model(Pi_E = input$Pi_E, mu_E = input$Mu_E, beta1 = input$Beta_1, mu_1 = input$mu_Ec,
                                                     kappa1 = input$Kappa_1,N1 = input$N1, theta_x = input$Theta_x, mu_c = input$Mu_c, 
                                                     Pi_tc = input$Pi_Tc, mu_tc = input$Mu_Tc, psi_tc = input$Psi_Tc, r_x=input$Rx, 
                                                     psi_x = input$Psi_X, beta2 =input$Beta_2,  mu_2 = input$Mu_Ei, kappa2 =input$Kappa2,
                                                     N2 = input$N2, mu_i = input$Mu_i, Pi_ti = input$Pi_Ti, psi_ti = input$Psi_Ti, 
                                                     mu_ti =  input$Mu_Ti, y0 = y0, start = 3, end = 10)
      
      solution <- rbind(monoinfection_solution, coinfection_solution)
      
    }
    if(input$coinfection_delay == "simul"){
      E0 <- 0.7*input$Pi_E/input$Mu_E
      y0 <- as.matrix(c(E0, 1, 10, 1, 1, 1, 1, 1))
      
      solution <- coinfection_model(Pi_E = input$Pi_E, mu_E = input$Mu_E, beta1 = input$Beta_1, mu_1 = input$mu_Ec,
                                    kappa1 = input$Kappa_1,N1 = input$N1, theta_x = input$Theta_x, mu_c = input$Mu_c, 
                                    Pi_tc = input$Pi_Tc, mu_tc = input$Mu_Tc, psi_tc = input$Psi_Tc, r_x=input$Rx, 
                                    psi_x = input$Psi_X, beta2 =input$Beta_2,  mu_2 = input$Mu_Ei, kappa2 =input$Kappa2,
                                    N2 = input$N2, mu_i = input$Mu_i, Pi_ti = input$Pi_Ti, psi_ti = input$Psi_Ti, 
                                    mu_ti =  input$Mu_Ti, y0 = y0)
      
      
    }
    
    
    output <- left_join(solution, covid_solution, by = "T")
    output <- left_join(output, influenza_solution, by = "T")
    solution <- list("coinfection" = solution, "influenza" = influenza_solution, "covid" = covid_solution)
    return(solution)
  })
  
  output$plot_1_1 <- renderPlot({
    ggplot(solution()$coinfection, aes(x=T,y=V2))+geom_path()+
      scale_y_log10()+theme_bw()+
      xlab("days") + ylab("E")
  })
  
  output$plot_1_2 <- renderPlot({
    ggplot(solution()$coinfection, aes(x=T,y=V3))+geom_path()+
      scale_y_log10()+theme_bw()+
      xlab("days") + ylab("E_c")
  })
  
  output$plot_2_1 <- renderPlot({
    ggplot(solution()$coinfection, aes(x=T,y=V4))+geom_path()+
      scale_y_log10()+theme_bw()+
      geom_path(data = solution()$covid, aes(x=T, y=V4), color = "red")+
      xlab("days") + ylab("C")
  })
  
  output$plot_2_2 <- renderPlot({
    ggplot(solution()$coinfection, aes(x=T,y=V5))+geom_path()+
      scale_y_log10()+theme_bw()+
      xlab("days") + ylab("E_i")
  })
  
  output$plot_3_1 <- renderPlot({
    ggplot(solution()$coinfection, aes(x=T,y=V6))+geom_path()+
      scale_y_log10()+theme_bw()+
      geom_path(data = solution()$influenza, aes(x=T, y=V4), color = "red")+
      xlab("days") + ylab("I")
  })
  
  output$plot_3_2 <- renderPlot({
    ggplot(solution()$coinfection, aes(x=T,y=V7))+geom_path()+
      scale_y_log10()+theme_bw()+
      xlab("days") + ylab("T_c")
  })
  
  output$plot_4_1 <- renderPlot({
    ggplot(solution()$coinfection, aes(x=T,y=V8))+geom_path()+
      scale_y_log10()+theme_bw()+
      xlab("days") + ylab("T_i")
  })
  
  output$plot_4_2 <- renderPlot({
    ggplot(solution()$coinfection, aes(x=T,y=V9))+geom_path()+
      scale_y_log10()+theme_bw()+
      xlab("days") + ylab("X")
  })
}