library(shiny)

# Define UI for application that draws a histogram
ui <- fluidPage(
  
  # Application title
  titlePanel("COVID-Influenza coinfection model"),
  
  # Sidebar with a sliderInput input for number of bins 
  sidebarLayout(
    sidebarPanel(
      radioButtons("coinfection_delay", "Type of co-infection",
                   choices = list("COVID first" = "covid", "Influenza first" = "flu", "Simultaneous (no delay)" = "simul"),
                   selected = "simul"),
      
      h2("COVID parameters"),
      sliderInput("Pi_E", "Pi_E", value=5e7, min=3.9e5, max=1.1e8),
      sliderInput("Mu_E", "Mu_E", value=0.5, min=0.0625, max=1),
      sliderInput("Beta_1", "Beta_1", value=2e-8, min=3e-10, max=2.1e-7),
      sliderInput("mu_Ec", "mu_Ec", value=1, min=0.61, max=4.5),
      sliderInput("Kappa_1", "Kappa_1", value = 5e-4, min= 1e-5,  max= 1e-2),
      sliderInput("N1", "N1", value = 151, min= 151,  max= 6591),
      sliderInput("Theta_x", "Theta_x", value=100, min=0.1, max= 100),
      sliderInput("Mu_c", "Mu_c", value = 1.8, min=1.8, max=15.12),
      sliderInput("Pi_Tc", "Pi_Tc", value=1e5, min=780, max=137000),
      sliderInput("Mu_Tc", "Mu_Tc", value=0.34, min= 0.003, max= 37.3),
      sliderInput("Psi_Tc", "Psi_Tc", value=10, min= 0.003, max= 37.3),
      sliderInput("Rx", "Rx", value=10, min=1, max=10),
      sliderInput("Psi_X", "Psi_X", value=1e5, min=1e4, max=4e5),
      
      h2("Influenza parameters"),
      sliderInput("Beta_2", "Beta_2", value=5.4e-9, min=5.4e-9, max=4.25e-7, step=1e-9),
      sliderInput("Mu_Ei", "Mu_Ei", value=0.5, min=0.5, max=3.9, step=0.1),
      sliderInput("Kappa2", "Kappa2", value=2e-3, min=4e-6, max=5e-3, step=1e-5),
      sliderInput("N2", "N2", value=1.2e4, min=33, max=13400),
      sliderInput("Mu_i", "Mu_i", value=1, min=1, max=6, step=0.5),
      sliderInput("Pi_Ti", "Pi_Ti", value=5e5, min= 2.3e5, max=3.65e6, step =1e6),
      sliderInput("Psi_Ti", "Psi_Ti", value=30, min=0.003, max= 37.3, step = 0.25),
      sliderInput("Mu_Ti", "Mu_Ti", value = 0.33, min= 0.33, max = 0.5, step = 0.01)
    ),
    
    # Show a plot of the generated distribution
    mainPanel(
      fluidRow(splitLayout(cellWidths = c("50%", "50%"), plotOutput("plot_1_1"), plotOutput("plot_1_2"))),
      fluidRow(splitLayout(cellWidths = c("50%", "50%"), plotOutput("plot_2_1"), plotOutput("plot_2_2"))),
      fluidRow(splitLayout(cellWidths = c("50%", "50%"), plotOutput("plot_3_1"), plotOutput("plot_3_2"))),
      fluidRow(splitLayout(cellWidths = c("50%", "50%"), plotOutput("plot_4_1"), plotOutput("plot_4_2")))
    )
  )
)
