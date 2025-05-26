import streamlit as st

st.title("📘 제성준")

col1,col2 = st.columns([2,3])
# 공간을 2:3 으로 분할하여 col1과 col2라는 이름을 가진 컬럼을 생성합니다.  

with col1 :
  # column 1 에 담을 내용
  st.title('여기는 1 열 ')
with col2 :
  # column 2 에 담을 내용
  st.title('여기는 2열')
  st.checkbox('2열 체크박스 1 ')


# with 구문 말고 다르게 사용 가능 
col1.subheader(' 1열 서브헤더 !! ')

col2.checkbox('2열 체크박스 2 ') 

#=>위에 with col2: 안의 내용과 같은 기능을합니다

