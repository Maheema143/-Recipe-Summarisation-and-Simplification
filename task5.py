import streamlit as st
import google.generativeai as genai

# ===============================
# Gemini API Configuration
# ===============================
genai.configure(api_key="YOUR_API_KEY")  # Replace with your actual key
model = genai.GenerativeModel("gemini-1.5-pro-latest")

# ===============================
# Streamlit Page Setup
# ===============================
st.set_page_config(
    page_title="Smart Recipe Helper 🍳",
    page_icon="🧑‍🍳",
    layout="wide"
)

# ===============================
# Sidebar
# ===============================
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3172/3172602.png", width=100)
    st.title("🍲 Recipe Assistant")
    st.markdown("**Powered by Gemini AI**")
    st.markdown("---")
    st.caption("Paste any complex recipe and get a simplified, easy-to-follow version!")

# ===============================
# Main Layout
# ===============================
st.markdown("<h1 style='text-align: center;'>🧑‍🍳 AI Recipe Simplifier</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Making cooking easier, one recipe at a time.</p>", unsafe_allow_html=True)
st.markdown("---")

# Input Section
col1, col2 = st.columns([2, 1])

with col1:
    recipe_input = st.text_area(
        label="📋 Paste Your Recipe",
        placeholder="e.g., 1. Preheat oven to 350°F. 2. Mix flour and sugar...",
        height=300
    )

with col2:
    st.markdown("### ⚙️ Options")
    add_tips = st.toggle("Include Cooking Tips", value=True)
    make_shorter = st.toggle("Make Recipe Even Shorter", value=False)

# Summarization Action
if st.button("✨ Simplify Recipe"):
    if not recipe_input.strip():
        st.warning("Please paste a recipe first.")
    else:
        with st.spinner("🤖 Gemini is simplifying your recipe..."):
            try:
                prompt = "Simplify the following recipe into clear steps:\n"
                if add_tips:
                    prompt += "- Include basic cooking tips.\n"
                if make_shorter:
                    prompt += "- Make it as concise as possible.\n"
                prompt += f"\n{recipe_input}"

                response = model.generate_content(prompt)
                simplified = response.text.strip()

                st.success("✅ Recipe Simplified!")
                st.subheader("🧾 Your Simplified Recipe")
                st.markdown(f"```markdown\n{simplified}\n```")

            except Exception as e:
                st.error(f"❌ Error: {str(e)[:300]}")

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Gemini API & Streamlit | Developed by Maheema")
