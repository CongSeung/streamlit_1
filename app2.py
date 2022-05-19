from pandas import value_counts
import streamlit as st

def main():
    st.title('웹 대시보드')                ## 큰 글씨
    st.text('웹 대시보드 개발하기')
   
    name = '홍길동'

    # 제 이름은 홍길동입니다.
    print('제 이름은 {} 입니다.'.format(name))
    # 프린트문은 터미널에 찍힌다.
    st.text('제 이름은 {} 입니다.'.format(name))

    st.header('이 영역은 헤더 영역')
    st.subheader('이 영역은 서브헤더')
    st.success('작업이 성공했을 때 사용하자.')
    st.warning('경고 문구를 보여줘야 할 때 사용하자.')
    st.info('정보를 보여주고 싶을 때')
    st.error('오류가 났을 때')

    # 파이썬의 함수 사용법을 보여주고 싶을 때 
    st.help(sum)
    st.help(len)
    st.help(value_counts)


if __name__ == '__main__':
    main()