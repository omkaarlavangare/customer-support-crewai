from crewai import Crew
from agents import customer_support_representative, quality_assurance_specialist
from tasks import inquiry_resolution, quality_assurance_review
import streamlit as st

def main():
    st.title("Customer Support CrewAI System")
    st.markdown("""
    This system uses AI agents to handle customer inquiries for Department for Work and Pensions and ensure quality responses.
    """)

    # Input fields
    customer_name = st.text_input("Enter your name here")
    customer_inquiry = st.text_area("How can I help you?")

    if st.button("Search"):
        with st.spinner("AI Agents are working on your query...Please wait"):
            # Create and run the crew
            crew = Crew(
                agents=[customer_support_representative, quality_assurance_specialist],
                tasks=[inquiry_resolution, quality_assurance_review],
                verbose=True,
                memory=True
            )

            inputs = {
                "customer": customer_name,
                "inquiry": customer_inquiry
            }
            
            result = crew.kickoff(inputs=inputs)
            
            # Display results
            st.success("Inquiry processed successfully!")
            st.subheader("Response:")
            st.write(result.raw)

if __name__ == "__main__":
    main()