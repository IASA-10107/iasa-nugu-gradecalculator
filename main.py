import streamlit as st

st.title("느그평학 계싼기")

__grade = {"C+": 2.3,"B-": 2.7, "B0": 3.0, "B+": 3.3, "A-": 3.7, "A0": 4.0, "A+": 4.3, "A++": 4.7}
__get_grade = __grade.__getitem__

__subject_main = ("기하", "미적분", "물리", "화학", "생명과학", "지구과학")
__subject_sub = ("컴프", "국어", "영어", "한국사", "공학개론")
__subject_subsub = ("음악·미술", "체육")

st.header("주요과목: 3학점")
for s in __subject_main: 
    st.select_slider(s, __grade, key=s)
__mains = {
    s: __get_grade(st.session_state[s]) for s in __subject_main
}
__sum_main = sum(__mains.values())
__len_main = len(__mains)

st.header("안주요과목: 2학점")
for s in __subject_sub: 
    st.select_slider(s, __grade, key=s)
__subs = {
    s: __get_grade(st.session_state[s]) for s in __subject_sub
}
__sum_sub = sum(__subs.values())
__len_sub = len(__subs)

st.header("(비시험과목: 2학점)")
for s in __subject_subsub: 
    st.select_slider(s, __grade, key=s)
__subsubs = {
    s: __get_grade(st.session_state[s]) for s in __subject_subsub
}
__sum_subsub = sum(__subsubs.values())
__len_subsub = len(__subsubs)

__sum_subtot = __sum_subsub + __sum_sub
__len_subtot = __len_subsub + __len_sub

with st.sidebar:
    st.header("느그 학점")
    
    __avg1 = __sum_main/__len_main
    st.subheader(f"주요과목: {__avg1:.3f}")

    __avg2s = (__sum_main*3 + __sum_subtot*2) / (__len_main*3 + __len_subtot*2)
    st.subheader(f"평학(가중치, 비시험 포함): {__avg2s:.3f}")
    
    __avg2 = (__sum_main*3 + __sum_sub*2) / (__len_main*3 + __len_sub*2)
    st.subheader(f"평학(가중치): {__avg2:.3f}")

    __avg3s = (__sum_main + __sum_subtot) / (__len_main + __len_subtot)
    st.subheader(f"평학(동일, 비시험 포함): {__avg3s:.3f}")
    
    __avg3 = (__sum_main + __sum_sub) / (__len_main + __len_sub)
    st.subheader(f"평학(동일): {__avg3:.3f}")

    with st.expander("3학점"):
        for m in __subject_main: st.write(f"**{m}: {st.session_state[m]}**")

    with st.expander("2학점"):
        for m in __subject_sub: st.write(f"**{m}: {st.session_state[m]}**")

    with st.expander("(2학점 비시험)"):
        for m in __subject_subsub: st.write(f"**{m}: {st.session_state[m]}**")
