import streamlit as st
from pathlib import Path
import pandas as pd
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

st.title("GC Viewer")
st.markdown("""
GC Viewer is a simple application to explore GC fractions of all sequences in a FASTA file.

Select a FASTA file to get started.
""")

def show_gc(records):
    ID = []
    GC = []
    for rec in records:
        ID.append(rec.id)
        GC.append(gc_fraction(rec.seq))
    data = { "Seq ID" : ID , "GC Fraction" : GC}
    df = pd.DataFrame(data)
    df.set_index("Seq ID", inplace=True)
    return (df)
    
def barchart(df):
    st.bar_chart(data=df, x =None , y = "GC Fraction")
    
def upload_dataset():
    st.header("Select a FASTA file")

    uploaded_file = st.file_uploader(
        "Choose a FASTA file to upload",
        type="fasta")
    if uploaded_file is not None:
    	data = uploaded_file.getvalue()
    	path = root.joinpath(uploaded_file.name)
    	path.write_bytes(data)
    	st.write("saved the file to", path)
    	st.header("GC Fraction as a Table")
    	records = SeqIO.parse(path, "fasta")
    	df = show_gc(records)
    	st.write(df)

    	st.header("GC Fraction as Chart")
    	barchart(df)

   
root = Path("datasets")

upload_dataset()





