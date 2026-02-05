import streamlit as st
from scholarly import scholarly
import pandas as pd


# 1. PAGE CONFIGURATION
st.set_page_config(
    page_title="Kaveer Nagessar | Researcher Profile",
    page_icon="⚛️",
    layout="wide"
)



@st.cache_data(ttl=86400)
def get_scholar_data(scholar_id):
    try:
        author = scholarly.search_author_id(scholar_id)
        full_author = scholarly.fill(sections=['basics', 'indices', 'counts'])
        return full_author
    except Exception as e:
        # Fallback data so the site doesn't look broken
        return {
            "citedby": 5,  # Manual update required occasionally
            "hindex": 1,
            "i10index": 0,
            "publications": [] 
        }

# Your Google Scholar ID
scholar_id = "GIBw1REAAAAJ"
author_data = get_scholar_data(scholar_id)


# 3. SIDEBAR (Professional Social & Contact)
with st.sidebar:
    st.image("https://ui-avatars.com/api/?name=Kaveer+Nagessar&background=0D8ABC&color=fff&size=200", width=150)
    st.title("Kaveer Nagessar")
    st.write("📍 Pretoria, South Africa")
    st.write("🏛️ University of Pretoria")
    st.write("🎓 Physics Honours Student and Aspiring Physicist")
            

    
    st.divider()

    # --- PROFESSIONAL BUTTONS SECTION ---
    # CSS for uniform, sleek buttons
    button_style = """
        <style>
            .social-btn {
                display: flex;
                align-items: center;
                justify-content: center;
                background-color: #ffffff;
                border: 1px solid #ddd;
                border-radius: 8px;
                padding: 8px 12px;
                margin-bottom: 10px;
                color: #333 !important;
                text-decoration: none;
                font-weight: 500;
                font-size: 14px;
                transition: all 0.3s ease;
                box-shadow: 1px 1px 3px rgba(0,0,0,0.05);
            }
            .social-btn:hover {
                border-color: #0D8ABC;
                background-color: #f9f9f9;
                transform: translateY(-2px);
                box-shadow: 2px 4px 8px rgba(0,0,0,0.1);
            }
            .icon-img {
                width: 18px;
                margin-right: 12px;
            }
        </style>
    """
    st.markdown(button_style, unsafe_allow_html=True)

    # 1. Google Scholar Button
    st.markdown(f"""
        <a href="https://scholar.google.com/citations?user={scholar_id}" class="social-btn" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/c/c7/Google_Scholar_logo.svg" class="icon-img">
            Google Scholar
        </a>
    """, unsafe_allow_html=True)

    # 2. ResearchGate Button
    st.markdown(f"""
        <a href="https://www.researchgate.net/profile/Kaveer-Nagessar" class="social-btn" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/5/5e/ResearchGate_icon_SVG.svg" class="icon-img">
            ResearchGate
        </a>
    """, unsafe_allow_html=True)

    # 3. ORCID Button
    st.markdown(f"""
        <a href="https://orcid.org/0009-0000-9829-1608" class="social-btn" target="_blank">
            <img src="https://orcid.org/sites/default/files/images/orcid_16x16.png" class="icon-img">
            ORCID iD
        </a>
    """, unsafe_allow_html=True)

    st.divider()

    # 4. Email Button (Primary Action)
    email_address = "nagessar.kaveer@gmail.com" 
    st.markdown(f"""
        <a href="mailto:{email_address}?subject=Research Collaboration Inquiry" class="social-btn" 
           style="background-color: #0D8ABC; color: white !important; border: none;">
           📧 Contact via Email
        </a>
    """, unsafe_allow_html=True)

    st.divider()


# --- 4. MAIN HEADER & STATS ---
st.title("Academic & Research Portfolio")

if author_data:
    # This creates the 4 columns for your metrics at the top
    col1, col2, col3, col4 = st.columns(4)
    
    # Live stats from Google Scholar
    col1.metric("Citations", author_data.get("citedby", 0))
    col2.metric("h-index", author_data.get("hindex", 0))
    col3.metric("i10-index", author_data.get("i10index", 0))
    
    # Manual stat from your ResearchGate/Bio
    col4.metric("RG Research Interest", "15.7") 

    st.divider()

# --- 5. CONTENT TABS SECTION ---
tabs = st.tabs([
    "👤 About Me", 
    "🔬 Research Focus", 
    "📚 All Publications", 
    "🎓 Education",
    "✈️ Research Collaborations", 
    "👨‍🏫 Teaching", 
    "🛠️ Skills", 
    "🏆 Awards",
    "📞 Contact"
])

# --- TAB 1: ABOUT ME ---
with tabs[0]:
    st.subheader("Biography")
    st.write("""
    Kaveer Nagessar is a multidisciplinary and interdisciplinary researcher currently focused on various projects. He has a background in Physics, Material Science, Mathematics, and Astronomy. He has authored several papers in Medical Physics, General Material Science, and Astronomy, and enjoys investigating topics that span multiple disciplines.

He completed his undergraduate degree in 2025 with a major project applying Deep Level Transient Spectroscopy (DLTS) to silicon bipolar junction transistors, studying irradiation-induced deep-level defects. This work was the first to apply Laplace DLTS to bipolar junction transistors. Understanding the defects formed from irradiation in these electronic semiconductor devices has applications in space technology and nuclear environments.

Kaveer also won 2nd Place nationally in the ARSO-SABS National Essay Competition on Education about Standardization (2025), which earned him a bursary. He has collaborated with various researchers and attended several workshops.
    """)

