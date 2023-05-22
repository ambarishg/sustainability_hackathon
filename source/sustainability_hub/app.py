import streamlit as st
import openaing
from streamlit_chat import message
from sentence_transformers import SentenceTransformer
import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from picklefilename import get_ncert_biology_filename, \
get_sustainability_report_filename
from openaing import create_prompt, generate_answer


filename_pickle = ""

from config import analysis_category, ncert_biology_chapters, \
sustainability_reports, ecology_books, activity

result_analysis_category = st.sidebar.radio("Select your Analysis Category",
                 analysis_category)

if result_analysis_category == "NCERT Biology":   
    
    ncert_biology_chapter = st.sidebar.selectbox("Select your Chapter",ncert_biology_chapters)
    filename_pickle =get_ncert_biology_filename(ncert_biology_chapter)
    

if result_analysis_category == "Sustainability Reports":
    sustainability_report = st.sidebar.selectbox("Select your Sustainability Report",sustainability_reports)
    filename_pickle =get_sustainability_report_filename(sustainability_report)
         
if result_analysis_category == "Ecology Books":
     filename_pickle ="Ecology-From-Individuals-to-Ecosystems-by-Michael-Begon--2006.pkl"
    

activity_type = st.sidebar.selectbox("Select your Activity",activity)
conversation=[{"role": "system", "content": "You are a helpful assistant."}]



@st.cache_resource
def get_model():
    model = SentenceTransformer('all-MiniLM-L6-v2')
    return model

def get_encodings():
        if (filename_pickle != ""):
             with open(filename_pickle, 'rb') as f:
                  df_embeddings = pickle.load(f)
                  Lines = df_embeddings["text"].tolist()
                  embeddings = df_embeddings["embeddings"].tolist()
        else:
                Lines = []
                embeddings = []
        return Lines,embeddings

def get_top_N_from_embeddings(q_new):
    Lines,embeddings = get_encodings()
    result = cosine_similarity(q_new,embeddings)
    result_df = pd.DataFrame(result[0], columns = ['sim'])
    df = pd.DataFrame(Lines,columns = ["text"])
    q = pd.concat([df,result_df],axis = 1)
    q = q.sort_values(by="sim",ascending = False)

    q_n = q[:5]
    q_n = q_n[["text"]]
    return q_n

def get_top_N(user_input):
    model = get_model()
    q_new = user_input
    q_new = [model.encode(q_new)]
    q_n = get_top_N_from_embeddings(q_new)
    return q_n

if activity_type == "Question":

    st.title("Sustainability Question and Answering System")

    user_input = st.text_area("Your Question",
    "How do we prevent disturbance to nested birds?")
    result = st.button("Make recommendations")

    if result:   
        if result_analysis_category == "General":
            conversation=[{"role": "system", "content": "Assistant is a large language model trained by OpenAI."}]
            conversation.append({"role": "user", "content": user_input})
            reply = generate_answer(conversation)
            st.write(reply)
        else:
             q_n = get_top_N(user_input)
             conversation=[{"role": "system", "content": "Assistant is a large language model trained by OpenAI."}]
             context= "\n\n".join(q_n["text"])
             prompt = create_prompt(context,user_input)            
             conversation.append({"role": "assistant", "content": prompt})
             conversation.append({"role": "user", "content": user_input})
             reply = generate_answer(conversation)
             st.write(reply)

if activity_type == "Chat":
    st.title("Sustainability Chatbot")
    if 'generated' not in st.session_state:
            st.session_state['generated'] = []

    if 'past' not in st.session_state:
        st.session_state['past'] = []
        
    user_input = st.text_input("Your Question","How do we protect nested birds?")
    conversation.append({"role": "user", "content": user_input})

    if result_analysis_category == "General":
         reply = generate_answer(conversation)
    else:
         q_n = get_top_N(user_input)
         context= "\n\n".join(q_n["text"])
         prompt = create_prompt(context,user_input)
         conversation.append({"role": "assistant", "content": prompt})
         conversation.append({"role": "user", "content": user_input})
    
         reply = generate_answer(conversation)
    

    st.session_state.past.append(user_input)
    st.session_state.generated.append(reply)

    if st.session_state['generated']:    
        for i in range(len(st.session_state['generated'])-1, -1, -1):
            message(st.session_state["generated"][i], key="SUSTAINABILITY" + str(i))
            message(st.session_state['past'][i], is_user=True, key="SUSTAINABILITY" + str(i) + "_user")



