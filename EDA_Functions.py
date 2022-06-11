from re import I
import streamlit as st
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

# Image Processing Libraries
from skimage import io
from skimage.filters.rank import entropy
from skimage.morphology import disk
from skimage.filters import threshold_otsu

# Linear Regression
from scipy.stats import linregress

# My Custom Function 
import Custom_Functions as CF

def Show_Image_Entropy(Img_File, 
                       Min_Entropy_Disk_Size: int, 
                       Max_Entropy_Disk_Size: int, 
                       Steps_Entropy_Disk: int):
    """_summary_ : "Show Image Entropy"

    Args:
        Img_File (_type_): _description_: Image File
        Min_Entropy_Disk_Size (int): _description_ : Minimum Entropy Disk Size
        Max_Entropy_Disk_Size (int): _description_: Maximum Entropy Disk Size
        Steps_Entropy_Disk (int): _description_: Steps Entropy Disk
    """
    
    # Load Image
    # img_file = CF.load_image(Img_File)
    # st.image(img_file, width=650)
    CF.save_uploadedfile(uploadedfile=Img_File, Save_Path='User Uploaded Images\OTSU Threshold Image Analysis')

    Single_Image_Entropy_Disk_Analysis(Min_Entropy_Disk_Size,
                                       Max_Entropy_Disk_Size,
                                       Steps_Entropy_Disk,
                                       Image_Path=r"User Uploaded Images\OTSU Threshold Image Analysis\user_scratch_data.jpg",)
   

###! Improve the code to make it more efficient !###
def Get_MatplotFigure_Rows_Columns(Min_Entropy_Disk_Size,
                                   Max_Entropy_Disk_Size,
                                   Steps_Entropy_Disk,):
    
    """_summary_ : "Get Matplot Figure Rows by looping through the Entropy Disk Size"

    Returns:
        _type_: _description_: Number of Rows Subplots
    """
    Total_Loop = 0
    for x in range(Min_Entropy_Disk_Size, Max_Entropy_Disk_Size+1, Steps_Entropy_Disk):
        Total_Loop += 1
    
    Total_Rows = Total_Loop 
    return Total_Rows

def Entropy_Image_Processing(Entropy_Disk_Size, Image_Path):
    """_summary_ : "Entropy Image Processing"

    Args:
        Entropy_Disk_Size (_type_): _description_: Entropy Disk Size
        Image_Path (_type_): _description_: Image Path

    Returns:
        _type_: _description_: Entropy Image
    """
    # Load image
    img = io.imread(Image_Path)

    # Entropy of image
    # Disk size is the radius of the disk used to calculate the entropy
    # Large disk size means more detail in the image, but less detail in the entropy
    entropy_img = entropy(img, disk(Entropy_Disk_Size))
    return entropy_img


def Binary_OTSU_Threshold_Image_Processing(Entropy_Image):
    """_summary_ : "Binary OTSU Threshold Image Processing"

    Args:
        Entropy_Image (_type_): _description_: Entropy Image

    Returns:
        _type_: _description_: Binary OTSU Threshold Image
    """
    # Create a mask of the image using the otsu's thresholding
    # Thresholding is the process of converting an image to a binary image
    OTSU_Threshold = threshold_otsu(Entropy_Image)
    # print(f"Threshold: {OTSU_Threshold}") # Error Check

    # Create a binary image using the threshold
    Binary_OTSU_Image = Entropy_Image <= OTSU_Threshold

    # Show Total Sum of the Scratch Assay(The sum of the Yellow pixels in the image)
    Scratch_Area = np.sum(Binary_OTSU_Image  == True)
    # print(f"Scratch area: {Scratch_Area}") # Error Check
    
    return Binary_OTSU_Image, Scratch_Area, OTSU_Threshold