# --- TAB 2: RESEARCH FOCUS ---
with tabs[1]:
    st.subheader("Electronic Materials & Semiconductor Physics")
    st.write("Current focus: **Electrical Characterization of Defects in Silicon Bipolar Junction Transistors Under Electron Irradiation.**")
    
    # Using a single markdown block with proper spacing
    st.markdown(r"""
Deep Level Transient Spectroscopy (DLTS) is a powerful technique used to characterize electrically active defects in semiconductors. These defects can trap carriers and affect device performance, especially in high-radiation environments.

The thermal emission rate of carriers from a trap is:

$$
e_n(T) = \sigma_n v_{th} N_C \exp\left(-\frac{E_T}{k_B T}\right)
$$

**Where:** 
* $e_n(T)$: electron emission rate  
* $\sigma_n$: capture cross-section of the trap  
* $v_{th}$: thermal velocity of electrons  
* $N_C$: effective density of states in the conduction band  
* $E_T$: trap energy level relative to conduction band  
* $k_B$: Boltzmann constant  
* $T$: absolute temperature

By analyzing the Arrhenius behavior:

$$
\ln\left(\frac{e_n}{T^2}\right) = \ln(\gamma \sigma_n) - \frac{E_T}{k_B T}
$$

> **Note:** In the Arrhenius plot, we often use $T^2$ because $v_{th} \propto T^{1/2}$ and $N_C \propto T^{3/2}$.

From this, both the activation energy $E_T$ and the capture cross-section $\sigma_n$ can be extracted.  

**Laplace DLTS** further improves the resolution to detect closely spaced defect levels, making it a powerful tool for studying defects in silicon BJTs.
    """)
    

    import pandas as pd
    import io
    import matplotlib.pyplot as plt
    
    # 1. THE DATA
    raw_data = """T	RW4
    349.81	2.73E-04
    349.735	-7.13E-04
    349.095	2.73E-04
    348.4	-6.72E-04
    348.005	-3.45E-04
    347.66	3.96E-04
    347.22	-6.50E-04
    346.735	1.02E-03
    346.23	6.12E-04
    345.835	-3.63E-04
    345.295	6.03E-04
    344.63	-1.37E-04
    344.185	-8.02E-04
    343.71	2.22E-04
    343.115	2.59E-04
    342.665	-3.57E-04
    342.29	-4.67E-04
    341.835	1.02E-04
    341.42	-5.59E-05
    340.955	5.03E-04
    340.445	-1.36E-04
    340.025	-3.71E-06
    339.57	5.33E-04
    339.085	-2.10E-04
    338.595	-1.09E-03
    337.95	1.21E-04
    337.42	-6.23E-04
    337.045	9.35E-04
    336.635	4.50E-04
    336.22	2.42E-04
    335.81	-2.93E-04
    335.295	-3.90E-04
    334.645	3.80E-04
    334.15	-3.93E-04
    333.585	4.14E-04
    333.12	-1.65E-04
    332.605	-3.00E-05
    332.015	5.84E-05
    331.535	-2.55E-03
    330.985	-9.40E-04
    330.445	9.35E-04
    330.04	4.93E-04
    329.62	-1.18E-03
    329.21	-9.58E-04
    328.705	-2.10E-03
    328.035	1.68E-04
    327.475	-1.78E-03
    327.115	5.56E-04
    326.69	-1.05E-04
    326.24	6.04E-04
    325.69	-4.55E-04
    324.985	6.06E-04
    324.65	-4.19E-04
    324.155	-2.01E-04
    323.55	-1.11E-03
    323.115	-7.49E-04
    322.715	-6.80E-05
    322.275	-6.81E-04
    321.8	4.52E-04
    321.325	6.49E-06
    320.84	-8.13E-04
    320.42	4.23E-04
    319.965	-2.64E-04
    319.515	-1.20E-04
    319.075	5.63E-04
    318.605	-8.22E-04
    318.165	-5.92E-04
    317.71	-1.16E-03
    317.26	-3.29E-04
    316.725	5.65E-04
    316.1	-2.33E-04
    315.605	-7.43E-04
    315.23	-2.85E-04
    314.835	-5.80E-04
    314.495	-1.96E-04
    313.995	-7.46E-04
    313.29	-3.97E-04
    312.825	-7.62E-04
    312.48	-2.02E-04
    312.04	-9.60E-04
    311.575	-3.68E-04
    311.09	4.31E-04
    310.65	-2.96E-04
    310.21	-8.65E-04
    309.585	-1.02E-05
    309.015	-4.84E-04
    308.635	-5.95E-04
    308.23	-3.32E-04
    307.79	2.23E-04
    307.335	-2.91E-04
    306.85	-5.32E-04
    306.435	3.19E-04
    305.88	-1.15E-04
    305.225	-5.36E-04
    304.84	-1.55E-07
    304.26	-4.96E-05
    303.74	-5.36E-04
    303.365	-7.79E-04
    302.895	1.83E-04
    302.34	-1.90E-03
    301.76	2.82E-04
    301.165	-1.84E-03
    300.71	-3.28E-05
    300.125	1.80E-04
    299.53	-2.84E-04
    299.185	-7.06E-05
    298.785	-4.71E-05
    298.32	-6.27E-04
    297.825	-9.47E-04
    297.35	1.76E-05
    296.945	-3.36E-04
    296.5	-1.19E-05
    295.835	-8.34E-04
    295.29	-1.21E-03
    294.92	-3.55E-04
    294.53	-1.21E-03
    294.04	1.48E-04
    293.5	-5.30E-04
    292.87	7.17E-05
    292.47	-3.36E-04
    292.11	-1.16E-05
    291.63	2.86E-04
    291.165	-1.77E-04
    290.72	-4.72E-04
    290.3	-1.68E-04
    289.88	-4.78E-04
    289.44	-4.30E-04
    288.95	-4.51E-04
    288.535	1.10E-04
    288.005	1.18E-04
    287.35	-1.67E-04
    286.925	9.31E-05
    286.46	-3.42E-04
    285.835	-3.01E-04
    285.36	-1.73E-04
    284.82	-1.35E-03
    284.245	-9.08E-04
    283.765	-5.77E-05
    283.145	-5.48E-04
    282.655	-2.98E-04
    282.31	-8.87E-05
    281.87	-1.32E-04
    281.435	-9.50E-05
    280.965	-9.32E-05
    280.49	-5.52E-05
    280.06	-6.95E-07
    279.605	-2.67E-04
    279.175	2.36E-04
    278.73	-1.74E-04
    278.25	1.55E-04
    277.85	-9.23E-05
    277.205	7.02E-05
    276.595	-2.11E-04
    276.135	1.11E-04
    275.585	1.03E-04
    275.045	1.32E-05
    274.54	2.34E-04
    273.92	-1.03E-04
    273.465	6.75E-04
    272.935	-4.64E-04
    272.315	-2.63E-04
    271.875	1.15E-04
    271.46	-4.65E-05
    271.04	8.70E-05
    270.555	-3.00E-05
    270.1	-6.43E-04
    269.61	-9.20E-04
    268.94	-3.57E-04
    268.445	8.04E-06
    268.06	-2.94E-05
    267.615	2.62E-04
    267.22	-1.23E-04
    266.775	-6.31E-04
    266.3	-7.08E-04
    265.865	-3.40E-04
    265.375	-4.00E-04
    264.9	3.09E-04
    264.47	2.54E-05
    264.01	-1.40E-04
    263.59	-3.25E-04
    263.175	-1.06E-04
    262.76	-4.31E-04
    262.275	-1.94E-04
    261.74	-3.42E-04
    261.325	-2.10E-04
    260.73	1.54E-04
    260.11	-4.20E-04
    259.805	2.36E-04
    259.29	-3.64E-04
    258.64	7.91E-05
    258.22	1.39E-05
    257.835	1.14E-04
    257.385	-1.36E-04
    256.895	-1.74E-04
    256.265	2.75E-04
    255.71	-7.12E-05
    255.375	2.12E-05
    254.97	8.95E-05
    254.46	-1.45E-04
    254.04	-1.59E-04
    253.485	9.27E-05
    252.81	4.99E-04
    252.315	1.13E-04
    251.93	-4.22E-04
    251.435	-7.62E-04
    250.965	-4.50E-05
    250.52	-5.29E-05
    250.055	-3.91E-05
    249.65	2.70E-04
    249.08	-2.08E-04
    248.43	-2.18E-04
    248	-3.10E-04
    247.605	1.99E-04
    247.21	-2.47E-05
    246.66	2.79E-04
    246	7.42E-05
    245.465	5.85E-04
    244.945	2.80E-05
    244.44	-1.99E-04
    243.955	2.50E-04
    243.345	-1.08E-05
    242.85	-1.31E-04
    242.445	-3.49E-04
    242	4.85E-04
    241.495	2.46E-05
    240.84	-1.65E-04
    240.335	4.13E-05
    239.945	-7.73E-05
    239.535	1.44E-04
    239.08	5.57E-04
    238.595	2.48E-04
    238.17	-2.88E-05
    237.725	4.99E-04
    237.265	2.52E-04
    236.82	-5.89E-06
    236.355	4.90E-04
    235.95	4.50E-05
    235.41	2.35E-04
    234.755	3.48E-04
    234.29	-2.50E-06
    233.85	3.70E-04
    233.455	-4.24E-05
    232.905	-1.11E-04
    232.25	1.17E-05
    231.79	-2.09E-05
    231.4	3.49E-04
    230.985	1.11E-04
    230.535	6.66E-05
    230.05	9.43E-05
    229.64	-3.28E-04
    229.08	5.82E-04
    228.445	1.05E-03
    228.005	3.15E-05
    227.6	8.40E-04
    227.18	5.92E-04
    226.72	5.52E-04
    226.25	5.72E-04
    225.825	6.23E-04
    225.365	-6.27E-04
    224.915	-2.14E-04
    224.465	-2.50E-04
    223.96	8.20E-05
    223.495	9.70E-04
    222.88	2.35E-04
    222.355	2.68E-04
    221.87	-1.06E-03
    221.28	2.21E-04
    220.81	3.51E-04
    220.395	4.92E-04
    220	1.60E-04
    219.49	3.79E-04
    218.835	-1.49E-04
    218.335	1.63E-04
    217.945	4.16E-04
    217.525	-1.30E-04
    217.08	5.87E-05
    216.555	3.97E-04
    216.14	-6.89E-05
    215.605	1.24E-04
    214.96	-7.81E-05
    214.495	7.86E-04
    214.1	9.73E-05
    213.705	7.31E-05
    213.11	3.39E-04
    212.45	5.22E-04
    212.035	9.30E-04
    211.665	-2.24E-06
    211.185	-1.96E-04
    210.725	-3.01E-04
    210.25	-2.46E-04
    209.815	-1.14E-03
    209.37	-2.87E-04
    208.89	7.06E-04
    208.5	-3.46E-04
    208.11	5.60E-05
    207.595	-4.83E-04
    206.945	-1.80E-04
    206.515	-2.99E-04
    206.105	-3.69E-05
    205.69	-8.96E-05
    205.22	3.25E-04
    204.76	-1.25E-03
    204.315	-9.06E-04
    203.85	-5.87E-04
    203.425	-5.30E-04
    202.97	2.57E-04
    202.51	-8.23E-04
    202.065	5.17E-04
    201.6	-1.34E-04
    201.16	1.40E-04
    200.7	5.49E-04
    200.26	5.93E-04
    199.83	2.67E-04
    199.355	4.73E-04
    198.92	-1.13E-03
    198.415	1.71E-03
    197.95	-1.87E-04
    197.52	-6.37E-04
    197.06	5.13E-04
    196.6	1.52E-04
    196.235	3.71E-04
    195.775	-4.54E-04
    195.31	-4.50E-04
    194.81	5.73E-04
    194.2	1.78E-04
    193.695	2.22E-04
    193.29	5.93E-05
    192.83	6.22E-04
    192.32	-4.13E-05
    191.695	4.67E-04
    191.185	-4.86E-05
    190.785	9.80E-05
    190.38	2.55E-05
    189.91	1.07E-04
    189.28	2.84E-04
    188.73	1.51E-04
    188.325	7.04E-04
    187.905	3.68E-04
    187.545	6.24E-04
    187.09	9.33E-05
    186.6	5.98E-04
    186.155	2.29E-04
    185.655	5.27E-04
    185.235	-1.44E-04
    184.7	1.51E-03
    184.06	1.69E-03
    183.59	-6.49E-04
    183.145	1.66E-03
    182.735	1.34E-03
    182.225	1.32E-03
    181.595	9.48E-04
    181.095	7.31E-04
    180.66	1.30E-03
    180.225	1.24E-03
    179.78	1.97E-03
    179.31	1.61E-03
    178.84	1.51E-03
    178.415	1.87E-03
    177.955	1.61E-03
    177.505	2.72E-03
    177.01	2.48E-03
    176.4	1.76E-03
    175.915	2.29E-03
    175.42	1.87E-03
    174.825	1.95E-03
    174.37	2.09E-03
    173.955	2.49E-03
    173.475	2.30E-03
    173.03	2.35E-03
    172.545	3.09E-03
    172.115	2.39E-03
    171.67	1.39E-03
    171.195	2.09E-03
    170.765	2.45E-03
    170.2	1.65E-03
    169.595	2.64E-03
    169.165	1.66E-03
    168.71	2.38E-03
    168.285	2.27E-03
    167.835	2.02E-03
    167.345	1.26E-03
    166.915	1.72E-03
    166.47	2.36E-03
    165.995	1.79E-03
    165.625	1.75E-03
    165.19	1.72E-03
    164.765	1.88E-03
    164.21	1.56E-03
    163.555	1.75E-03
    163.105	1.40E-03
    162.705	1.23E-03
    162.11	8.89E-04
    161.545	9.39E-04
    161.125	9.80E-04
    160.71	1.29E-03
    160.275	7.74E-04
    159.755	1.37E-03
    159.305	7.94E-04
    158.845	8.32E-04
    158.39	7.50E-04
    158.025	1.37E-03
    157.435	-1.21E-04
    156.815	1.16E-03
    156.335	5.22E-04
    155.75	2.88E-04
    155.26	1.10E-03
    154.84	1.07E-03
    154.415	4.14E-04
    153.925	8.20E-04
    153.26	2.36E-04
    152.73	8.27E-04
    152.325	5.18E-04
    151.955	8.66E-04
    151.42	3.62E-04
    150.73	5.52E-04
    150.215	1.44E-03
    149.67	1.22E-03
    149.17	2.04E-03
    148.75	1.07E-03
    148.31	1.22E-03
    147.865	1.87E-03
    147.4	1.40E-03
    146.96	2.18E-03
    146.51	1.66E-03
    146.095	1.29E-03
    145.735	1.46E-03
    145.16	1.51E-03
    144.545	1.04E-03
    144.11	1.96E-03
    143.7	1.57E-03
    143.28	1.25E-03
    142.705	1.19E-03
    142.105	9.02E-04
    141.66	7.41E-04
    141.25	1.19E-03
    140.86	1.17E-03
    140.285	8.98E-04
    139.64	5.43E-04
    139.16	3.65E-05
    138.75	4.78E-04
    138.36	-2.30E-04
    137.785	-2.23E-04
    137.135	-5.25E-06
    136.665	-1.09E-04
    136.145	-1.87E-04
    135.62	-4.36E-04
    135.165	-4.55E-04
    134.59	-4.09E-04
    134.055	-1.25E-03
    133.63	-4.47E-04
    133.2	-5.75E-04
    132.765	-9.60E-04
    132.25	-6.47E-04
    131.82	-4.97E-04
    131.375	-6.64E-04
    130.9	-5.08E-04
    130.455	-1.08E-03
    130	-8.60E-04
    129.59	-1.30E-03
    129.055	-9.01E-04
    128.41	-3.18E-04
    127.98	-1.63E-04
    127.5	-4.49E-04
    126.88	-3.41E-04
    126.395	-4.29E-04
    125.98	-4.35E-04
    125.555	-6.12E-04
    125.125	-7.13E-04
    124.53	-6.51E-04
    123.935	-5.33E-04
    123.455	-9.19E-04
    122.905	-1.05E-03
    122.415	-7.35E-04
    121.99	-6.51E-04
    121.555	-9.73E-04
    121.125	-1.78E-03
    120.53	-6.15E-04
    119.94	-2.63E-04
    119.52	-1.72E-03
    119.105	-5.62E-04
    118.675	-2.87E-04
    118.21	-6.37E-04
    117.76	-1.10E-04
    117.31	-4.80E-04
    116.845	-1.91E-04
    116.43	-3.71E-04
    115.98	-5.39E-04
    115.495	-3.93E-04
    115.055	2.65E-04
    114.605	3.19E-04
    114.155	-1.01E-03
    113.73	6.69E-04
    113.27	-9.67E-05
    112.84	1.15E-03
    112.3	5.38E-04
    111.665	8.47E-04
    111.195	7.61E-04
    110.785	5.81E-04
    110.375	1.25E-03
    109.94	1.06E-03
    109.455	1.75E-03
    109.005	1.81E-03
    108.555	1.17E-03
    108.1	2.18E-03
    107.665	2.96E-03
    107.205	1.85E-03
    106.76	3.03E-03
    106.31	2.50E-03
    105.865	3.73E-03
    105.42	3.62E-03
    104.95	3.04E-03
    104.515	3.59E-03
    104.06	3.38E-03
    103.6	2.66E-03
    103.165	3.14E-03
    102.66	2.99E-03
    102.215	3.02E-03
    101.76	4.45E-03
    101.315	2.53E-03
    100.87	3.61E-03
    100.35	2.07E-03
    99.9105	2.81E-03
    99.4595	3.43E-03
    98.9675	2.70E-03
    98.51151	2.28E-03
    98.0615	1.68E-03
    97.59399	1.69E-03
    96.986	2.19E-03
    96.428	1.41E-03
    95.9245	1.21E-03
    95.3305	8.45E-04
    94.8715	1.63E-03
    94.448	-3.54E-04
    94.0255	1.43E-03
    93.5095	7.53E-04
    92.886	1.20E-03
    92.4055	9.47E-04
    92.004	7.33E-04
    91.55901	8.93E-04
    91.1265	6.78E-04
    90.673	6.42E-04
    90.1955	5.70E-04
    89.7645	6.34E-04
    89.325	7.07E-04
    88.8495	2.64E-04
    88.412	6.73E-04
    87.9815	2.76E-04
    87.5095	-4.98E-05
    87.064	1.06E-04
    86.623	1.73E-04
    86.1465	5.65E-04
    85.7485	5.90E-05
    85.2105	4.89E-04
    84.569	1.61E-04
    84.105	2.56E-04
    83.5755	4.24E-04
    83.0495	9.26E-04
    82.6345	1.62E-03
    82.237	1.25E-03
    81.7645	2.59E-03
    81.2675	2.73E-03
    80.81799	2.38E-03
    80.345	2.81E-03
    79.932	3.45E-03
    79.48	3.77E-03
    78.9935	3.33E-03
    78.565	3.56E-03
    78.113	3.87E-03
    77.651	3.62E-03
    77.2175	4.59E-03
    76.6225	4.15E-03
    76.05299	3.85E-03
    75.5665	3.53E-03
    74.9895	2.94E-03
    74.5405	2.52E-03
    73.9575	2.88E-03
    73.354	1.99E-03
    72.939	2.14E-03
    72.5235	2.09E-03
    72.032	9.63E-04
    71.5725	1.75E-03
    71.12801	1.09E-03
    70.6785	5.92E-04
    70.18	8.74E-04
    69.733	9.39E-04
    69.283	7.03E-04
    68.7835	3.43E-04
    68.312	3.47E-04
    67.8575	-4.59E-05
    67.3985	8.25E-05
    66.9705	5.23E-04
    66.52	3.07E-05
    66.0765	3.37E-04
    65.5745	-1.20E-04
    65.10049	4.28E-05
    64.65849	1.26E-04
    64.0815	2.30E-03
    63.531	1.43E-03
    63.103	-4.37E-04
    62.659	3.73E-04
    62.2655	-5.87E-04
    61.6845	8.06E-04
    61.061	-5.38E-04
    60.634	-2.62E-04
    60.209	2.63E-04
    59.811	2.21E-04
    59.2485	4.39E-04
    58.629	7.64E-05
    58.19	1.92E-04
    57.7605	6.41E-04
    57.323	2.19E-04
    56.885	-3.93E-04
    56.411	-6.87E-05
    55.9705	-2.12E-04
    55.5195	-3.26E-04
    55.0565	1.12E-04
    54.61	4.14E-04
    54.0095	-2.65E-04
    53.4725	-4.20E-04
    53.0445	-9.84E-05
    52.5375	-2.23E-04
    52.14	-3.01E-04
    51.679	5.24E-04
    51.198	-2.02E-04
    50.7445	2.13E-04
    50.1505	1.17E-04
    49.6375	-2.87E-04
    49.171	-1.05E-04
    48.71	2.34E-04
    48.272	-2.28E-04
    47.807	-1.91E-04
    47.434	2.12E-04
    46.811	2.97E-04
    46.17	5.24E-04
    45.7335	-4.37E-04
    45.1625	-6.15E-04
    44.66	-2.62E-04
    44.2385	-6.48E-05
    43.7705	-9.09E-04
    43.343	-1.66E-04
    42.879	-4.26E-04
    42.397	-4.44E-04
    41.9385	-8.56E-04
    41.472	-8.90E-04
    41.0035	-1.27E-04
    40.4115	-3.44E-04
    39.9725	-1.49E-03
    39.418	-9.85E-04
    38.7495	-4.66E-04
    38.296	-3.75E-04
    37.7155	-1.46E-03
    37.245	-7.46E-04
    36.804	-1.12E-03
    36.2805	-1.86E-03
    35.8335	-1.94E-03
    35.368	-2.12E-03
    34.9105	-2.19E-03
    34.3225	-3.93E-03
    33.812	-3.03E-03
    33.3935	-4.07E-03
    32.8085	-4.93E-03
    32.3605	-3.27E-03
    31.9125	-1.45E-03"""
    
    # 2. PROCESSING
    df = pd.read_csv(io.StringIO(raw_data), sep='\t')
    

    
    # Option A: Interactive Native Streamlit Chart
    st.subheader("Interactive DLTS Signal")
    # Set T as index for the native chart
    chart_df = df.set_index('T')
    st.line_chart(chart_df)
    
    # Option B: Matplotlib (Better for Publications/Labels)
    st.subheader("Final DLTS Spectrum of a Silicon BJT")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df['T'], df['RW4'], color='red', label='RW4 Signal')
    ax.set_xlabel("Temperature (K)")
    ax.set_ylabel("Capacitance (RW4)")
    ax.grid(True, which='both', linestyle='--', alpha=0.5)
    ax.legend()
    
    st.pyplot(fig)
    
    # Option C: Data Table
    with st.expander("Show Raw Data Table"):
        st.dataframe(df, use_container_width=True)

    import numpy as np
    import plotly.graph_objects as go
    
    # -----------------------------
    # Parameters
    # -----------------------------
    a = 5.43
    n = 2
    si_size = 9
    b_size = 10
    vac_size = 10
    bond_cutoff = 2.6
    
    # CPK colours
    SI_COLOR = "black"
    B_COLOR = "blue"
    VAC_COLOR = "red"
    BOND_COLOR = "gray"
    
    # Diamond cubic basis
    basis = np.array([
        [0,   0,   0],
        [0,   0.5, 0.5],
        [0.5, 0,   0.5],
        [0.5, 0.5, 0],
        [0.25, 0.25, 0.25],
        [0.25, 0.75, 0.75],
        [0.75, 0.25, 0.75],
        [0.75, 0.75, 0.25],
    ])
    
    # -----------------------------
    # Build lattice
    # -----------------------------
    atoms = []
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for b in basis:
                    atoms.append(a * (b + [i, j, k]))
    
    atoms = np.array(atoms)
    
    # -----------------------------
    # Choose defect sites
    # -----------------------------
    center = atoms.mean(axis=0)
    dist = np.linalg.norm(atoms - center, axis=1)
    
    # Boron substitution (closest to center)
    b_index = np.argmin(dist)
    boron = atoms[b_index]
    
    # Vacancy = nearest neighbour to boron
    dist_to_b = np.linalg.norm(atoms - boron, axis=1)
    dist_to_b[b_index] = np.inf
    vac_index = np.argmin(dist_to_b)
    vacancy = atoms[vac_index]
    
    # Remaining silicon atoms
    mask = np.ones(len(atoms), dtype=bool)
    mask[[b_index, vac_index]] = False
    silicon = atoms[mask]
    
    # -----------------------------
    # Bonds (excluding vacancy)
    # -----------------------------
    bond_x, bond_y, bond_z = [], [], []
    
    all_atoms = np.vstack([silicon, boron])
    
    for i in range(len(all_atoms)):
        for j in range(i + 1, len(all_atoms)):
            d = np.linalg.norm(all_atoms[i] - all_atoms[j])
            if d < bond_cutoff:
                bond_x += [all_atoms[i,0], all_atoms[j,0], None]
                bond_y += [all_atoms[i,1], all_atoms[j,1], None]
                bond_z += [all_atoms[i,2], all_atoms[j,2], None]
    
    # -----------------------------
    # Unit cell
    # -----------------------------
    L = n * a
    edges = [
        ([0,L],[0,0],[0,0]), ([0,L],[L,L],[0,0]),
        ([0,L],[0,0],[L,L]), ([0,L],[L,L],[L,L]),
        ([0,0],[0,L],[0,0]), ([L,L],[0,L],[0,0]),
        ([0,0],[0,L],[L,L]), ([L,L],[0,L],[L,L]),
        ([0,0],[0,0],[0,L]), ([L,L],[0,0],[0,L]),
        ([0,0],[L,L],[0,L]), ([L,L],[L,L],[0,L]),
    ]
    
    # -----------------------------
    # Plot
    # -----------------------------
    fig = go.Figure()
    
    # Bonds
    fig.add_trace(go.Scatter3d(
        x=bond_x, y=bond_y, z=bond_z,
        mode="lines",
        line=dict(color=BOND_COLOR, width=4),
        name="Bonds"
    ))
    
    # Silicon atoms
    fig.add_trace(go.Scatter3d(
        x=silicon[:,0], y=silicon[:,1], z=silicon[:,2],
        mode="markers",
        marker=dict(size=si_size, color=SI_COLOR),
        name="Si"
    ))
    
    # Boron atom
    fig.add_trace(go.Scatter3d(
        x=[boron[0]], y=[boron[1]], z=[boron[2]],
        mode="markers",
        marker=dict(size=b_size, color=B_COLOR),
        name="B"
    ))
    
    # Vacancy marker (explicit)
    fig.add_trace(go.Scatter3d(
        x=[vacancy[0]], y=[vacancy[1]], z=[vacancy[2]],
        mode="markers",
        marker=dict(size=vac_size, color=VAC_COLOR, symbol="x"),
        name="Vacancy"
    ))
    
    # Unit cell
    for e in edges:
        fig.add_trace(go.Scatter3d(
            x=e[0], y=e[1], z=e[2],
            mode="lines",
            line=dict(color="black", width=2),
            showlegend=False
        ))
    
    fig.update_layout(
        title="Silicon Lattice with Boron-Vaccancy Defect",
        scene=dict(
            aspectmode="cube",
            xaxis_visible=False,
            yaxis_visible=False,
            zaxis_visible=False
        )
    )
    
    st.plotly_chart(fig)

    

