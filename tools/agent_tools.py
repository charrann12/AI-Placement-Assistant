from langchain.tools import tool 
from tools.ats_checker import ats_checker
from tools.resume_analysis import resume_analysis
from tools.resume_qa import resume_qa
from tools.interview_qns import interview_questions
from tools.skill_gap import skill_gap_analyser

def create_tools(llm, documents, vector_store):

## ATS checker tool
    @tool
    def ats_checker_agent_tool(jd:str)->str:
        """
        ALWAYS use this tool when the user provides a job description
        and asks for ATS score, ATS compatibility, keyword matching,
        resume comparison, or resume optimization.
        """
        print("ats checker tool called")
        report =  ats_checker(
            llm,
            vector_store,
            jd
        )

        return f"""
ATS Score: {report.ats_score}/100

Matching Keywords:
{", ".join(report.matching_keywords)}

Missing keywords:
{", ".join(report.missing_keywords)}

Suggestions:
- """ + "\n- ".join(report.suggestions)


## Resume Analysis tool
    @tool
    def resume_analysis_agent_tool() -> str:
        """
        Analyze the uploaded resume and provide strengths,
        weaknesses and suggestions.
        """
        print("Resume resume analysis tool called")
        return resume_analysis(
            llm,
            documents
        )

## Interview qns tool   
    @tool
    def interview_questions_agent_tool(target_role:str)->str:
        """
    ALWAYS use this tool when the user asks for:

    - Interview questions
    - Mock interviews
    - HR interview questions
    - Technical interview questions
    - Behavioral interview questions
    - Resume-based interview preparation

    Generates personalized interview questions
    using the uploaded resume.
    """
        print("interview tool called")
        report = interview_questions(
            llm,
            vector_store,
            target_role
        )
        
        output = []

        output.append("## Easy Questions: ")

        for q in report.easy_questions:
            output.append(
                f"""
Question: {q.question}

Expected answer: {q.expected_answer}
"""
            )
        output.append("## Medium Questions: ")

        for q in report.medium_questions:
            output.append(
                f"""
Question: {q.question}

Expected answer: {q.expected_answer}
"""
            )
        output.append("## Hard Questions: ")

        for q in report.hard_questions:
            output.append(
                f"""
Question: {q.question}

Expected answer: {q.expected_answer}
"""
            )
        
        return "\n".join(output)
            
    
    @tool
    def resume_qa_agent_tool(question:str)->str:
        """
        Answer questions about the uploaded resume.
        Use this tool whenever the user asks about
        projects, skills, experience, education,
        achievements, internships or resume details.
        """
        print("Resume QA tool called")

        return resume_qa(
            llm,
            vector_store,
            question
        )
    
    @tool
    def skill_gap_agent_tool(jd: str)->str:
        """
        Analyse skill gaps between the uploaded resume
        and a job description 
        """
        print("Resume skill gap tool called")
        report = skill_gap_analyser(
            llm,
            vector_store,
            jd
        )

        return f"""
Matching Skills:
-{"\n-".join(report.matching_skills)}

Missing Skills:
-{"\n-".join(report.missing_skills)}

Priority Skills:
-{"\n-".join(report.priority_skills)}

Learning Roadmap:
-{"\n-".join(report.learning_roadmap)}
"""


    return [
        ats_checker_agent_tool,
        resume_analysis_agent_tool,
        interview_questions_agent_tool,
        resume_qa_agent_tool,
        skill_gap_agent_tool
    ]

    