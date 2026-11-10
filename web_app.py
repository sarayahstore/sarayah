import streamlit as st
from rembg import remove
from PIL import Image
import io

st.set_page_config(page_title="مُزيل الخلفيات الذكي", layout="centered")
st.title("🖼️ أداة إزالة الخلفية للمنتجات أونلاين")
st.write("ارفع صورة منتجك ليقوم الذكاء الاصطناعي بتفريغها بدقة عالية فوراً.")

uploaded_file = st.file_uploader("اختر صورة المنتج...", type=["jpg", "jpeg", "png", "webp"])

if uploaded_file is not None:
    input_image = Image.open(uploaded_file)
    
    st.image(input_image, caption="الصورة الأصلية", use_column_width=True)
    
    if st.button("احذف الخلفية الآن", type="primary"):
        with st.spinner("جاري تفريغ الحواف بدقة..."):
            # إزالة الخلفية
            result_image = remove(input_image)
            
            # تحويل النتيجة بايتس لتجهيزها للتحميل
            buf = io.BytesIO()
            result_image.save(buf, format="PNG")
            byte_im = buf.getvalue()
            
            st.image(result_image, caption="النتيجة الشفافة (PNG)", use_column_width=True)
            
            st.download_button(
                label="تحميل الصورة الشفافة بجودة عالية",
                data=byte_im,
                file_name="transparent_product.png",
                mime="image/png"
            )