#--- TAB 3: PUBLICATIONS ---
with tabs[2]:
    st.subheader("Full Publication List")
    
    # 1. HARDCODED FALLBACK DATA (Because Scholar can be unreliable)
    # This ensures your profile always looks professional
    manual_pubs = [
        {
            "year": 2025,
            "title": "Advanced thermal and magnetic materials for high-power and high-temperature applications: a comprehensive review",
            "authors": "WG Mengesha, K Nagessar",
            "source": "Discover Materials 5"
        },
        {
            "year": 2025,
            "title": "A critical review on electronic materials properties and multifunctional applications",
            "authors": "WG Mengesha, K Nagessar",
            "source": "Discover Materials 5 (1)"
        },
        {
            "year": 2025,
            "title": "Electrical Characterization of Defects in a Commercial Silicon Bipolar Junction Transistor Under Electron Irradiation",
            "authors": "K Nagessar",
            "source": "University of Pretoria (Honours Thesis/Project)"
        },
        {
            "year": 2023,
            "title": "Applications and Topics of Physics in Surgery",
            "authors": "K Nagessar",
            "source": "Alternate Horizons"
        },
        {
            "year": 2020,
            "title": "Importance of Astronomy in Our Education Systems",
            "authors": "K Nagessar",
            "source": "CosmosNow Online Magazine"
        }
    ]

    # 2. LOGIC: Try live data first, then manual
    if author_data and "publications" in author_data and len(author_data["publications"]) > 0:
        all_pubs = author_data.get("publications", [])
        all_pubs.sort(key=lambda x: x.get("bib", {}).get("pub_year", 0), reverse=True)
        
        st.success("Fetched live data from Google Scholar.")
        for pub in all_pubs:
            bib = pub.get("bib", {})
            with st.expander(f"({bib.get('pub_year', 'N/A')}) {bib.get('title')}"):
                st.write(f"**Authors:** {bib.get('author')}")
                st.write(f"**Source:** {bib.get('journal', 'Publication')}")
                if st.button("Fetch Abstract", key=pub.get('author_pub_id')):
                    with st.spinner("Loading..."):
                        full_pub = scholarly.fill(pub)
                        st.write(full_pub.get('bib', {}).get('abstract', 'No abstract available.'))
    else:
        # 3. SHOW MANUAL DATA IF SCHOLAR FAILS
        st.warning("Google Scholar is currently unreachable. Showing archived publication list.")
        for p in manual_pubs:
            with st.expander(f"({p['year']}) {p['title']}"):
                st.write(f"**Authors:** {p['authors']}")
                st.write(f"**Source:** *{p['source']}*")
                st.markdown(f"[Search on Google Scholar](https://scholar.google.com/scholar?q={p['title'].replace(' ', '+')})")
            

            
