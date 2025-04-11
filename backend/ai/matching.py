from .nlp_utils import analyze_text
from typing import List, Dict

def process_story(story: str) -> Dict:
    """Process story text into keywords/sentiment"""
    return analyze_text(story)

def find_matches(target_id: str, stories: List[Dict], top_n: int = 3) -> List[Dict]:
    """Find matches for a user based on processed stories"""
    target = next(s for s in stories if s['id'] == target_id)
    scores = []
    
    for story in stories:
        if story['id'] == target_id:
            continue
            
        # Calculate match score (60% keywords, 40% sentiment)
        keyword_overlap = len(set(target['keywords']) & set(story['keywords']))
        sentiment_diff = 1 - abs(target['sentiment'] - story['sentiment'])
        score = 0.6 * keyword_overlap + 0.4 * sentiment_diff
        
        scores.append({
            "id": story['id'],
            "score": round(score, 2),
            "preview": story['story'][:50] + "...",
            "shared_keywords": list(set(target['keywords']) & set(story['keywords']))
        })
    
    return sorted(scores, key=lambda x: x['score'], reverse=True)[:top_n]