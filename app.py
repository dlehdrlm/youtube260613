if korean_font is None:
    st.error("한글 폰트를 찾지 못했습니다.")
else:
    wc = WordCloud(
        font_path=korean_font,
        width=1200,
        height=600,
        background_color="white"
    ).generate(" ".join(words))

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.imshow(wc)
    ax.axis("off")

    st.pyplot(fig)
