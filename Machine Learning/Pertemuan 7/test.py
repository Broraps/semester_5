import streamlit as st
import pickle
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

model_path = 'c45_pinjam_mod.pkl'
with open(model_path, 'rb') as model_file :
    loaded_model = pickle.load(model_file)
    