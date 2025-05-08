# Import necessary classes
from crewai import Agent,LLM
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()


# Initialize the LLM using GPT-4o
llm = LLM(
    model="openai/gpt-4o",
    temperature=0.7      # Controls randomness; 0.7 allows creativity while maintaining coherence
)

# Define the Customer Support Representative Agent
customer_support_representative = Agent(
    role="Customer Support Representative",
    goal="Deliver the most friendly and effective customer support within your team.",
    backstory=(
        # Context and motivation for how this agent should behave in its role
		"You are employed at the Department for Work and Pensions (https://www.gov.uk/) "
        "and are currently tasked with providing customer support to {customer}, "
        "an exceptionally important client for the organization. "
        "Your responsibility is to ensure the highest quality of support, "
        "providing complete, detailed answers without making any assumptions."
	),
    allow_delegation=False, # Prevents this agent from delegating its tasks to others
    verbose=True,           # Enables detailed logs for debugging and transparency
    llm=llm                 # Assigns the pre-configured LLM to this agent
)

# Define the Quality Assurance Specialist Agent
quality_assurance_specialist = Agent(
    role="Support Quality Assurance Specialist",
    goal="Be recognized for delivering the best support quality assurance within your team.",
    backstory=(
        # Context for this QA agent to review support interactions with a critical eye
		"You are part of the Department for Work and Pensions (https://www.gov.uk/), "
        "working with your team to fulfill a request from {customer}. "
        "Your task is to ensure that the support representative delivers "
        "exceptional and complete customer support. "
        "All answers must be thorough, detailed, and free of assumptions."
	),
    verbose=True,
    llm=llm
)