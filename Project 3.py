"""Simple Recommendation System"""

#Small dataset: item name -> set of tags/genres 
ITEMS = {
    "Inception":          {"sci-fi", "thriller", "mindbending", "action"},
    "The Notebook":        {"romance", "drama", "emotional"},
    "The Dark Knight":     {"action", "thriller", "superhero", "crime"},
    "Interstellar":        {"sci-fi", "space", "drama", "emotional"},
    "La La Land":          {"romance", "musical", "drama"},
    "John Wick":           {"action", "thriller", "crime"},
    "The Hangover":        {"comedy", "friendship"},
    "Toy Story":           {"animation", "comedy", "family", "friendship"},
    "Get Out":             {"horror", "thriller", "mindbending"},
    "The Grand Budapest Hotel": {"comedy", "drama", "quirky"},
}

ALL_TAGS = sorted({tag for tags in ITEMS.values() for tag in tags})


def get_user_interests():
    """Ask the user to pick interests from the available tag list."""
    print("Available interests:")
    print(", ".join(ALL_TAGS))
    print()

    raw_input_str = input(
        "Enter your interests, separated by commas (e.g. action, comedy): "
    )

    # Clean up input: split on commas, strip whitespace, lowercase
    interests = {tag.strip().lower() for tag in raw_input_str.split(",") if tag.strip()}
    return interests


def similarity_score(user_interests, item_tags):
    """
    Calculate how well an item matches user interests using
    Jaccard similarity: (shared tags) / (total unique tags involved).
    Returns a value between 0 (no match) and 1 (perfect match).
    """
    if not user_interests or not item_tags:
        return 0.0

    intersection = user_interests & item_tags   # tags in common
    union = user_interests | item_tags          # all tags combined

    return len(intersection) / len(union)


def recommend_items(user_interests, top_n=3):
    """Score every item and return the top N matches."""
    scored_items = []

    for name, tags in ITEMS.items():
        score = similarity_score(user_interests, tags)
        if score > 0:  # only keep items with at least some overlap
            scored_items.append((name, score, tags & user_interests))

    # Sort by score, highest first
    scored_items.sort(key=lambda x: x[1], reverse=True)

    return scored_items[:top_n]


def display_recommendations(recommendations):
    """Print the recommended items in a readable format."""
    print("\n" + "=" * 50)
    if not recommendations:
        print("No matches found. Try different or broader interests!")
    else:
        print("Top Recommendations:")
        for rank, (name, score, matched_tags) in enumerate(recommendations, start=1):
            print(f"{rank}. {name}  (match: {score:.0%})")
            print(f"   Matched tags: {', '.join(sorted(matched_tags))}")
    print("=" * 50)


def main():
    print("=" * 50)
    print(" Simple Movie Recommendation System")
    print("=" * 50)

    user_interests = get_user_interests()

    if not user_interests:
        print("No interests entered. Exiting.")
        return

    recommendations = recommend_items(user_interests, top_n=3)
    display_recommendations(recommendations)


if __name__ == "__main__":
    main()