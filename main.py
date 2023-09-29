import numpy as np
import streamlit as st
import pickle

loaded_model=pickle.load(open('D:/machine learning projects/HEART_BEAT/heart_beat.sav','rb'))

def predictive_system(input_data):
    
    prediction=loaded_model.predict(input_data)
    return prediction[0]

def main():
    st.title('HEART BEAT PREDICTIVE SYSTEM')
    MEAN_RR=st.number_input('Enter the  Mean of RR intervals')
    MEDIAN_RR=st.number_input('Enter the Median of RR intervals')
    SDRR=st.number_input('Enter the Standard deviation of RR intervals')
    RMSSD=st.number_input('Enter the  Root mean square of successive RR interval differences')
    SDSD=st.number_input('Enter the Standard deviation of successive RR interval differences')
    SDRR_RMSSD=st.number_input('Enter the  Ratio of SDRR / RMSSD')
    pNN25=st.number_input('Enter the Percentage of successive RR intervals that differ by more than 25 ms')
    pNN50=st.number_input('Enter the Percentage of successive RR intervals that differ by more than 50 ms')
    KURT=st.number_input('Enter the  Kurtosis of distribution of successive RR intervals')
    SKEW=st.number_input('Enter the Skew of distribution of successive RR intervals')
    MEAN_REL_RR=st.number_input('Enter the Mean of relative RR intervals')
    MEDIAN_REL_RR=st.number_input('Enter the Median of relative RR intervals')
    SDRR_REL_RR =st.number_input('Enter the Standard deviation of relative RR intervals')
    RMSSD_REL_RR=st.number_input('Enter the Root mean square of successive relative RR interval differences')
    SDSD_REL_RR =st.number_input('Enter the Standard deviation of successive relative RR interval differences')
    SDRR_RMSSD_REL_RR  =st.number_input('Enter the  Ratio of SDRR/RMSSD for relative RR interval differences')
    KURT_REL_RR  =st.number_input('Enter the  Kurtosis of distribution of relative RR intervals')
    SKEW_REL_RR  =st.number_input('Enter the  Skewness of distribution of relative RR intervals')
    SD1  =st.number_input('Enter the  Poincaré plot standard deviation perpendicular to the line of identity')
    SD2  =st.number_input('Enter the  Poincaré plot standard deviation along the line of identity')
    Sampen  =st.number_input('Enter the sample entropy which measures the regularity and complexity of a time series')
    higuci  =st.number_input('Enter the datasetId ')
    datasetId   =st.number_input('Enter the datasetId')
    condition   =st.number_input('Enter the  condition of the patient at the time the data was recorded')
    VLF   =st.number_input('Enter the Absolute power of the very low frequency band (0.0033 - 0.04 Hz)')
    VLF_PCT   =st.number_input('Enter the Principal component transform of VLF')
    LF   =st.number_input('Enter the Absolute power of the low frequency band (0.04 - 0.15 Hz)')
    LF_PCT   =st.number_input('Enter the Principal component transform of LF')
    LF_NU   =st.number_input('Enter the Absolute power of the low frequency band in normal units')
    HF   =st.number_input('Enter the Absolute power of the high frequency band (0.15 - 0.4 Hz)')
    HF_PCT  =st.number_input('Enter the  Principal component transform of HF')
    HF_NU   =st.number_input('Enter the Absolute power of the highest frequency band in normal units')
    TP   =st.number_input('Enter the Total power of RR intervals')
    LF_HF   =st.number_input('Enter the  Ratio of LF to HF')
    HF_LF   =st.number_input('Enter the Ratio of HF to LF')
    result=0
    if(st.button('check for heart rate')):
        input_data=(MEAN_RR, MEDIAN_RR, SDRR, RMSSD, SDSD, SDRR_RMSSD,
       pNN25, pNN50, KURT, SKEW, MEAN_REL_RR, MEDIAN_REL_RR,
       SDRR_REL_RR, RMSSD_REL_RR, SDSD_REL_RR, SDRR_RMSSD_REL_RR,
       KURT_REL_RR, SKEW_REL_RR, SD1, SD2, Sampen, higuci,
       datasetId, condition, VLF, VLF_PCT, LF, LF_PCT, LF_NU,
       HF, HF_PCT, HF_NU, TP, LF_HF, HF_LF)
        prediction=predictive_system([input_data])
        result=prediction
    st.success(result)
    
if __name__=='__main__':
    main()
                                     
    