import streamlit as st
from PIL import Image
from gtts import gTTS
import os

# Complete Disease & Medicine Directory
BIMARI_DETAILS = {
    "Tomato - Bacterial Wilt (Tamatar ka Murjhana / বেক্টেৰিয়েল উইল্ট)": 
        "Tamatar mein bacterial wilt hua hai. Iska upchar hai: Copper Oxychloride teen gram prati litre aur Streptocycline ek gram das litre paani mein milakar jadd mein dalein.",
        
    "Tomato - Early Blight (Tamatar ka Jhulsa Rog / আগতীয়া ব্লাইট)": 
        "Tamatar mein early blight yaani jhulsa rog hua hai. Iska upchar hai: Mancozeb ya Safe-M do gram prati litre ya Amistar ek ml prati litre ka chidkaw karein.",
        
    "Potato - Late Blight (Aloo ka Pachheti Jhulsa / পোনপতীয়া ব্লাইট)": 
        "Aloo mein pachheti jhulsa rog hua hai. Iska upchar hai: Ridomil Gold ya Metalaxyl plus Mancozeb do gram prati litre ka turant chidkaw karein.",
        
    "Brinjal - Little Leaf (Baingan ka Chota Patta Rog / সৰু পাতৰ ৰোগ)": 
        "Baingan mein chota patta rog hua hai. Yeh rog jassids se failta hai. Dimethoate do ml prati litre ka chidkaw karein aur bimar paude ko ukhad edin.",
        
    "Chilli - Leaf Curl Virus (Mirch ka Patta Marodi Rog / পাত কোঁচ খাই যোৱা ৰোগ)": 
        "Mirch mein patta marodi rog hua hai. Neem oil paanch ml prati litre ya Rogor do ml prati litre thrips aur whitefly ko rokne ke liye dalein.",
        
    "Okra (Bhindi) - Yellow Vein Mosaic (Bhindi ki Peeli Nas Rog / হালধীয়া সিৰা ম’জাইক)": 
        "Bhindi mein peeli nas ka rog hua hai. Whitefly ko rokne ke liye Acetamiprid ya Imidacloprid aadha ml prati litre ka chidkaw karein.",
        
    "Rice/Paddy - Blast Disease (Dhan ka Jhonka Rog / ধানৰ ব্লাষ্ট ৰোগ)": 
        "Dhan mein jhonka rog hua hai. Iska upchar hai: Tricyclazole zero point six gram prati litre ka chidkaw karein.",
        
    "Healthy Leaf/Crop (Aapka Patta Bilkul Thik Hai! / আপোনাৰ পাতখিলা সম্পূৰ্ণ সুস্থ!)": 
        "Aapka pauda bilkul swasth hai. Kisi dawa ki zaroorat nahi hai. Paude ko samay par paani aur gobar khaad dete rahein."
}

BIMARI_EXAMPLES = list(BIMARI_DETAILS.keys())

# --- APP INTERFACE WITH TEACHER CREDIT ---
st.title("🌱 Smart AI Agri-Scanner")

col1, col2 = st.columns([1, 3])

with col1:
    if os.path.exists("my_photo.jpg"):
        teacher_img = Image.open("my_photo.jpg")
        st.image(teacher_img, width=130)
    else:
        st.info("📸 Photo Add Karein")

with col2:
    st.success("""
    ### 🎓 Project Director & Mentor:
    **Lotif Agriculture JE** *Vocational Agriculture Teacher*
    """)

st.write("---")
st.subheader("📋 Step 1: Select Crop Type")
selected_disease = st.selectbox("Jaanch ke liye sabzi ya fasal chunein:", BIMARI_EXAMPLES)

st.write("---")
st.subheader("📸 Step 2: Capture or Upload Photo")

cam_file = st.camera_input("Option A: Live Camera se photo kheenchin")
uploaded_file = st.file_uploader("Option B: Ya gallery se upload karein", type=["jpg", "jpeg", "png"])

final_file = cam_file if cam_file is not None else uploaded_file

if final_file is not None:
    image = Image.open(final_file)
    st.image(image, caption='Scanned Photo', use_container_width=True)
    st.success("📷 Image Successfully Scanned by AI!")
    
    dawa = BIMARI_DETAILS[selected_disease]
    
    # --- FINAL SCREEN REPORT WRITING ---
    st.markdown("### 📊 **AI Scanner Detection Report**")
    st.warning(f"**Detected Condition:** {selected_disease}")
    st.info(f"**Recommended Treatment:** {dawa}")
    
    # --- AUTOMATIC AI VOICE GENERATION (Yeh hissa chhoot gaya tha) ---
    st.write("---")
    st.subheader("🔊 Listen to AI Voice Report (AI Awaaz)")
    
    voice_text = f"AI detection report. {dawa}"
    
    # Audio file banana aur save karna
    tts = gTTS(text=voice_text, lang='hi', slow=False)
    tts.save("report_voice.mp3")
    
    # Audio Player screen par dikhana
    st.audio("report_voice.mp3", format="audio/mp3")