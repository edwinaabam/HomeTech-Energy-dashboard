import streamlit as st
import streamlit.components.v1 as components

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="HomeTech SmartSense Platform",
    page_icon="⚡",
    layout="wide"
)

# ---------------------------------------------------
# CSS
# ---------------------------------------------------

st.markdown("""
<style>

.stApp {
    background-color: #F4F6F9;
}

.banner {
    background-color: #E67E22;
    padding: 1.2rem;
    border-radius: 8px;
    text-align: center;
    color: white;
    font-size: 1.6rem;
    font-weight: 600;
    margin-bottom: 20px;
}

.ai-box {
    background-color: white;
    border-radius: 10px;
    padding: 15px;
    border: 1px solid #e6e6e6;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.markdown(
    "<div class='banner'>⚡ HomeTech SmartSense Platform — IoT Energy & Property Analytics</div>",
    unsafe_allow_html=True
)

# ---------------------------------------------------
# MAIN LAYOUT
# ---------------------------------------------------

main_col, ai_col = st.columns([4,1])

# ===================================================
# MAIN APPLICATION AREA
# ===================================================

with main_col:

    tab1, tab2, tab3 = st.tabs([
        "About Platform",
        "Energy & Maintenance Dashboard",
        "Business Insights Report"
    ])

# ---------------------------------------------------
# TAB 1 — ABOUT
# ---------------------------------------------------

    with tab1:

        st.header("About the SmartSense Analytics Platform")

        st.markdown("""
The **HomeTech SmartSense Platform** provides property managers with real-time
visibility into energy consumption, tenant behaviour, and equipment performance
across **169 smart rental apartments**.

The platform analyzes IoT sensor data to identify inefficiencies, optimize HVAC
usage, and support proactive maintenance planning.

### Key Capabilities

• Monitor energy consumption across rental units  
• Identify peak energy demand patterns  
• Analyze HVAC settings and tenant behaviour  
• Detect maintenance trends and equipment failures  
• Access insights through an AI-powered assistant  

### How to Use the Platform

1. Explore the **Energy Dashboard** to monitor operational performance  
2. Review the **Business Insights Report** for strategic findings  
3. Generate the **Full Operational Insight Report**  
4. Ask questions using the **AI Assistant on the right**
""")

# ---------------------------------------------------
# TAB 2 — DASHBOARD
# ---------------------------------------------------

    with tab2:

        st.header("Energy Usage & Maintenance Dashboard")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Total Rental Units", "169")
        col2.metric("Total Energy Consumption", "72,761 kWh")
        col3.metric("Average Energy per Unit", "430 kWh")
        col4.metric("Maintenance Requests", "345")

        st.divider()

        excel_embed_url = "https://1drv.ms/x/c/62ed36bcf96b63c6/IQTReiVIWbsOS5OupYuHIIlIAdvsv_naDcjm9k72CfGl7qk?em=2&wdHideGridlines=True&wdHideHeaders=True&wdDownloadButton=False"

        components.html(
            f"""
            <iframe
                src="{excel_embed_url}"
                width="100%"
                height="800"
                frameborder="0"
                scrolling="no">
            </iframe>
            """,
            height=810
        )

# ---------------------------------------------------
# TAB 3 — BUSINESS INSIGHTS
# ---------------------------------------------------

    with tab3:

        st.header("Operational Insights")

        st.info("Summary Insights from Dashboard")

        # Consulting-style executive insight cards
        colA, colB, colC = st.columns(3)

        colA.success("""
**Key Insight**

HVAC usage is the primary driver of energy demand
across the **169 monitored apartments**.
""")

        colB.warning("""
**Operational Risk**

HVAC failures account for **44% of all maintenance
requests**, indicating equipment strain during
peak demand periods.
""")

        colC.info("""
**Strategic Opportunity**

Smart thermostat limits and preventive maintenance
can significantly reduce energy waste and system failures.
""")

        st.divider()

        st.markdown("""
The SmartSense analytics platform analyzed IoT sensor data from **169 smart rental apartments**
to understand how energy consumption, tenant behaviour, and maintenance events interact across the property portfolio.

### Key Observations from the Dashboard

• **HVAC usage is the primary driver of energy demand** across the monitored apartments.

• Total energy consumption across the portfolio reached **72,761 kWh**, with average unit consumption of approximately **430 kWh per apartment**.

• Energy demand increases significantly during **evening and night hours**, reflecting typical residential occupancy patterns.

• Maintenance activity is strongly linked to HVAC system performance, with **HVAC failures accounting for 44% of service requests**.

• Operational data highlights **Unit U493 as the highest maintenance-frequency unit**, suggesting possible equipment inefficiencies.
""")

        # Toggle logic
        if "show_report" not in st.session_state:
            st.session_state.show_report = False

        col1, col2 = st.columns(2)

        with col1:
            if st.button("Generate Full Insight Report"):
                st.session_state.show_report = True

        with col2:
            if st.session_state.show_report:
                if st.button("Hide Report"):
                    st.session_state.show_report = False

        # FULL REPORT
        if st.session_state.show_report:

            st.subheader("Executive Summary")

            st.markdown("""
HomeTech Solutions manages **169 smart rental apartments** equipped with IoT sensors that continuously monitor:

• Energy consumption  
• Indoor environmental conditions  
• HVAC system performance  

Key operational metrics observed:

• **Total energy consumption:** 72,761 kWh  
• **Average HVAC setting:** 3.05  
• **Total maintenance requests:** 345
""")

            st.subheader("Energy Consumption Insights")

            st.markdown("""
Key observations from the energy analysis:

• Energy consumption varies seasonally with higher demand during warmer months  
• Peak energy demand occurs during **evening and night hours**  
• HVAC settings strongly influence energy consumption  

Comparison of HVAC usage levels:

• **High HVAC setting:** average 23.65 energy units  
• **Low HVAC setting:** average 9.75 energy units  

This confirms that **HVAC usage is the primary driver of energy demand**.
""")

            st.subheader("Maintenance & Operations Insights")

            st.markdown("""
Maintenance records revealed several operational patterns:

• **Total maintenance requests recorded:** 345  
• **HVAC failures:** 44% of all maintenance issues  
• Other common issues include:
  - Filter replacements  
  - Thermostat malfunctions  

Operational risk indicators:

• Maintenance events increase during periods of heavy HVAC usage  

**High-risk unit identified**

• Unit **U493 recorded the highest maintenance frequency with 13 service requests**
""")

            st.subheader("Strategic Recommendations")

            st.markdown("""
**1. Optimize HVAC Protocols**

• Implement smart thermostat limits  
• Reduce excessive HVAC usage  

**2. Preventive Maintenance Scheduling**

• Schedule HVAC inspections before peak seasons  

**3. Manage Peak Hour Energy Demand**

• Encourage tenant awareness programs  

**4. Targeted Unit Inspections**

• Prioritize inspection of **Unit U493**
""")

            st.subheader("Conclusion")

            st.markdown("""
HVAC usage and tenant occupancy patterns are the **primary drivers of energy consumption** across HomeTech’s rental portfolio.

By implementing **predictive maintenance strategies and smarter HVAC policies**, HomeTech can:

• Reduce operational costs  
• Improve tenant comfort  
• Extend equipment lifespan  
• Improve energy efficiency
""")

# ===================================================
# AI ASSISTANT
# ===================================================

with ai_col:

    st.markdown("<div class='ai-box'>", unsafe_allow_html=True)

    st.subheader("🤖 AI Insights Assistant")

    st.write("Example questions you can ask:")

    st.markdown("""
• How does HVAC usage affect energy consumption?  
• Which unit has the highest maintenance requests?  
• When does energy consumption peak?  
""")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    question = st.chat_input("🤖 Ask about energy, HVAC, or maintenance")

    if question:

        st.session_state.messages.append({"role":"user","content":question})

        with st.chat_message("user"):
            st.write(question)

        knowledge = {
            "hvac":"Units operating under high HVAC settings consume about 23.65 energy units compared with 9.75 units under low settings.",
            "maintenance":"HVAC failures represent 44% of maintenance requests.",
            "u493":"Unit U493 recorded the highest maintenance frequency with 13 service requests.",
            "peak":"Energy demand peaks during evening and night hours when tenants return home.",
            "occupancy":"Occupied apartments show significantly higher energy consumption due to HVAC and appliance usage."
        }

        response = "Try asking about HVAC usage, maintenance patterns, occupancy impact, or peak energy demand."

        q = question.lower()

        for key in knowledge:
            if key in q:
                response = knowledge[key]

        st.session_state.messages.append({"role":"assistant","content":response})

        with st.chat_message("assistant"):
            st.write(response)

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.divider()
st.caption("© 2026 HomeTech Solutions | Smart Property Analytics")