def Single_Image_Entropy_Disk_Analysis(Min_Entropy_Disk_Size,
                                       Max_Entropy_Disk_Size,
                                       Steps_Entropy_Disk,
                                       Image_Path):
 

    # Define Number of Rows and Columns of Subplots
    fig_NumRows = Get_MatplotFigure_Rows_Columns(Min_Entropy_Disk_Size,
                                                 Max_Entropy_Disk_Size,
                                                Steps_Entropy_Disk,) # Number of ROWS Image to be displayed
    fig_NumColums = 2 # Number of COLUMNS Image to be displayed
    
    
    # Define subplots
    fig, ax = plt.subplots(fig_NumRows, fig_NumColums, figsize=(10,60))

 
    with st.spinner('Wait for it...'):
        Entropy_Disk_Parameters = []
        for Entropy_Disk_Size in range(Min_Entropy_Disk_Size, Max_Entropy_Disk_Size+1, Steps_Entropy_Disk):
            Entropy_Disk_Parameters.append(Entropy_Disk_Size)
            

        # Ploting the Entropy of the images Subplot 
        for Row in range(fig_NumRows):
            for Column in range(fig_NumColums):
                Entropy_Img = Entropy_Image_Processing(Entropy_Disk_Parameters[Row], Image_Path)
                Binary_OTSU_Image, Scratch_Area, OTSU_Threshold = Binary_OTSU_Threshold_Image_Processing(Entropy_Img)
                
                if Column == 0:
                    ax[Row, Column].imshow(Entropy_Img)
                    ax[Row, Column].set_title(f'Entropy Image \n Entropy Disk Size: {Entropy_Disk_Parameters[Row]}', fontweight="bold")
                elif Column == 1:
                    ax[Row, Column].imshow(Binary_OTSU_Image)
                    ax[Row, Column].set_title(f"Binary Image\nEntropy Disk Size: {Entropy_Disk_Parameters[Row]}\nOTSU Threshold Size: {OTSU_Threshold:.2f}\nScratch Area: {Scratch_Area} ", fontweight="bold")
        
    
        
        # plt.suptitle('Finding Best OTSU Threshold Parameter', fontweight="bold") # Overall Title of the Figure  
        fig.tight_layout()# Auto adjust the subplot layout   
        st.pyplot(fig)

    
def Plotly_Scatter_Plot(DataFrame,
                        x_axis, 
                        y_axis, 
                        title, 
                        x_axis_title, 
                        y_axis_title, 
                        Hover_Template):
    df = DataFrame
    
    fig = go.Figure()
    
    # Add traces
    fig.add_trace(go.Scatter(x=df[x_axis], y=df[y_axis],
                        mode='markers',
                        name='markers',
                        hovertemplate=Hover_Template))
    
    # Add Plot Title
    fig.update_layout(title_text=title, title_x=0.5)
    
    # Add Axis Title
    fig.update_layout(xaxis_title= x_axis_title,
                      yaxis_title=y_axis_title)
    
    return fig


def Scipy_Get_LinearRegression_Parameters(DataFrame, x_axis, y_axis):
    """_summary_ : "Scipy Get Linear Regression Parameters"

    Args:
        DataFrame (_type_): _description_: DataFrame
        x_axis (_type_): _description_: x_axis
        y_axis (_type_): _description_: y_axis

    Returns:
        _type_: _description_: Linear Regression Parameters
    """
    # Create a linear regression object
    slope, intercept, r_value, p_value, std_err = linregress(DataFrame[x_axis], DataFrame[y_axis])
    
    return slope, intercept, r_value, p_value, std_err
    
def Multi_Image_Entropy_Disk_Analysis(Ideal_Entropy_Disk_Size,Images_List):
    
    Scratch_Area_List = []
    Time_List = []
    time = 1
    for Image in Images_List:

        Entropy_Img=Entropy_Image_Processing(Ideal_Entropy_Disk_Size, Image)
        Binary_OTSU_Image, Scratch_Area, OTSU_Threshold = Binary_OTSU_Threshold_Image_Processing(Entropy_Img)
        Scratch_Area_List.append(Scratch_Area)

        Time_List.append(time)
        time+=1
        
    # st.write(f"Scratch Area List: {Scratch_Area_List}") # Error Check
    
    
    # Create a DataFrame
    df = pd.DataFrame(list(zip(Time_List, Scratch_Area_List)),
                     columns =['Day', 'Scratch Area'])
    # st.dataframe(df) # Error Check
    
    ## Create Linear Regression Equation
    slope, intercept, r_value, p_value, std_err = Scipy_Get_LinearRegression_Parameters(df,  
                                                                                        x_axis='Day', 
                                                                                        y_axis='Scratch Area')
    
    st.latex(rf'''

    Linear Regression Equation: \newline
    Y = {slope:.2f}X + {intercept:.2f}\newline
    R^2 = {r_value**2:.2f}
    
    ''')
    
    ## Scatter Plot
    fig = Plotly_Scatter_Plot(DataFrame=df,
                                     x_axis='Day', 
                                     y_axis='Scratch Area', 
                                     title="Scratch Area vs Time Plot",
                                     x_axis_title="<b>Day</b>",
                                     y_axis_title="<b>Scratch Total Area</b>",
                                     Hover_Template='<b>Day: %{x}</b><br><b>Scratch Area: %{y}</b>')

    st.plotly_chart(fig, use_container_width=True)
    

    
    
    
    