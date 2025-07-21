#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from aula_1_2.crew import Aula12

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")



# /////////////////// executar o crewai //////////////////////////////
# entra na pasta do projeto
# cd "C:\1_EstudosPython\codigos_Aplicacoes_IA__3\9_2-Deploy_com_CrewAI\codigos_das_aulas_IA__3-9_2\aula_1_2" && cls
# ou
# cd "9_2-Deploy_com_CrewAI\codigos_das_aulas_IA__3-9_2\aula_1_2" && cls
# executando o arquivo main.py
# crewai run
# /////////////////////////////////////////////////////////////////////////



def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI LLMs',
        'current_year': str(datetime.now().year)
    }
    
    try:
        Aula12().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        Aula12().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Aula12().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    
    try:
        Aula12().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
