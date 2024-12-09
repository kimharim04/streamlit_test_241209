import streamlit as st

#과제
st.title("21대 대통령선거")

st.header('**투표 용지**')
with st.form('my form'):
        kr_president = st.selectbox('21대 대통령 후보', ['이재명', '한동훈', '조국', '이준석', '허경영', '홍길동', '강감찬'])
        submitted = st.form_submit_button('제출')

if submitted:
        st.markdown(f'''
                    - 투표한 대통령 후보 : '{kr_president}'
                    ''')
        
else:
        st.write("투표하세요")