# --- TAB 4: EDUCATION ---
with tabs[3]: 
    st.subheader("Academic Background")
    
    col_edu, col_logo = st.columns([2, 1])
    
    with col_edu:
        st.markdown("""
        ### **University of Pretoria**
        
        **Bachelor of Science Honours** | *Physics* *(Feb 2026 - Present)*
        * Currently pursuing a Bachelor of Science Honours in Physics.

        ---

        **Bachelor of Science** | *Physics, Mathematics & Astronomy* *(Feb 2022 - Dec 2025)*
        * Completed a Bachelor of Science in Physics with electives in **Pure Mathematics**, **Applied Mathematics**, and **Astronomy** up to third-year level. 
        * Conducted undergraduate research in the **Electronic Materials and Thin Films Group**. 
        * Authored several publications in undergrad. 
        * Appointed as a practical demonstrator for **PHY 114** in 2025.
        """)



# --- TAB 5: RESEARCH VISITS ---
with tabs[4]:
    st.subheader("Research Visits & Collaborations")
    st.write("Details of institutional visits and collaborative research projects.")
    
    import pandas as pd
    import pydeck as pdk
    
    # -----------------------------
    # Data Setup
    # -----------------------------
    locations = pd.DataFrame([
        {
            "name": "University of Pretoria (Gauteng, SA)",
            "lat": -25.7479, 
            "lon": 28.2293,
            "color": [255, 0, 0, 200]  # Red
        },
        {
            "name": "Woldia University (Ethiopia)",
            "lat": 11.8288, 
            "lon": 39.5932,
            "color": [0, 0, 255, 200]  # Blue
        }
    ])
    
    arc_data = pd.DataFrame([{
        "start_lat": -25.7479,
        "start_lon": 28.2293,
        "end_lat": 11.8288,
        "end_lon": 39.5932
    }])
    
    # -----------------------------
    # PyDeck Map
    # -----------------------------
    view_state = pdk.ViewState(
        latitude=-7.0,
        longitude=34.0,
        zoom=3,
        pitch=40
    )
    
    scatter_layer = pdk.Layer(
        "ScatterplotLayer",
        locations,
        get_position="[lon, lat]",
        get_color="color",
        get_radius=150000,
        pickable=True
    )
    
    arc_layer = pdk.Layer(
        "ArcLayer",
        arc_data,
        get_source_position="[start_lon, start_lat]",
        get_target_position="[end_lon, end_lat]",
        get_source_color=[255, 0, 0, 150],
        get_target_color=[0, 0, 255, 150],
        get_width=5,
    )
    
    # If the map is blank on the website, change map_style to None 
    # or use "pdk.map_styles.SATELLITE"
    r = pdk.Deck(
            layers=[scatter_layer, arc_layer],
            initial_view_state=view_state,
            tooltip={"text": "{name}"},
            map_style=None  # This removes the Mapbox requirement
        )
    
    st.pydeck_chart(r)
    

