# Import classes and pre-defined agents
from crewai import Task
from agents import customer_support_representative, quality_assurance_specialist
from tools import tool

# Define a task for resolving a customer's inquiry
inquiry_resolution = Task(
    description=(
        # Describes the scenario the agent will handle.
        "{customer} has just submitted a critical inquiry:\n"
        "{inquiry}\n\n"
        "Utilize all available resources and knowledge "
        "to provide the highest standard of support. "
        "Your response must be complete, accurate, and directly address "
        "all aspects of the customer's inquiry."
    ),
    expected_output=(
        # Outlines the expected output from the agent performing this task.
	    "A detailed, informative response that thoroughly addresses "
        "the customer's inquiry. "
        "The response should include references to all sources and tools utilized "
        "to gather information, ensuring that no aspect of the inquiry is left unanswered. "
        "Maintain a helpful, friendly tone throughout the response."
    ),
    agent=customer_support_representative, # Assigns the customer support agent to this task
    tools=[tool]  # Provides any necessary tools the agent can use to complete the task
)


# Define a task for quality assurance review of the support response
quality_assurance_review = Task(
    description=(
        # Describes what the QA agent should evaluate in the support response
        "Conduct a comprehensive review of the response prepared by the Customer Support Representative "
        "for {customer}'s inquiry. "
        "Evaluate whether the answer is accurate, complete, and upholds the highest standards "
        "of customer service.\n"
        "Ensure that every element of the customer's inquiry is addressed with a helpful and friendly tone.\n"
        "Verify that appropriate references and sources have been used to support the response, "
        "and confirm that no questions are left unanswered."
    ),
    expected_output=(
        # Outlines the final deliverable that the QA agent should produce
        "A final, polished, and detailed response that is ready for delivery to the customer. "
        "The response must fully address the customer's inquiry, incorporate all necessary feedback and improvements, "
        "and maintain a professional and friendly tone throughout."
    ),
    agent=quality_assurance_specialist,
)