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
    st.header("⚠️ Risicoanalyse & Vastgoedalerts")

    portfolio = [
        {'adres': 'Prinsengracht 123', 'risico': 0.2, 'melding': False},
        {'adres': 'Appelhoutstraat 16', 'risico': 0.4, 'melding': True},
        {'adres': 'Willemsparkweg 88', 'risico': 0.6, 'melding': False},
        {'adres': 'Singel 89', 'risico': 0.8, 'melding': True}
    ]

    for obj in portfolio:
        kleur = "🟢" if obj['risico'] < 0.3 else "🟡" if obj['risico'] < 0.6 else "🔴"
        status = "Geen alert" if not obj['melding'] else "⚠️ Externe melding actief"
        with st.expander(f"{kleur} {obj['adres']} – Risico: {obj['risico']*100:.0f}%"):
            st.markdown(f"- Risiconiveau: **{obj['risico']*100:.0f}%**")
            st.markdown(f"- Status: {status}")
            if obj['risico'] > 0.5:
                st.warning("AI-advies: Vermijd aankoop tenzij prijs fors onder markt ligt.")
            elif obj['risico'] > 0.3:
                st.info("AI-advies: Voer due diligence uit op vergunningen, meldingen, huurders.")
            else:
                st.success("AI-advies: Object lijkt stabiel op basis van huidige signalen.")

    st.subheader("📊 Gemiddeld risico profiel")
    gem_risico = sum(p['risico'] for p in portfolio) / len(portfolio)
    st.metric("Gemiddeld risico", f"{gem_risico*100:.1f}%")

    if gem_risico > 0.6:
        st.error("🚨 Hoge blootstelling aan risicogebieden.")
    elif gem_risico > 0.4:
        st.warning("⚠️ Risico is gemiddeld. Monitor nauwgezet.")
    else:
        st.success("✅ Portefeuille is relatief stabiel.")

elif menu == "Lead & Rapport":
    st.header("📥 Leadgenerator & rapport")

    pitch_adres = st.text_input("Adres", "Willemsparkweg 88")
    pitch_prijs = st.number_input("Vraagprijs (€)", value=440000)
    pitch_huur = st.number_input("Huur (€)", value=1750)
    pitch_rendement = round((pitch_huur * 12 * 0.75) / pitch_prijs, 4)
    pitch_potentie = "Opbouw mogelijk" if pitch_rendement > 0.05 else "Beperkt"

    pitch = f"""{pitch_adres}
Vraagprijs: €{pitch_prijs}
Huur: €{pitch_huur}/maand
Netto rendement: {pitch_rendement*100:.2f}%
Potentie: {pitch_potentie}

Contacteer Team PROPHECY voor meer info."""

    st.text_area("📄 Pitchtekst / Rapport", pitch, height=180)

    lead_opvolging = st.radio("Leadstatus", ["Niet aangemaakt", "Open", "Opgevolgd"])
    if lead_opvolging == "Open":
        st.warning("Lead is nog niet opgevolgd.")
    elif lead_opvolging == "Opgevolgd":
        st.success("✅ Lead is opgevolgd. Verwerk in je CRM.")

elif menu == "Financiering":
    st.header("💰 Financiering & Onderhandeling")

    prijs = st.number_input("Vraagprijs (€)", value=440000)
    inbreng = st.number_input("Eigen inbreng (€)", value=80000)
    rente = st.slider("Rente (%)", 1.0, 6.0, 3.5)
    looptijd = st.slider("Looptijd (jaar)", 10, 30, 20)
    huur = st.number_input("Huur per maand (€)", value=1750)

    geleend = prijs - inbreng
    maandlast = ((geleend * (rente / 100)) + (geleend / looptijd)) / 12
    huur_jaar = huur * 12
    netto = huur_jaar - maandlast * 12
    roi = round((netto / inbreng) * 100, 2) if inbreng else 0

    st.markdown(f"- 💸 Geleend: €{geleend:,}")
    st.markdown(f"- 📉 Maandlast: €{int(maandlast)}")
    st.markdown(f"- 📈 Netto cashflow: €{int(netto)} p.j.")
    st.markdown(f"- ROI op inbreng: **{roi}%**")

    st.subheader("🤝 Onderhandeling")
    bod = st.slider("Stel alternatief bod voor (€)", prijs - 100000, prijs, prijs - 25000, 5000)
    nieuw_ge = bod - inbreng
    maandlast_nieuw = ((nieuw_ge * (rente / 100)) + (nieuw_ge / looptijd)) / 12
    netto_nieuw = huur_jaar - maandlast_nieuw * 12
    roi_nieuw = round((netto_nieuw / inbreng) * 100, 2)

    st.markdown(f"- 🧮 Nieuwe maandlast: €{int(maandlast_nieuw)}")
    st.markdown(f"- 🧾 Nieuwe cashflow: €{int(netto_nieuw)}")
    st.markdown(f"- 📈 Nieuwe ROI: **{roi_nieuw}%**")

    if roi_nieuw > roi:
        st.success("🔼 Beter rendement: bod is strategisch sterk.")
    elif roi_nieuw < roi:
        st.warning("⬇️ Minder rendement: alleen zinvol bij andere voordelen.")
    else:
        st.info("⚖️ Vergelijkbaar rendement. Onderhandel slim.")

elif menu == "PDF & Dataroom":
    import datetime

    st.header("📁 Dataroom & Ondertekening")

    st.subheader("📂 Upload documentatie")
    woz = st.file_uploader("WOZ-beschikking")
    splitsing = st.file_uploader("Splitsingsakte")
    huur = st.file_uploader("Huurcontract")
    energielabel = st.file_uploader("Energielabel")

    uploads = [woz, splitsing, huur, energielabel]
    if all(uploads):
        st.success("✅ Alle documenten geüpload")
    else:
        st.warning("⚠️ Nog niet alle documenten geüpload")

    st.subheader("📅 Aankoopplanning")
    optie = st.date_input("Optie geldig tot", value=datetime.date.today())
    inspectie = st.date_input("Inspectiedatum")
    transport = st.date_input("Transportdatum")

    st.markdown(f"- Optie tot: **{optie}**")
    st.markdown(f"- Inspectie: **{inspectie}**")
    st.markdown(f"- Transport: **{transport}**")

    st.subheader("✍️ Ondertekening")
    naam = st.text_input("Naam ondertekenaar")
    if st.button("Onderteken intentieverklaring") and naam:
        st.success(f"Document digitaal ondertekend door {naam}")
        st.balloons()

    st.subheader("📄 PDF-samenvatting (simulatie)")
    st.markdown("Rapportgegevens + handtekening + planning gereed voor PDF-export.")
