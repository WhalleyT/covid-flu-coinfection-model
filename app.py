import src.default_params
import src.sliders
import src.models

from scipy.integrate import solve_ivp

from bokeh.models import Slider, RangeSlider, ColumnDataSource
from bokeh.io import curdoc, output_file
from bokeh.layouts import column, row
from bokeh.plotting import figure,save
from bokeh.models.widgets import Paragraph
from bokeh.client import push_session


def readme():
    return Paragraph(text="""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor 
                                incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud 
                                exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute 
                                irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
                                Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt 
                                mollit anim id est laborum""", 
                                width=250, height=100)

def main():

    #retrieve our starting parameters and store them in a dictionary
    params = src.default_params.params
    covid_params = src.default_params.covid_params
    flu_params = src.default_params.influenza_params

    #retrieve our initial conditions, tau parameter and time intervals for coinfection model
    coinfection_inital_conditions, tau, time_interval_1, time_interval_2 = src.default_params.init_params_comb(params)


    #run our coinfection model first, so we have something to
    coinfection_sol = src.models.run_covid_coinfection_model(src.models.model_covid_influenza,
                                                            time_interval_1, time_interval_2, 
                                                            coinfection_inital_conditions, params)


    #put it into a dataframe
    coinfection_src = ColumnDataSource(data=dict(t = coinfection_sol.t, y1 = coinfection_sol.y[0,], y2 = coinfection_sol.y[1,], 
                                        y3 = coinfection_sol.y[2,], y4 = coinfection_sol.y[3,], y5 = coinfection_sol.y[4,], 
                                        y6 = coinfection_sol.y[5,], y7 = coinfection_sol.y[6,], y8 = coinfection_sol.y[7,]))

    
    #now do the same for the flu model
    flu_initial_conditions, tint_flu, flu_params_tuple = src.default_params.init_params_flu(params)

    flu_sol = solve_ivp(src.models.model_flu, tint_flu, flu_initial_conditions,
                                atol = [1e-20] * 5, args=flu_params_tuple)

    flu_src = ColumnDataSource(data=dict(t = flu_sol.t, y1 = flu_sol.y[0,], 
                               y2 = flu_sol.y[1,], y3 = flu_sol.y[2,], 
                               y4 = flu_sol.y[3,], y5 = flu_sol.y[4,]))

    
    
    
    
    #create our plots
    e_cell_per_ml_vs_time = figure(height=800, width=800, title="E (cells/mL) vs Time (Days)",
                                tools="crosshair,pan,reset,save,wheel_zoom")
    ec_cell_per_ml_vs_time = figure(height=800, width=800, title="E_c (cells/mL) vs Time (Days)",
                                tools="crosshair,pan,reset,save,wheel_zoom")

    #set up plots
    e_cell_per_ml_vs_time.line('t', 'y1', source=coinfection_src, line_width=3, line_alpha=0.6)
    ec_cell_per_ml_vs_time.line('t', 'y2', source=coinfection_src, line_width=3, line_alpha=0.6)

    #function to update over time
    def update_data(attrname, old, new):
        for parameter in params:
            if parameter in src.sliders.covid_sliders:
                params[parameter] = src.sliders.covid_sliders[parameter].value
            elif parameter in src.sliders.covid_sliders:
                params[parameter] = src.sliders.flu_sliders[parameter].value

        coinfection_sol = src.models.run_covid_coinfection_model(src.models.model_covid_influenza,
                                                        time_interval_1, time_interval_2, coinfection_inital_conditions, params)

        coinfection_src.data = dict(t = coinfection_sol.t, y1 = coinfection_sol.y[0,], y2 = coinfection_sol.y[1,], 
                        y3 = coinfection_sol.y[2,], y4 = coinfection_sol.y[3,], y5 = coinfection_sol.y[4,], 
                        y6 = coinfection_sol.y[5,], y7 = coinfection_sol.y[6,], y8 = coinfection_sol.y[7,])
        
        #now reinit flu model with parameters as they take a different tuple
        flu_initial_conditions, tint_flu, flu_params_tuple = src.default_params.init_flu_params(params)
        
        flu_sol = solve_ivp(src.models.model_flu, tint_flu, flu_initial_conditions,
                            atol = [1e-20] * 5, args=flu_params_tuple)
                                
        flu_src.data = ColumnDataSource(data=dict(t = flu_sol.t, y1 = flu_sol.y[0,], 
                                        y2 = flu_sol.y[1,], y3 = flu_sol.y[2,], 
                                        y4 = flu_sol.y[3,], y5 = flu_sol.y[4,]))

    for w in list(src.sliders.covid_sliders.values()) + list(src.sliders.flu_sliders.values()):
        w.on_change('value', update_data)


    inputs = column(list(src.sliders.covid_sliders.values()))

    plot_column_left = column(e_cell_per_ml_vs_time, ec_cell_per_ml_vs_time)



    #make the document
    curdoc().add_root(row(inputs, plot_column_left))
    curdoc().title = "Coinfection Model of COVID-19 and Influenza"
    output_file('plot.html')

main()