import streamlit as st

import Custom_Functions as CF
import EDA_Functions as EDA

def OTSU_Threshold_Analysis():
    ### Part 1: OTSU Analysis ### 
    ## OTSU Analysis
    st.header("OTSU Analysis")

    st.subheader("Step 1: Analyze Image using OTSU Threshold")
    st.write("""
        - OTSU Threshold:
            - returns a single intensity threshold that separate pixels into two classes, foreground and background.
            - This threshold is determined by minimizing intra-class intensity variance, or equivalently, by maximizing inter-class variance.
        """)
    ## Upload Scratch Data
    img_file = st.file_uploader("Upload A Single Scratch Data:", type=["png", "jpg", "jpeg"])   
    
 
  # Check if a file was uploaded
    if img_file is not None:
        # To See Image details
        file_details = {"filename":img_file.name, 
                        "filetype":img_file.type,
                        "filesize":img_file.size}
        st.write(file_details)
        
        # To View Uploaded Image
        st.image(CF.load_image(img_file),width=650)
        
        ###  Step 2: OTSU Threshold Analysis ### 
        st.subheader('Step 2: Finding Ideal OTSU Threshold Parameter:')
        # st.caption("Identify the Best Disk Parameter:")
        Min_disk_starting_number = st.number_input('Insert Min Disk Parameter:', value=1, min_value=1, max_value=50)
        Max_disk_starting_number = st.number_input('Insert Max Disk Parameter:', value=1, min_value=1, max_value=50)
        StepNum_disk = st.number_input('Insert Number of Steps Parameter:', value=1, min_value=1, max_value=50)
        
        if st.button('Process OTSU Threshold'):
                EDA.Show_Image_Entropy(img_file, 
                                       Min_disk_starting_number, 
                                       Max_disk_starting_number, 
                                       StepNum_disk)
 
    else:
        st.warning('Please Upload Scratch Image Data First')


def Multi_Image_OTSU_Regression():
    ###  Step 3: Multi_Image_OTSU_Regression ### 
    st.subheader('Step 3: Multi Image OTSU Regression')
    
    ## Upload Multiple Scratch Data
    multi_img_files = st.file_uploader("Upload Multiple Scratch Data(Order Matters !):", 
                                       accept_multiple_files=True,
                                       type=["png", "jpg", "jpeg"],
                                       key="multi_img_files")
    

    if st.button('Process Multi Image OTSU Regression'):
        # Check if More Than 3 files was uploaded
        if (len(multi_img_files)>3):
            with st.spinner('Processing Multiple Image OTSU Regression...'):
    
                EDA.Multi_Image_Entropy_Disk_Analysis(Ideal_Entropy_Disk_Size=10,
                                                    Images_List=multi_img_files)

        
        elif (len(multi_img_files)<=3):
            st.error('Please Upload More Than 3 Scratch Images Data')  
        else:
            st.warning('Please Upload Scratch Images Data First')  
    
    


### OTSU Analysis Main###
def OTSU_Analysis_Main():
    OTSU_Threshold_Analysis() # Part 1 & 2: OTSU Analysis
    Multi_Image_OTSU_Regression() # Part 3: Multi Image OTSU Regression