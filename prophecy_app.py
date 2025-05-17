import streamlit as st

st.set_page_config(page_title="PROPHECY LIVE", layout="wide")
st.title("🔮 PROPHECY is volledig geladen")
st.markdown("Welkom bij de volledige versie van PROPHECY – v1 t/m v30. Kies hieronder je functie.")

menu = st.sidebar.selectbox("📂 Modules", [
    "Objectanalyse", "Pitch & AI", "Portfolio", "Kaart", "Risico", "Lead & Rapport", "Financiering", "PDF & Dataroom"
])

if menu == "Objectanalyse":
    st.header("📍 Objectanalyse")
    adres = st.text_input("Adres", "Willemsparkweg 88")
    prijs = st.number_input("Vraagprijs (€)", 100000, 2000000, 440000, 5000)
    huur = st.number_input("Huur per maand (€)", 500, 10000, 1750, 50)
    m2 = st.number_input("Oppervlakte (m²)", 20, 300, 90, 5)
    etages = st.slider("Aantal etages", 1, 5, 2)
    if st.button("🚀 Analyseer"):
        rendement = round((huur * 12 * 0.75) / prijs, 4)
        potentie = "Opbouw mogelijk" if m2 > 90 and etages < 3 else "Beperkt"
        st.success(f"Netto rendement: {rendement*100:.2f}%")
        st.info(f"Potentie: {potentie}")

elif menu == "Pitch & AI":
    st.header("📝 Pitch & AI")
    st.text_area("📩 Genereerde pitch", "Voer eerst een analyse uit...")
    st.markdown("AI-coaching en aanbevelingen volgen in deze sectie.")

elif menu == "Portfolio":
    st.header("📊 Portfolio")
    st.markdown("Overzicht en totalen van al jouw gescande objecten.")

elif menu == "Kaart":
    st.header("🗺️ Kaartvisualisatie")
    st.markdown("Visualiseer jouw objecten per regio met risicokleuring.")

elif menu == "Risico":
    st.header("⚠️ Risico & Alerts")
    st.markdown("AI-risicoscore en externe meldingen per object.")

elif menu == "Lead & Rapport":
    st.header("📥 Leadgeneratie & Rapportage")
    st.markdown("Genereer PDF's, stuur rapporten en volg leads op.")

elif menu == "Financiering":
    st.header("💰 Financieringsanalyse")
    st.markdown("Bereken maandlasten, ROI, en biedingsscenario's.")

elif menu == "PDF & Dataroom":
    st.header("📄 PDF-export & Dataroom")
    st.markdown("Upload contracten en plan overdrachtsmomenten.")
