from datasets import Dataset
from ragas.metrics import faithfulness, answer_relevancy, context_precision
from ragas.evaluation import evaluate

# Sample data: Replace with your own RAG output
data = {
    "question": [
        "What is the capital of France?",
        "Who wrote Hamlet?"
    ],
    "answer": [
        "The capital of France is Paris.",
        "Hamlet was written by William Shakespeare."
    ],
    "contexts": [
        ["Paris is the capital of France. It is known for the Eiffel Tower."],
        ["William Shakespeare wrote many plays. One of them is Hamlet."]
    ],
    "ground_truth": [
        "Paris",
        "William Shakespeare"
    ]
}

# Create a dataset
dataset = Dataset.from_dict(data)

# Run RAGAS evaluation
result = evaluate(
    dataset,
    metrics=[faithfulness, answer_relevancy, context_precision]
)

# Print evaluation results
print("\nEvaluation Scores:")
print(result)
