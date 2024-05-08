import tensorflow as tf
import os
import keras
import numpy as np
import easygdf
import mne
import json
import pandas as pd



def event_position():

    filenames = ["A01T.gdf"]#, "A01E.gdf", "A02T.gdf", "A02E.gdf","A03T.gdf","A03E.gdf","A04T.gdf","A04E.gdf","A05T.gdf","A05E.gdf","A06T.gdf","A06E.gdf","A07T.gdf","A07E.gdf","A08T.gdf","A08E.gdf","A09T.gdf","A09E.gdf"
    labels = ["A01T"]#, "A01E", "A02T", "A02E","A03T","A03E","A04T","A04E","A05T","A05E","A06T","A06E","A07T","A07E","A08T","A08E","A09T","A09E"]


    events_with_labels_arrays = {}

    for filename, label in zip(filenames, labels):

        filename='../datasets/BCICIV_2a_gdf/'+filename
        raw = mne.io.read_raw_gdf(filename)

        # Access event information from the raw object
        events, event_id = mne.events_from_annotations(raw)

        #the list have the dictionary that map each events' id  to events' labels
        events_id_labels = list(event_id.keys())

        #create array for gather togther events' type and positions
        temp= np.zeros_like(events)


        for i in range(len(events)):
            temp[i,0]=events[i,0]
            id=events[i,2]
            temp[i,1]=events_id_labels[id-1] # be in dalil ke dar list event ha ma id 10 drim vali araye events_id_labels k az tarigh key dastresi peyda krdim yedone adadash paiin tare

        events_with_labels_arrays[label] = temp

    
    # Get the sample indices of the events
    #event_positions_samples = events[:, 0]

    # Get the corresponding time points from raw
    #event_positions_times = raw.times[event_positions_samples]    

    return events_with_labels_arrays

def save_data_in_array():

    filenames = ["A01T.gdf"]# , "A01E.gdf", "A02T.gdf", "A02E.gdf","A03T.gdf","A03E.gdf","A04T.gdf","A04E.gdf","A05T.gdf","A05E.gdf","A06T.gdf","A06E.gdf","A07T.gdf","A07E.gdf","A08T.gdf","A08E.gdf","A09T.gdf","A09E.gdf"
    labels = ["A01T"]# , "A01E", "A02T", "A02E","A03T","A03E","A04T","A04E","A05T","A05E","A06T","A06E","A07T","A07E","A08T","A08E","A09T","A09E"


    # Create a dictionary to store data arrays
    data_arrays = {}


    # Iterate over the filenames and labels
    for filename, label in zip(filenames, labels):
        # Read the raw data
        filename='../datasets/BCICIV_2a_gdf/'+filename
        raw = mne.io.read_raw_gdf(filename)
        
        # Convert to DataFrame
        df = raw.to_data_frame()
        
        # Store data array in the dictionary
        data_arrays[label] = df.values  # Store the numpy array representation of the DataFrame

    # # Access data array for a specific label
    # example_label = "A01T"
    # example_data_array = data_arrays[example_label]    

    return data_arrays


def create_training_data(data_arrays,events_with_labels_arrays):
    labels = ["A01T"]#, "A02T", "A03T","A04T","A05T","A06T","A07T","A08T","A09T"

    X_train=[]

    for label in labels:

        temp_data=data_arrays[label]
        temp_events=events_with_labels_arrays[label]
        for i in range(len(temp_events)):
        
            if temp_events[i,1]==769 or temp_events[i,1]==770 or temp_events[i,1]==771 or temp_events[i,1]==772 :

                ev=temp_events[i,1]
                position=temp_events[i,0]
                for j in range(position, position+1000):

                    temp=np.append(temp_data[j,1:23],ev)
                    X_train.append(temp)

   
    return X_train                
            


