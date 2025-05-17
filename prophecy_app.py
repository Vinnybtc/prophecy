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
    
    pitch_adres = st.text_input("Adres", "Willemsparkweg 88")
    pitch_prijs = st.number_input("Vraagprijs (€)", value=440000)
    pitch_huur = st.number_input("Huur per maand (€)", value=1750)
    pitch_rendement = round((pitch_huur * 12 * 0.75) / pitch_prijs, 4)
    potentie = "Opbouw mogelijk" if pitch_rendement > 0.05 else "Beperkt"

    pitch_text = (
        f"{pitch_adres}\n"
        f"Vraagprijs: €{pitch_prijs}\n"
        f"Huur: €{pitch_huur}/maand\n"
        f"Netto rendement: {pitch_rendement*100:.2f}%\n"
        f"Potentie: {potentie}\n\n"
        "Geïnteresseerd? Neem contact op met Team PROPHECY."
    )

    st.subheader("📩 Pitchtekst")
    st.text_area("Automatisch gegenereerd", pitch_text, height=180)

    st.subheader("🤖 AI-aanbeveling (simulatie)")
    if pitch_rendement > 0.055:
        st.success("AI: Dit object scoort boven verwachting. Geschikt voor buy-to-let.")
    elif pitch_rendement > 0.045:
        st.info("AI: Gemiddeld rendement. Onderhandel slim en reken scenario’s door.")
    else:
        st.warning("AI: Laag rendement. Alleen overwegen bij unieke locatie of verbouwpotentie.")

elif menu == "Portfolio":
    st.header("📊 Portfolio")
    st.markdown("Overzicht en totalen van al jouw gescande objecten.")

elif menu == "Kaart":
    import pandas as pd
    import pydeck as pdk

    st.header("🗺️ Vastgoed op de kaart")

    objecten = pd.DataFrame([
        {"adres": "Prinsengracht 123", "lat": 52.3738, "lon": 4.8910, "rendement": 0.051, "risico": 0.2},
        {"adres": "Appelhoutstraat 16", "lat": 52.1017, "lon": 5.1155, "rendement": 0.048, "risico": 0.4},
        {"adres": "Willemsparkweg 88", "lat": 52.3566, "lon": 4.8673, "rendement": 0.056, "risico": 0.6},
        {"adres": "Singel 89", "lat": 52.3740, "lon": 4.8897, "rendement": 0.045, "risico": 0.8}
    ])

    kleurtype = st.radio("Kleur op basis van:", ["Rendement", "Risico"])

    if kleurtype == "Rendement":
        objecten["kleur"] = objecten["rendement"].apply(lambda x: [0, int(x*2000), 0])
    else:
        objecten["kleur"] = objecten["risico"].apply(lambda x: [int(x*255), 0, 0])

    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=pdk.ViewState(latitude=52.37, longitude=4.89, zoom=11, pitch=45),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=objecten,
                get_position='[lon, lat]',
                get_fill_color='kleur',
                get_radius=120,
                pickable=True
            )
        ]
    ))

    st.dataframe(objecten[["adres", "rendement", "risico"]])

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
