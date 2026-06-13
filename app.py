from matplotlib import font_manager

fonts = [f.fname for f in font_manager.fontManager.ttflist]

korean_font = None

for f in fonts:
    if (
        "Nanum" in f
        or "Malgun" in f
        or "NotoSansCJK" in f
        or "Noto Sans CJK" in f
    ):
        korean_font = f
        break

st.write("찾은 폰트:", korean_font)