# --- TAB 6: TEACHING ---
with tabs[5]:
    st.subheader("Teaching Experience")
    st.markdown("""
    - **Practical Demonstrator** | *University of Pretoria* (Feb 2025 - June 2025)
        - Assisting first-year physics students (**PHY 114**) with laboratory experiments.
        - Guiding students through fundamental physics concepts and data analysis techniques.
        - Responsible for ensuring laboratory safety and equipment maintenance.
    """)

# --- TAB 7: SKILLS ---
with tabs[6]:
 
    # Research Skills Section
    st.markdown("### **Research Skills**")
    st.markdown("---")
    col_res1, col_res2 = st.columns(2)
    
    with col_res1:
        st.write("**Theory & Physics**")
        st.write("- Semiconductor Physics\n- Theory of Defects\n- Radiation Physics")
    
    with col_res2:
        st.write("**Characterization Techniques**")
        st.write("- I–V (Current-Voltage) & C–V (Capacitance-Voltage) measurements")
        st.write("- Conventional and Laplace DLTS (Deep Level Transient Spectroscopy)")

    st.info("💡 **Experience:** Working with low-energy electron radioactive sources, such as **Strontium-90**.")

    # Technical Skills Section
    st.markdown("### **Technical Skills**")
    st.markdown("---")
    col_tech1, col_tech2 = st.columns(2)
    
    with col_tech1:
        st.write("**Programming & Markup**")
        st.write("- Python, SageMath, Delphi, and LaTeX")
    
    with col_tech2:
        st.write("**Software**")
        st.write("- Microsoft Office (Word, Excel, PowerPoint)")

    # Languages Section
    st.markdown("### **Languages**")
    st.markdown("---")
    l_col1, l_col2 = st.columns(2)
    
    with l_col1:
        st.write("**English:** Home language")
        st.write("**Afrikaans:** Fair proficiency (studied as First Additional Language)")
        
    with l_col2:
        st.write("**French:** Fair proficiency (**DELF B1** certified)")
        st.write("**Hindi:** Basic proficiency (Self-studied)")
        
# Social Media / Department Section
    st.markdown("### **Social Media Management**")
    st.markdown("---")
    
    st.write("📸 **Managed Content:** University of Pretoria Physics Department Instagram Page")
    
    # Replace the URL with the actual handle if different
    st.link_button("🌐 Visit UP Physics on Instagram", "https://www.instagram.com/up_tuks_physics/")
        
# --- TAB 8: AWARDS ---
with tabs[7]:
    st.subheader("Awards & Recognition")
    st.success("🏆 **ARSO-SABS National Essay Competition** - 2nd National Winner (2025)")
    st.info("📝 **TSSS Essay Competition** - Publication & Top 5 Entry (2023)")

# --- TAB 9: CONTACT ---
with tabs[8]:
    st.subheader("Get in Touch")
    st.write("📍 Department of Physics, University of Pretoria")

    st.markdown("📧 **Email:** [nagessar.kaveer@gmail.com](mailto:nagessar.kaveer@gmail.com)")














