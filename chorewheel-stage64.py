# === Stage 64: Add validation for relationship references ===
# Project: ChoreWheel
def validate_relationships(assignment: Assignment) -> str:
    """Validate that relationship references in an assignment are valid."""
    errors = []
    if assignment.relationship is not None:
        if assignment.relationship not in RELATIONSHIP_TYPES:
            errors.append(f"Invalid relationship type: {assignment.relationship}")
        if assignment.relationship and assignment.relationship not in [r for r in assignment._schema.get('valid_relationships', [])]:
            errors.append(f"Relationship '{assignment.relationship}' not in allowed set for this assignment schema")
    return "; ".join(errors)
