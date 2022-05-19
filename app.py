# 스트림릿 라이브러리를 사용하기 위해 import 하기
import streamlit as st

# 웹 대시보드 개발 라이브러리인, 스트림릿은
# main 함수가 있어야 한다.

def main() :
    st.title('안녕하세요. 웹 대시보드 프로젝트.')
    st.title('Hello. 안녕.')

if __name__ == '__main__' :
    main() 
## 위가 기본 틀

## 터미널에서 실행하기 전에 꼭 저장할 것. HTML에서 매번 저장해서 확인하듯이 

## 웹서버가 도는 동안 터미널엔 입력이 되지 않는다. 그 때 Ctrl + C 누르면 멈추고 명령 입력 가능해진다.