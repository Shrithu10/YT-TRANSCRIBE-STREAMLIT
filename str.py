# import module
import streamlit as st
from string import punctuation
from heapq import nlargest
from youtube_transcript_api import YouTubeTranscriptApi as yta
import re
# Title
st.title("YOUTUBE TO TRANSCRIPT")
# Text Input

# save the input text in the variable 'name'
# first argument shows the title of the text input box
# second argument displays a default text inside the text input area
link= st.text_input("Drop the link", "Type Here ...")

# display the name when the submit button is clicked
# .title() is used to get the input text string

def transcribe(l):#Here pass the link only , copy it from the url
    ids=l.split("=")
    vid_id=ids[1]
    data=yta.get_transcript(vid_id)
    transcript=''
    for value in data:
        for key,val in value.items():
            if key=="text":
                transcript+=val
    l=transcript.splitlines()
    finaldata=" ".join(l)
    return finaldata

if(st.button('Transcribe')):
    st.components.v1.iframe(link, width=None, height=None, scrolling=False)
    st.text_area(label="Output Data:", value=transcribe(link), height=350)