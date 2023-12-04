import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta
from faker import *
import random 
from structs import *

with sidebar:
    structs.get_main_components()


st.title('Seja bem-vindo ao sistema Superchips')
structs.get_image()
    
