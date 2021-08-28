
question_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            # If set to VAR, content must contain a symbolic expression
            # If set to TXT, content can be anything
            "type": { "enum": ["VAR", "TXT"] },
            "content": { "type": "string" }
        }
    }
}

answer_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            # Must be a symbolic expression (for now)
            "choice": { "type": "string" },
            "correct": { "type": "boolean" }
        }
    }
}

assignment_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "question": question_schema,
            "answer": answer_schema
        }
    }
}
