# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: ChoreWheel
def recommend_next(chore_assignments):
    """Score uncompleted chores to suggest the next one.
    
    Parameters:
    chore_assignments (list of dict): Each dict has keys 'name', 'assigned_to', 
                                       'last_done' (str date or None), 'priority' (int).
    
    Returns:
    list of dict: Top 3 scored chore suggestions.
    """
    today = datetime.date.today().isoformat()
    scored = []
    for c in chore_assignments:
        if c.get('completed', False):
            continue
        score = 0
        if c.get('priority', 3) <= 2:
            score += 5
        elif c.get('priority', 3) == 1:
            score += 3
        if c.get('last_done') is None:
            score += 10
        elif c.get('last_done', '') < today:
            days_ago = (datetime.date.today() - datetime.date.fromisoformat(c['last_done'])).days
            if days_ago >= 7:
                score += 8
            elif days_ago >= 3:
                score += 5
            else:
                score += 2
        scored.append({**c, 'score': score})
    scored.sort(key=lambda x: x['score'], reverse=True)
    return scored[:3]
